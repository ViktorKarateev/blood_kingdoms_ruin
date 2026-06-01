"""Основной игровой класс Blood Kingdoms: Ruin."""

import pygame

from core.settings import (
    BACKGROUND_COLOR,
    FPS,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    WINDOW_WIDTH,
)
from map.grid import Grid
from render.renderer import Renderer


class Game:
    """Управляет окном игры, событиями и главным игровым циклом."""

    def __init__(self) -> None:
        """Инициализировать игру и создать основные объекты pygame."""
        pygame.init()

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)

        self.grid = Grid(radius=3)
        self.renderer = Renderer(self.screen)

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self) -> None:
        """Запустить главный игровой цикл."""
        while self.running:
            self._handle_events()
            self._update()
            self._draw()

            self.clock.tick(FPS)

        pygame.quit()

    def _handle_events(self) -> None:
        """Обработать события окна, клавиатуры и мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def _update(self) -> None:
        """Обновить игровое состояние."""
        pass

    def _draw(self) -> None:
        """Отрисовать текущий кадр."""
        self.screen.fill(BACKGROUND_COLOR)
        self.renderer.draw_grid(self.grid)

        pygame.display.flip()

        current_fps = int(self.clock.get_fps())
        pygame.display.set_caption(f"{WINDOW_TITLE} | FPS: {current_fps}")
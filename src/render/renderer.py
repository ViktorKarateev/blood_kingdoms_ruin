"""Отрисовщик игровых объектов."""

from math import cos, pi, sin

import pygame

from core.settings import (
    DEBUG_SHOW_HEX_COORDINATES,
    HEX_SIZE,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)
from map.grid import Grid
from map.hex import Hex
from utils.hex_math import hex_to_pixel


HEX_OUTLINE_COLOR = (90, 90, 96)
HEX_FILL_COLOR = (34, 34, 40)
HEX_COORDINATES_COLOR = (150, 150, 160)
HEX_SELECTED_COLOR = (90, 42, 42)

class Renderer:
    """Отвечает за отрисовку карты и игровых объектов."""

    def __init__(self, screen: pygame.Surface) -> None:
        """Сохранить поверхность экрана для дальнейшей отрисовки."""
        self.screen = screen
        self.debug_font = pygame.font.Font(None, 18)

    def draw_grid(self, grid: Grid) -> None:
        """Отрисовать все гексы карты."""
        for hex_cell in grid.all_hexes():
            self._draw_hex(hex_cell)

    def _draw_hex(self, hex_cell: Hex) -> None:
        """Отрисовать одну гекс-клетку."""
        center_x, center_y = hex_to_pixel(hex_cell, HEX_SIZE)

        center_x += WINDOW_WIDTH / 2
        center_y += WINDOW_HEIGHT / 2

        points = self._get_hex_corners(center_x, center_y)

        pygame.draw.polygon(self.screen, HEX_FILL_COLOR, points)
        pygame.draw.polygon(self.screen, HEX_OUTLINE_COLOR, points, width=2)

        if DEBUG_SHOW_HEX_COORDINATES:
            self._draw_hex_coordinates(hex_cell, center_x, center_y)

    def _get_hex_corners(
        self,
        center_x: float,
        center_y: float,
    ) -> list[tuple[float, float]]:
        """Вернуть координаты шести углов гекса."""
        points = []

        for index in range(6):
            angle_radians = pi / 180 * (60 * index - 30)

            x = center_x + HEX_SIZE * cos(angle_radians)
            y = center_y + HEX_SIZE * sin(angle_radians)

            points.append((x, y))

        return points

    def _draw_hex_coordinates(
        self,
        hex_cell: Hex,
        center_x: float,
        center_y: float,
    ) -> None:
        """Отрисовать axial-координаты гекса в центре клетки."""
        text = self.debug_font.render(
            f"{hex_cell.q},{hex_cell.r}",
            True,
            HEX_COORDINATES_COLOR,
        )
        text_rect = text.get_rect(center=(center_x, center_y))

        self.screen.blit(text, text_rect)
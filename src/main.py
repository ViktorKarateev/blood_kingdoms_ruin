"""Точка входа в игру Blood Kingdoms: Ruin."""

from core.game import Game


def main() -> None:
    """Создать и запустить экземпляр игры."""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
"""Математические функции для работы с гексами."""

from math import sqrt

from map.hex import Hex


def hex_to_pixel(hex_cell: Hex, hex_size: int) -> tuple[float, float]:
    """Перевести axial-координаты гекса в экранные координаты.

    Используется ориентация pointy-top:
    гекс стоит острым углом вверх.
    """
    x = hex_size * sqrt(3) * (hex_cell.q + hex_cell.r / 2)
    y = hex_size * 3 / 2 * hex_cell.r

    return x, y
"""Гексагональная сетка карты."""

from map.hex import Hex


class Grid:
    """Хранит набор гекс-клеток и управляет доступом к ним."""

    def __init__(self, radius: int) -> None:
        """Создать гекс-карту заданного радиуса.

        Радиус — это размер карты от центра до края.

        Например:
        radius = 1 даст 7 клеток:
        центр + 6 соседей.

        radius = 2 даст уже 19 клеток.
        """
        self.radius = radius
        self.hexes = self._generate_hexes()

    def _generate_hexes(self) -> dict[tuple[int, int], Hex]:
        """Сгенерировать гексы внутри заданного радиуса."""
        hexes: dict[tuple[int, int], Hex] = {}

        for q in range(-self.radius, self.radius + 1):
            r_min = max(-self.radius, -q - self.radius)
            r_max = min(self.radius, -q + self.radius)

            for r in range(r_min, r_max + 1):
                hex_cell = Hex(q=q, r=r)
                hexes[(q, r)] = hex_cell

        return hexes

    def get_hex(self, q: int, r: int) -> Hex | None:
        """Вернуть гекс по axial-координатам, если он есть на карте."""
        return self.hexes.get((q, r))

    def all_hexes(self) -> list[Hex]:
        """Вернуть список всех гексов карты."""
        return list(self.hexes.values())
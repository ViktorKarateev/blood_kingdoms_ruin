"""Модель одной гексагональной клетки карты."""

from dataclasses import dataclass


HEX_DIRECTIONS = (
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
)


@dataclass(frozen=True)
class Hex:
    """Хранит axial-координаты одной гекс-клетки.

    В axial-системе у гекса есть две координаты:
    q — колонка по диагональной оси;
    r — строка по диагональной оси.

    Третья cube-координата s вычисляется через q и r.
    """

    q: int
    r: int

    @property
    def s(self) -> int:
        """Вернуть третью cube-координату гекса."""
        return -self.q - self.r

    def neighbor(self, direction_index: int) -> "Hex":
        """Вернуть соседний гекс по индексу направления от 0 до 5."""
        direction = HEX_DIRECTIONS[direction_index]
        q_offset, r_offset = direction

        return Hex(
            q=self.q + q_offset,
            r=self.r + r_offset,
        )

    def neighbors(self) -> list["Hex"]:
        """Вернуть список всех шести соседних гексов."""
        return [self.neighbor(index) for index in range(6)]
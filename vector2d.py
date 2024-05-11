import math
from typing import Union


class Vector2D:
    """
    Simple 2D Vector class
    """
    __slots__ = ('x', 'y')

    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    def __eq__(self, other: 'Vector2D') -> bool:
        return self.x == other.x and self.y == other.y

    def __add__(self, other) -> 'Vector2D':
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        elif isinstance(other, Union[int, float]):
            return Vector2D(self.x + other, self.y + other)
        else:
            raise TypeError(f'Cannot add {type(other)} to Vector2D')
    __radd__ = __add__

    def __iadd__(self, other) -> 'Vector2D':
        if isinstance(other, Vector2D):
            self.x += other.x
            self.y += other.y
        elif isinstance(other, Union[int, float]):
            self.x += other
            self.y += other
        else:
            raise TypeError(f'Cannot add {type(other)} to Vector2D')
        return self

    def __sub__(self, other) -> 'Vector2D':
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        elif isinstance(other, Union[int, float]):
            return Vector2D(self.x - other, self.y - other)
        else:
            raise TypeError(f'Cannot subtract {type(other)} to Vector2D')
    __rsub__ = __sub__

    def __isub__(self, other) -> 'Vector2D':
        if isinstance(other, Vector2D):
            self.x -= other.x
            self.y -= other.y
        elif isinstance(other, Union[int, float]):
            self.x -= other
            self.y -= other
        else:
            raise TypeError(f'Cannot subtract {type(other)} to Vector2D')
        return self

    def __mul__(self, other) -> 'Vector2D':
        if isinstance(other, Union[float, int]):
            return Vector2D(self.x * other, self.y * other)
        elif isinstance(other, Vector2D):
            return Vector2D(self.x * other.x, self.y * other.y)
        else:
            raise TypeError(f'Cannot multiply {type(other)} to Vector2D')
    __rmul__ = __mul__

    def __imul__(self, other) -> 'Vector2D':
        if isinstance(other, Vector2D):
            self.x *= other.x
            self.y *= other.y
        elif isinstance(other, Union[int, float]):
            self.x *= other
            self.y *= other
        else:
            raise TypeError(f'Cannot multiply {type(other)} to Vector2D')
        return self

    def __truediv__(self, factor: float) -> 'Vector2D':
        return Vector2D(self.x / factor, self.y / factor)

    def __itruediv__(self, factor: float) -> 'Vector2D':
        self.x /= factor
        self.y /= factor
        return self

    def __pow__(self, power: float) -> 'Vector2D':
        return Vector2D(self.x ** power, self.y ** power)

    def __ipow__(self, power: float) -> 'Vector2D':
        self.x **= power
        self.y **= power
        return self

    def __pos__(self) -> 'Vector2D':
        return Vector2D(self.x, self.y)

    def __neg__(self) -> 'Vector2D':
        return Vector2D(-self.x, -self.y)

    def __copy__(self) -> 'Vector2D':
        return Vector2D(self.x, self.y)

    def __repr__(self) -> str:
        return f"Vector2D(x={self.x}, y={self.y})"

    def dot(self, other: 'Vector2D') -> float:
        """
        Dot product between two vectors
        """
        return (self.x * other.x) + (self.y * other.y)
    scalar = dot

    def dist(self) -> float:
        """
        Length of vector
        """
        return math.sqrt(self.x**2 + self.y**2)
    length = norm = dist

    def normalize(self) -> 'Vector2D':
        """
        Normalize a vector
        """
        if self.dist() != 0:
            return Vector2D(self.x, self.y) / self.dist()
        return self

    def to_tuple(self) -> tuple[float, float]:
        return self.x, self.y

    def axis(self, vector: 'Vector2D') -> 'Vector2D':
        v = self - vector
        if v.dist() != 0:
            return -v / v.dist()
        return -v

    @staticmethod
    def zero() -> 'Vector2D':
        return Vector2D(0, 0)


if __name__ == '__main__':
    v1 = Vector2D(3, 0)
    v2 = Vector2D(0, 3)
    assert v1 + v2 == Vector2D(3, 3)
    assert 2 * v1 == Vector2D(6, 0)
    assert v1 / 2 == Vector2D(3/2, 0)
    assert v1 - v2 == Vector2D(3, -3)
    assert v1 * v2 == Vector2D.zero()

    v1 += Vector2D(2, 2)
    assert v1 == Vector2D(5, 2)

    print(Vector2D(2, 2).axis(Vector2D(4, 4)))
    import copy

    v1 = copy.copy(v2)
    print(v1, v2)
    v1 += 10
    print(v1, v2)




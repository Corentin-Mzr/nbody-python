import pygame
import copy

from vector2d import Vector2D, math


class Particle:
    def __init__(self, mass: float, position: Vector2D, velocity: Vector2D, acceleration: Vector2D):
        self.mass: float = mass
        self.position: Vector2D = position
        self.velocity: Vector2D = velocity
        self.acceleration: Vector2D = acceleration
        self.previous_position: list[Vector2D] = []

        self.radius = max(16.0, min(64.0, self.mass * 0.01))

    def __repr__(self):
        return (f"Particle("
                f"Position(x={self.position.x}, y={self.position.y}), "
                f"Velocity(x={self.velocity.x}, y={self.velocity.y}), "
                f"Acceleration(x={self.acceleration.x}, y={self.acceleration.y}))")

    def update(self, dt: float) -> None:
        """
        Update particle motion
        """
        self.__update_velocity(dt)
        self.__update_position(dt)
        self.__update_acceleration()

    def __update_position(self, dt: float) -> None:
        if len(self.previous_position) <= 100:
            self.previous_position.append(copy.copy(self.position))
        else:
            self.previous_position.pop(0)
            self.previous_position.append(copy.copy(self.position))
        self.position += self.velocity * dt

    def __update_velocity(self, dt: float) -> None:
        self.velocity += self.acceleration * dt

    def __update_acceleration(self) -> None:
        self.acceleration = Vector2D(x=0, y=0)

    def apply_force(self, force: Vector2D) -> None:
        """
        Apply a force to the particle
        """
        if self.mass != 0:
            self.acceleration += force / self.mass

    def dist(self, particle: 'Particle') -> float:
        """
        Compute distance between two particles
        """
        return (particle.position - self.position).dist()

    def axis(self, particle: 'Particle') -> Vector2D:
        """
        Unit vector between two particles
        """
        return self.position.axis(particle.position)

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw a particle on screen
        """
        x_min = -5
        x_max = 5
        y_min = -5
        y_max = 5
        width, height = surface.get_size()

        y_a = height / (y_max - y_min)
        y_b = (height - y_a * (y_min + y_max)) / 2

        x_a = width / (x_max - x_min)
        x_b = (width - x_a * (x_min + x_max)) / 2

        centered_pos: Vector2D = self.position * Vector2D(x_a, y_a) + Vector2D(x_b, y_b)

        self.__draw_circle(surface, centered_pos)
        self.__draw_vector(surface, centered_pos, self.velocity, color=(0, 255, 0))
        #self.__draw_vector(surface, centered_pos, self.acceleration, color=(0, 0, 255))
        self.__draw_trailing(surface, (x_a, x_b, x_a, y_b))

    def __draw_circle(
            self,
            surface: pygame.Surface,
            position: Vector2D
    ) -> None:
        pygame.draw.circle(
            surface=surface,
            radius=self.radius,
            center=position.to_tuple(),
            color=(255, 255, 255)
        )

    @staticmethod
    def __draw_vector(
            surface: pygame.Surface,
            start_pos: Vector2D,
            end_pos: Vector2D,
            color: tuple[int, int, int] = (255, 255, 255)
    ) -> None:
        size = 100
        normalized_start = start_pos.normalize()
        normalized_end = normalized_start + end_pos.normalize()
        angle = math.atan2(normalized_end.y - normalized_start.y, normalized_end.x - normalized_start.x)
        arrow_size = 10
        vec1 = arrow_size * Vector2D(math.cos(angle - math.pi / 6), math.sin(angle - math.pi / 6))
        vec2 = arrow_size * Vector2D(math.cos(angle + math.pi / 6), math.sin(angle + math.pi / 6))
        arrow_points = [
            (start_pos + size * end_pos - vec1).to_tuple(),
            (start_pos + size * end_pos).to_tuple(),
            (start_pos + size * end_pos - vec2).to_tuple(),
        ]

        # Draw arrow shaft
        pygame.draw.line(
            surface=surface,
            color=color,
            start_pos=start_pos.to_tuple(),
            end_pos=(start_pos + size * end_pos).to_tuple(),
            width=3
        )

        # Draw arrowhead
        pygame.draw.polygon(
            surface=surface,
            color=color,
            points=arrow_points
        )

    def __draw_trailing(
            self,
            surface: pygame.Surface,
            coefs: tuple[float, float, float, float]
    ) -> None:
        xa, xb, ya, yb = coefs
        for i, vector in enumerate(self.previous_position[::-1]):
            centered_pos: Vector2D = vector * Vector2D(xa, ya) + Vector2D(xb, yb)
            prev_x, prev_y = centered_pos.to_tuple()
            alpha = int(255 * (i + 1) / len(self.previous_position))
            pygame.draw.circle(
                surface=surface,
                color=(255, alpha, alpha, alpha),
                center=(prev_x, prev_y),
                radius=1
            )


if __name__ == '__main__':
    p = Particle(
        mass=1,
        position=Vector2D(0, 0),
        velocity=Vector2D(0, 0),
        acceleration=Vector2D(1, 0)
    )

    p.update(dt=1)

    print(p)

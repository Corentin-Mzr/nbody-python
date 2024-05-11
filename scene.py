import random
from particle import Particle, Vector2D, math


class Scene:
    def __init__(self, seed: int = 0):
        random.seed(seed)
        self.nb_particles: int = 10
        self.particles: list[Particle] = [
            Particle(3300, Vector2D.zero(), Vector2D.zero(), Vector2D.zero()),
            Particle(1, Vector2D(1.0167103, 0), Vector2D(0, 2 * 0.6128), Vector2D.zero()),
            Particle(0.1, Vector2D(1.66599116, 0), Vector2D(0, 2 * 0.45969), Vector2D.zero()),
        ]

        # c = 0.26
        #self.particles: list[Particle] = [
        #    Particle(mass=1, position=Vector2D(x=1, y=0), velocity=Vector2D(x=0, y=c), acceleration=Vector2D.zero()),
        #    Particle(mass=1, position=Vector2D(x=0, y=1), velocity=Vector2D(x=-c, y=0), acceleration=Vector2D.zero()),
        #    Particle(mass=1, position=Vector2D(x=-1, y=0), velocity=Vector2D(x=0, y=-c), acceleration=Vector2D.zero()),
        #    Particle(mass=1, position=Vector2D(x=0, y=-1), velocity=Vector2D(x=c, y=0), acceleration=Vector2D.zero()),
        #    Particle(mass=100, position=Vector2D.zero(), velocity=Vector2D.zero(), acceleration=Vector2D.zero())
        #
        #]
        #for _ in range(self.nb_particles):
        #    rd_pos: Vector2D = Vector2D(x=random.uniform(-1.5, 1.5), y=random.uniform(-1.5, 1.5))
        #    rd_vel: Vector2D = Vector2D(x=random.uniform(-1.5, 1.5), y=random.uniform(-1.5, 1.5))
        #    acc: Vector2D = Vector2D(x=0, y=0)

        #    self.particles.append(
        #        Particle(
        #            mass=1.0,
        #            position=rd_pos,
        #            velocity=rd_vel,
        #            acceleration=acc
        #        )
        #    )

    def update(self, dt: float) -> None:
        self.attract()
        for particle in self.particles:
            particle.update(dt)

    @staticmethod
    def attraction(p1: Particle, p2: Particle) -> Vector2D:
        """ Compute attraction of p1 over p2 """
        G = 2.95e-4
        force = G * p1.mass * p2.mass / p1.dist(p2) ** 2
        return force * p2.axis(p1)

    def attract(self) -> None:
        for particle1 in self.particles:
            for particle2 in self.particles:
                if id(particle1) != id(particle2):
                    force = self.attraction(particle1, particle2)
                    particle2.apply_force(force)


if __name__ == "__main__":
    scene = Scene()
    print(scene.particles)

    scene.update(1.0)
    print(scene.particles)
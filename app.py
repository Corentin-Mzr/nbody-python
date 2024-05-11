import pygame as pg
from scene import Scene, Vector2D
import math


class App:
    def __init__(self, title: str, width: int, height: int):
        pg.init()
        self.screen: pg.Surface = pg.display.set_mode((width, height))
        self.title: str = title
        self.width: int = width
        self.height: int = height
        pg.display.set_caption(title)
        self.clock: pg.time.Clock = pg.time.Clock()
        self.running: bool = True
        self.fps: float = 0

        self.previous_time: float = 0
        self.scene: Scene = Scene()
        self.dt: float = 0.01

    def run(self) -> None:
        """
        Run the app
        """
        while self.running:
            self.update(self.dt)
            self.handle_events()
            self.clear()
            self.draw()
            self.display()

        self.__quit()

    def update(self, dt: float) -> None:
        self.update_fps()
        self.scene.update(dt)

    def update_fps(self) -> None:
        current_time: float = pg.time.get_ticks()
        if current_time - self.previous_time > 1000.0:
            pg.display.set_caption(f"{self.title} | FPS: {self.fps}")
            self.fps = 0
            self.previous_time = current_time
        else:
            self.fps += 1

    def handle_events(self) -> None:
        """
        Handle events
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def clear(self) -> None:
        """
        Clear the screen
        """
        self.screen.fill(color=(30, 30, 100))

    def draw(self) -> None:
        """
        Draw on screen
        """
        for particle in self.scene.particles:
            particle.draw(self.screen)

    def display(self) -> None:
        """
        Refresh clock and display new frame
        """
        self.clock.tick(144)
        pg.display.flip()

    @staticmethod
    def __quit():
        """
        Quit the app
        """
        pg.quit()


# circleshape.py
import pygame
from typing import ClassVar, Iterable, cast

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    # any iterable of sprite groups
    containers: ClassVar[Iterable[pygame.sprite.AbstractGroup]]

    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            # tell the type checker this is the right type
            super().__init__(*cast(Iterable[pygame.sprite.AbstractGroup], self.containers))
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: float = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius

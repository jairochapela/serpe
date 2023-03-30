class Field:
    def __init__(self, surface) -> None:
        self.surface = surface

    def draw(self):
        self.surface.fill((0,0,0))
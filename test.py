import pygame
import random
import sys

# Параметры окна
WIDTH, HEIGHT = 600, 400

# Количество частиц
NUM_PARTICLES = 150

# Класс частицы
class Particle:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)

    def update(self):
        self.x += self.vx
        self.y += self.vy

        # отражение от краёв
        if self.x < 0 or self.x > WIDTH:
            self.vx *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.vy *= -1

    def draw(self, surface):
        # цвет с градиентом по высоте
        gradient = int(255 * self.y / HEIGHT)
        color = (gradient, 120, 255 - gradient)
        pygame.draw.circle(surface, color, (int(self.x), int(self.y)), 4)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    particles = [Particle() for _ in range(NUM_PARTICLES)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        for p in particles:
            p.update()
            p.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

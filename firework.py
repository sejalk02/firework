import pygame
import random
import math


pygame.init()


width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Firework Using Framework")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]


font_size = 36  
font = pygame.font.SysFont(None, font_size) 
text = font.render('Firework', True, BLACK)  
text_rect = text.get_rect(center=(width // 2, height // 2))  


class Firework:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.particles = []
        self.create_particles()

    def create_particles(self):
        num_particles = 100
        for _ in range(num_particles):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(1, 5)
            color = random.choice(COLORS)
            dx = speed * math.cos(angle)
            dy = speed * math.sin(angle)
            self.particles.append({'x': self.x, 'y': self.y, 'dx': dx, 'dy': dy, 'color': color, 'life': random.randint(30, 60)})

    def update(self):
        for particle in self.particles:
            particle['x'] += particle['dx']
            particle['y'] += particle['dy']
            particle['life'] -= 1

        self.particles = [p for p in self.particles if p['life'] > 0]

    def draw(self, surface):
        for particle in self.particles:
            pygame.draw.circle(surface, particle['color'], (int(particle['x']), int(particle['y'])), 3)


running = True
fireworks = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            fireworks.append(Firework(x, y))

    screen.fill(WHITE)  

    for firework in fireworks:
        firework.update()
        firework.draw(screen)

  
    screen.blit(text, text_rect)

    pygame.display.flip()
    pygame.time.delay(16)  

pygame.quit()

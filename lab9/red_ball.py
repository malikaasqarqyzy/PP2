import pygame
pygame.init()

WHITE = (255,255,255)
RED = (255,0,0)

size = weight, hight = 690, 690
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Ellipse')
clock = pygame.time.Clock()

color = RED

x, y = 100, 100
dx, dy = 0, 0

done = False
while not done:
    for event in pygame.event.get():
        key = pygame.key.get_pressed()

        if event.type == pygame.QUIT:
            done = True

        if key[pygame.K_w]:
            dx, dy = 0, -20
            x += dx
            y += dy

            if y < 0:
                x -= dx
                y -= dy

            pygame.draw.ellipse(screen, color, [x, y, 50, 50])

        if key[pygame.K_s]:
            dx, dy = 0, 20
            x += dx
            y += dy

            if y > 650:
                x -= dx
                y -= dy

            pygame.draw.ellipse(screen, color, [x, y, 50, 50])

        if key[pygame.K_a]:
            dx, dy = -20, 0
            x += dx
            y += dy

            if x < 0:
                x -= dx
                y -= dy

            pygame.draw.ellipse(screen, color, [x, y, 50, 50])

        if key[pygame.K_d]:

            dx, dy = 20, 0
            x += dx
            y += dy

            if x > 650:
                x -= dx
                y -= dy

            pygame.draw.ellipse(screen, color, [x, y, 50, 50])

    screen.fill(WHITE)
    pygame.draw.ellipse(screen, color, [x, y, 50,50])
    clock.tick(60)
    pygame.display.update()
pygame.quit()
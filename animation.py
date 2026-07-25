import pygame
import math

WIDTH=1000
HEIGHT=800

origin = (WIDTH//2,HEIGHT//2)
scale = 0.4

def draw(components):
    print(len(components))
    print(len(components[0]))
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    t=0
    clock = pygame.time.Clock()
    path=[]
    running = True
    

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((30,30,30))
        for contour in components:
            center_x = origin[0]
            center_y = origin[1]

            for comp in contour:
                radius = comp.amplitude * scale
                angle = comp.frequency * t + comp.phase
                x = center_x + radius * math.cos(angle)
                y = center_y + radius * math.sin(angle)

                # circle
                pygame.draw.circle(screen, (100, 100, 100), (int(center_x),int(center_y)), int(radius), 1)

                # rotating vector
                pygame.draw.line(screen, (255, 255, 255), (int(center_x),int(center_y)), (int(x), int(y)), 2)

                # endpoint
                center_x = x
                center_y = y
            pygame.draw.circle(screen, (255, 0, 0), (int(center_x),int(center_y)), 5)
            path.append((center_x, center_y))
        if len(path) > 1:
            int_path = [(int(x), int(y)) for x, y in path]
            pygame.draw.lines(
                screen,
                (0,255,255),
                False,
                int_path,
                2
            )    
        # t+=0.02
        t += 2 * math.pi / len(components[0])
        if t >= 2 * math.pi:
            t = 0
            path.clear()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
import pygame
import random

def draw_grid(screen):

    # Horizontal Lines
    for y in range(0, 512, 32):
        pygame.draw.line(screen, "black", (0, y), (640, y))

    # Vertical Lines
    for x in range(0, 640, 32):
        pygame.draw.line(screen, "black", (x, 0), (x, 512))

def to_grid_pos(pos):
    return (pos[0] // 32, pos[1] // 32)

def main():

    try:
        pygame.init()

        # Load mole image
        mole_image = pygame.image.load("mole.png")

        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        
        # Mole coords
        mole_x, mole_y = 0, 0

        running = True
        while running:
            for event in pygame.event.get():
                # Exit Game
                if event.type == pygame.QUIT:
                    running = False
                # On click event
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Gets the 2D index of the mole's square
                    mole_square = to_grid_pos((mole_x, mole_y))
                    # Gets the 2D index of the clicked square
                    clicked_square = to_grid_pos(event.pos)

                    # If user clicks on mole's square, reassign mole's position
                    if mole_square == clicked_square:
                        # Gets the new square indices with randrage() and then converts them to coordinates
                        mole_x = random.randrange(0, 20) * 32
                        mole_y = random.randrange(0, 16) * 32
            
            # Draw Background
            screen.fill("light green")
            draw_grid(screen)
            
            # Draw moles' coordinates
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x,mole_y)))
            
            # Update graphics
            pygame.display.flip()
            
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

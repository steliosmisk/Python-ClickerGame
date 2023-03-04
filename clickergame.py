import pygame
import random

# Define game colors
RED = (255, 0, 0)
GREEN = (0, 255, 51)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (80, 80, 255)
YELLOW = (255, 255, 0)

# Initialize pygame and game display
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Fast Clicker Game")
clock = pygame.time.Clock()

# Create a Rectangle class to represent game elements
class Rectangle:
    def __init__(self, x, y, width, height):
        self.image = None
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, color):
        pygame.draw.rect(screen, color, self.rect)

    def set_text(self, text, font_size, x, y):
        self.image = pygame.font.SysFont('verdana', font_size).render(text, True, BLACK)
        screen.blit(self.image, (x, y))

    def draw_text(self, shift_x=0, shift_y=0):
        screen.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

# Game Variables
buttons = []
wait = 0
x = 70
score = 0

# Create game score and time display
score_display = Rectangle(0, 0, 0, 0)

# Create game buttons
for i in range(4):
    button = Rectangle(x, 90, 70, 100)
    button.draw(YELLOW)
    button.set_text('CLICK', 15, x, 90)
    buttons.append(button)
    x += 100

# Game loop
running = True
while running:
    # Limit frame rate and update display
    clock.tick(60)
    pygame.display.update()

    # Update game elements every 20 frames
    if wait == 0:
        screen.fill(LIGHT_BLUE)
        score_display.set_text(f'Score: {score}', 20, 0, 0)
        wait = 20
        click = random.randint(1, len(buttons))

        # Draw game buttons and highlight one of them
        for i, button in enumerate(buttons):
            if (i + 1) == click:
                button.draw_text(10, 40)
            else:
                button.draw(YELLOW)

    else:
        wait -= 1

    # Check for player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos

            # Check if player clicked the highlighted button
            for i, button in enumerate(buttons):
                if button.collidepoint(x, y):
                    if (i + 1) == click:
                        button.draw(GREEN)
                        score += 1
                    else:
                        button.draw(RED)
                        score -= 1

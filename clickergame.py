from random import randint
import pygame

# Game Colors
RED = (255, 0, 0)
GREEN = (0, 255, 51)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (80, 80, 255)
YELLOW = (255, 255, 0)

# Display
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Fast Clicker Game")
clock = pygame.time.Clock()
screen.fill(LIGHT_BLUE)


# Rectangles
class Rectangles:
    def __init__(self, x, y, width, height):
        self.image = None
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, color):
        pygame.draw.rect(screen, color, self.rect)

    def set_text(self, text, fsize, x, y):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, BLACK)
        screen.blit(self.image, (x, y))

    def draw_text(self, shift_x=0, shift_y=0):
        screen.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


# Game Variables
buttons = []
wait = 0
x = 70
score_game = 0

# Game Score / Time
score_text = Rectangles(0, 0, 0, 0)
for _ in range(4):
    clicker_buttons = Rectangles(x, 90, 70, 100)
    clicker_buttons.draw(YELLOW)
    clicker_buttons.set_text('CLICK', 15, x, 90)
    buttons.append(clicker_buttons)
    x += 100

running = True
while running:
    pygame.display.update()
    clock.tick(60)
    if wait == 0:
        screen.fill(LIGHT_BLUE)
        score_text.set_text(f'Score: {score_game}', 20, 0, 0)
        wait = 20
        click = randint(1, len(buttons))
        for i in range(len(buttons)):
            buttons[i].draw(YELLOW)
            if (i + 1) == click:
                buttons[i].draw_text(10, 40)
            else:
                buttons[i].draw(YELLOW)
    else:
        wait -= 1

    for event in pygame.event.get():
        if (
                event.type != pygame.QUIT
                and event.type == pygame.KEYDOWN
                and event.key == pygame.K_ESCAPE
                or event.type == pygame.QUIT
        ):
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(len(buttons)):
                if buttons[i].collidepoint(x, y):
                    if (i + 1) == click:
                        buttons[i].draw(GREEN)
                        score_game += 1
                    else:
                        buttons[i].draw(RED)
                        score_game -= 1

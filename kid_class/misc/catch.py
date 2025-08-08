import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Object")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BASKET_COLOR = (0, 128, 255)

# Basket properties
basket_width = 100
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - basket_height - 10
basket_speed = 7

# Falling object properties
object_radius = 20
object_x = random.randint(object_radius, WIDTH - object_radius)
object_y = -object_radius
object_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Clock
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)  # 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Basket movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT]:
        basket_x += basket_speed

    # Keep basket inside screen
    if basket_x < 0:
        basket_x = 0
    if basket_x > WIDTH - basket_width:
        basket_x = WIDTH - basket_width

    # Move the falling object
    object_y += object_speed

    # Check if object is caught
    if (basket_y < object_y + object_radius < basket_y + basket_height) and (
        basket_x < object_x < basket_x + basket_width
    ):
        score += 1
        # Reset object position
        object_x = random.randint(object_radius, WIDTH - object_radius)
        object_y = -object_radius
        # Increase speed slightly for difficulty
        object_speed += 0.2

    # Reset if missed
    if object_y - object_radius > HEIGHT:
        object_x = random.randint(object_radius, WIDTH - object_radius)
        object_y = -object_radius
        # Optionally, you could reset speed or deduct points here

    # Draw everything
    screen.fill(WHITE)
    # Draw basket
    pygame.draw.rect(
        screen, BASKET_COLOR, (basket_x, basket_y, basket_width, basket_height)
    )
    # Draw falling object (circle)
    pygame.draw.circle(screen, RED, (object_x, int(object_y)), object_radius)
    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()

import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREY = (200, 200, 200)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Realistic Roblox Clone")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Player properties
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player_size = 50
player_color = BLUE
player_velocity = [0, 0]
player_speed = 0.3
gravity = 0.5
is_jumping = False
jump_force = -10

# Ground properties
ground_height = 50
ground_color = GREY

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  # Move left
        player_velocity[0] = -player_speed
    elif keys[pygame.K_d]:  # Move right
        player_velocity[0] = player_speed
    else:
        player_velocity[0] = 0

    if keys[pygame.K_SPACE] and not is_jumping:  # Jump
        is_jumping = True
        player_velocity[1] = jump_force

    # Apply gravity
    player_velocity[1] += gravity

    # Update player position
    player_pos[0] += player_velocity[0]
    player_pos[1] += player_velocity[1]

    # Collision detection with the ground
    if player_pos[1] + player_size > SCREEN_HEIGHT - ground_height:
        player_pos[1] = SCREEN_HEIGHT - ground_height - player_size
        player_velocity[1] = 0
        is_jumping = False

    # Prevent player from leaving the screen
    player_pos[0] = max(0, min(SCREEN_WIDTH - player_size, player_pos[0]))

    # Fill screen with background color
    screen.fill(WHITE)

    # Draw ground
    pygame.draw.rect(screen, ground_color, (0, SCREEN_HEIGHT - ground_height, SCREEN_WIDTH, ground_height))

    # Draw player
    pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], player_size, player_size))

    # Refresh screen
    pygame.display.flip()

    # Frame rate control
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
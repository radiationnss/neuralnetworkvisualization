import pygame
import sys
from neural_network import Classify
from slider import Slider1

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
# 750, 50
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neural Network Visualization")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)  # Red with alpha value for transparency
GREEN = (0, 255, 0)  # Green with alpha value for transparency

# Create a transparent surface for overlay
overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
overlay.fill((0, 0, 0, 0))  # Fill with transparent color

# Create sliders
sliders = [
    Slider1((500, 80), (100, 10), 0.5, -1, 1),
    Slider1((500, 100), (100, 10), 0.5, -1, 1),
    Slider1((500, 120), (100, 10), 0.5, -1, 1),
    Slider1((500, 140), (100, 10), 0.5, -1, 1)
]

# Function to draw the axes
def draw_axes():
    # Draw x-axis
    pygame.draw.line(screen, BLACK, (50, HEIGHT - 50), (WIDTH - 50, HEIGHT - 50), 2)
    # Draw y-axis
    pygame.draw.line(screen, BLACK, (50, HEIGHT - 50), (50, 50), 2)

    # Draw axis labels
    font = pygame.font.SysFont(None, 24)
    x_label = font.render("Spot Size -->", True, BLACK)
    x_label_rect = x_label.get_rect(center=(WIDTH - 700, HEIGHT - 30))
    screen.blit(x_label, x_label_rect)

    y_label = font.render("Spike Length -->", True, BLACK)
    y_label = pygame.transform.rotate(y_label, 90)
    y_label_rect = y_label.get_rect(center=(30, 500))
    screen.blit(y_label, y_label_rect)

prev_slider_values = None
BLOCK_SIZE = 5

# Main loop
while True:
    screen.fill(WHITE)
    mouse_pos = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pressed()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Check if slider values have changed
    slider_values = [slider.get_value() for slider in sliders]
    if slider_values != prev_slider_values:
        prev_slider_values = slider_values

        # Clear the overlay
        overlay.fill((0, 0, 0, 0))

        for x_block in range(0, WIDTH, BLOCK_SIZE):
            for y_block in range(0, HEIGHT, BLOCK_SIZE):
                # Calculate block coordinates
                block_rect = pygame.Rect(x_block, y_block, BLOCK_SIZE, BLOCK_SIZE)

                # Classify the block
                result = Classify(x_block + BLOCK_SIZE // 2, y_block + BLOCK_SIZE // 2, *slider_values)

                # Set color for the block based on classification result
                color = RED if result == 1 else GREEN
                pygame.draw.rect(overlay, color, block_rect)
    #this is for gthub
    # Blit the overlay and draw axes
    horizontal_translation = 50  # Adjust as needed
    vertical_translation = -50  # Adjust as needed

    # Flip the overlay vertically and then translate it
    translated_overlay = pygame.transform.flip(overlay, False, True)
    translated_overlay_rect = translated_overlay.get_rect().move(horizontal_translation, vertical_translation)

    # Blit the translated and flipped overlay
    screen.blit(translated_overlay, translated_overlay_rect)
    for slider in sliders:
        if slider.container_rect.collidepoint(mouse_pos) and mouse[0]:
            slider.move_slider(mouse_pos)
        slider.render(screen)

    draw_axes()

    pygame.display.update()
    pygame.display.flip()
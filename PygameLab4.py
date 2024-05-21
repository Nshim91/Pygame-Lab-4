import pygame
import math
import random

pygame.init()

# Define some colours
black = (   0,   0,   0)
white = ( 255, 255, 255)
red   = ( 255,   0,   0)
green = (   0, 255,   0)
blue  = (   0,   0, 255)

# Set the width and height of the window
size = [1000, 562]
screen = pygame.display.set_mode(size)

pygame.display.set_caption('MONKEY SWINGING THROUGH DA JUNGLE')

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

x = 200
y = 100

x2 = 400
y2 = 200

background_image = pygame.image.load('jungle-pic.jpg').convert()
peely = pygame.image.load('monkey.jpg').convert()
peely = pygame.transform.scale(monkey_image, (200, 100)).convert()
peely.set_colorkey(black)
fish_stick = pygame.image.load('banana.png').convert()
fish_stick = pygame.transform.scale(banana_image, (400, 200)).convert()
fish_stick.set_colorkey(black)

# -------- Main Program Loop -----------
while done == False:
  # --- Main event loop
  for event in pygame.event.get(): # User did something
    if event.type == pygame.QUIT: # If user clicked close
      done = True # Flag that we are done so we exit this loop

  # --- Keyboard input goes here
  keys = pygame.key.get_pressed()

  if keys[pygame.K_a] and x > 0:
    x -= 3
  if keys[pygame.K_d] and x < 980:
    x += 3
  if keys[pygame.K_w] and y > 0:
    y -= 3
  if keys[pygame.K_s] and y < 525:
    y += 3

  if keys[pygame.K_LEFT] and x2 > 0:
    x2 -= 3
  if keys[pygame.K_RIGHT] and x2 < 980:
    x2 += 3
  if keys[pygame.K_UP] and y2 > 0:
    y2 -= 3
  if keys[pygame.K_DOWN] and y2 < 525:
    y2 += 3

  # --- Game logic should go here


  # --- Screen clearing goes here.
  screen.blit(background_image, [0, 0])
  screen.blit(monkey_image, [x, y])
  screen.blit(banana_image, [x2, y2])

  # --- Drawing code should go here


  # --- Update the screen with our drawing commands
  pygame.display.flip()

  # --- Limit to 60 frames per second
  clock.tick(60)

# Close the window and quit.
pygame.quit()

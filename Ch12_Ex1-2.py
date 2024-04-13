# Exercise 12-1 Blue Sky: Make a Pygame window with a blue background.

import sys
import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Exercise")
    bg_color = (0, 122, 255)
    character = Character(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        character.blitme()

        pygame.display.flip()


# Exercise 12-2 Game Character: Find a bitmap image of a game character you like or convert an image to bitmap. Make a
# class that draws the character at the center of the screen and match the background color of the image to the back-
# ground color of the screen, or vice versa.


class Character:

    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load("images/exercise-dragonborn.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)


run_game()

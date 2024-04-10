# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 19:06:03 2024

@author: Noah.Payne
"""


import pygame

pygame.init()


#game window
screen_width = 800
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle RPG by NoahCodes')


# load images
# background image
background_img = pygame.image.load('')
run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()

    
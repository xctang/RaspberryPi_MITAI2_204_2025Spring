# This is musicbox program
import pygame
from gpiozero import Button

pygame.init()

Noise = pygame.mixer.Sound("/home/pi/GPIO-Music-Box/Noise.wav")

btn_Noise = Button(17)

btn_Noise.when_pressed = Noise.play

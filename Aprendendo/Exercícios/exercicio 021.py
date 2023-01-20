#função import para colocar áudio para rodar não está funcionando#
import pygame
pygame.init()
pygame.mixer.music.load("musica")
pygame.mixer.music.play()
pygame.event.wait()
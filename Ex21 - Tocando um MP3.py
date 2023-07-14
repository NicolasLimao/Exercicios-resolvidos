import pygame

pygame.init()
pygame.mixer.music.load('C:\\Users\\nicoo\\Desktop\\Ex21.mp3')
pygame.mixer.music.play()

input("Pressione Enter para parar a música...")

pygame.mixer.music.stop()
pygame.quit()


import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play()

# mantém o programa rodando enquanto a música toca
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)


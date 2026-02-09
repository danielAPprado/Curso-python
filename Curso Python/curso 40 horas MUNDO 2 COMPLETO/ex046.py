from time import sleep
import pygame
pygame.init()
pygame.mixer.init()
for c in range(10, 0, -1):
    print(c)
    sleep(1)
sleep(2)
pygame.mixer.music.load("rojao.mp3")
pygame.mixer.music.play()

# mantém o programa rodando enquanto a música toca
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)



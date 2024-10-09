import pygame
import time
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('Eyes Without A Face.mp3')
pygame.mixer.music.play()
pygame.event.wait()
for s in range(0, 301):
    time.sleep(1)
    print(f"{s} segundos.")
    if s == 10:
        print(f"1 minuto e {s-10} segundos")
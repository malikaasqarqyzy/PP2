import pygame

pygame.init()
pygame.mixer.init()

WHITE = (255,255,255)
RED = (255,0,0)

size = weight, hight = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Music player')
clock = pygame.time.Clock()

music_img = pygame.image.load('music_fon.jpg').convert()
player = pygame.image.load('player.jpg').convert()
stop = pygame.image.load('player1.png').convert()

pygame.mixer.music.load('music.mp3')
song = ['music.mp3', 'game.mp3', 'melody.mp3']

done = False
playing_state = False
cnt = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            screen.blit(player, (0, 300))
            pygame.mixer.music.play()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            cnt -= 1
            if cnt < 0:
                cnt = len(song) - 1
            pygame.mixer.music.load(song[cnt])
            pygame.mixer.music.play()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            cnt += 1
            if cnt > len(song) - 1:
                cnt = 0
            pygame.mixer.music.load(song[cnt])
            pygame.mixer.music.play()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            screen.blit(stop, (0, 300))
            pygame.mixer.music.stop()

    screen.blit(music_img, (0, 0))
    clock.tick(60)
    pygame.display.update()
pygame.quit()
import pygame, time

#max_pts = int(input("Enter max points: "))
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brainrot Clicker")
pygame.display.set_icon(pygame.image.load("resources/tungtung.png"))
clock = pygame.time.Clock()
points = 1
sentence = "Click the brainrots. Game ends at 300 pts. "
pygame.font.init()
font = pygame.font.SysFont("Calibri", 20, False)
score_font = pygame.font.SysFont("Calibri", 35, True)
chosen_brainrot = None
tungtung = pygame.image.load("resources/tungtung.png")
patapim = pygame.image.load("resources/patapim.png")
lirili = pygame.image.load("resources/lirililarila.png")
thanks = pygame.image.load("resources/thanks.png")
intro = pygame.image.load("resources/intro.png")
background = pygame.image.load("resources/background.png")
pygame.init()
muted = False
tung_sound = pygame.mixer.Sound("resources/tung.mp3")  # Sound for points <= 50
brr_sound = pygame.mixer.Sound("resources/brr.mp3")  # Sound for points 51-200
lirili_sound = pygame.mixer.Sound("resources/lirili.mp3")  # Sound for points > 200
pygame.mixer.music.load("resources/bgm.mp3")
pygame.mixer.music.play(-1)

#def brainrot_evolve(): 
#    if points <= 50: 
#        chosen_brainrot = pygame.image.load("resources/tungtung.png")
#    elif points >= 51 and points <= 200: 
#        chosen_brainrot = pygame.image.load("resources/patapim.png")
#    else: 
#        chosen_brainrot = pygame.image.load("resources/lirililarila.png")
screen.blit(intro, (0, 0))
pygame.display.flip()
time.sleep(3)

game_loop = True

while game_loop: 
    events = pygame.event.get()
    for event in events: 
        if event.type == pygame.QUIT: 
            game_loop = False
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE: 
                game_loop = False
            if event.key == pygame.K_m: 
                muted = not muted
                if muted: 
                    tung_sound.set_volume(1)
                    brr_sound.set_volume(1)
                    lirili_sound.set_volume(1)
                    pygame.mixer.music.set_volume(1)
                else: 
                    tung_sound.set_volume(0)
                    brr_sound.set_volume(0)
                    lirili_sound.set_volume(0)
                    pygame.mixer.music.set_volume(0)
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 1: #anticheat na myszke
                if brainrot.collidepoint(event.pos): 
                    #print("I")
                    if points <= 50:
                        pygame.mixer.Sound.play(tung_sound)
                    elif points >= 51 and points <= 200:
                        pygame.mixer.Sound.play(brr_sound)
                    else:
                        pygame.mixer.Sound.play(lirili_sound)
                    points += 1
            pass
    if points >= 300: 
        game_loop = False
    #brainrot_evolve()
    #screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    if points <= 50:
        brainrot_image = pygame.image.load("resources/tungtung.png") 
        brainrot = brainrot_image.get_rect()
        brainrot.center = (300, 300)
        screen.blit(brainrot_image, brainrot)
    elif points >= 51 and points <= 200: 
        brainrot_image = pygame.image.load("resources/patapim.png")
        brainrot = brainrot_image.get_rect()
        brainrot.center = (300, 300)
        screen.blit(brainrot_image, brainrot)
    else: 
        brainrot_image = pygame.image.load("resources/lirililarila.png")
        brainrot = brainrot_image.get_rect()
        brainrot.center = (300, 300)
        screen.blit(brainrot_image, brainrot)
    done = (points / 300) * 100
    done_conv = f"{done:.2f}"
    points_text = score_font.render(f"Points: {points}, done: {done_conv}%", True, (255, 255, 255))
    bottom_sentence = score_font.render(f"{sentence}", True, (0, 0, 0))
    screen.blit(points_text, (30, 30))
    screen.blit(bottom_sentence, ((WIDTH // 2 - bottom_sentence.get_width() // 2), 550))
    pygame.display.flip()
    clock.tick(30)
time.sleep(0.7)
screen.blit(thanks, (0, 0))
pygame.display.flip()
time.sleep(3)
pygame.quit()
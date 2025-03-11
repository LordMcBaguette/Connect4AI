import PositionClass
import AlphaBetaPruning as AI
import pygame
import sys
import time

# Initialize PyGame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("AI connect 4!")

# Set the frame rate
clock = pygame.time.Clock()

# Player settings
player_width = 40
player_height = 50
player_x = screen_width // 2 - player_width // 2 -2
player_y = 20
player_speed = 96
player_pos = 3
lCheck = False
rCheck = False
SCheck = False
player_colour = (255,0,0)
board_colour = (0,128,255)
Game = PositionClass.position()
Game.ReadGameState("")
Win = False
# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0 and not lCheck and player_pos > 0:
        player_x -= player_speed
        player_pos -= 1
        lCheck = True
    elif keys[pygame.K_RIGHT] and player_x < screen_width - player_width and not rCheck and player_pos < 6:
        player_x += player_speed
        player_pos += 1
        rCheck = True
    elif keys[pygame.K_SPACE] and not SCheck and Game.LegalPlay(player_pos):
        if Game.checkWin(player_pos):
            Win = True
            winTeam = Game.TurnOrder()
            Game.play(player_pos)
        else:
            Game.play(player_pos)
            nextMove = AI.BestMove(Game)
            if Game.checkWin(nextMove):
                Win = True
                winTeam = Game.TurnOrder()
            Game.play(nextMove)
        SCheck = True


    #Reset button held down checks if the button is released
    if lCheck == True:
        if not keys[pygame.K_LEFT]:
            lCheck = False
    if rCheck == True:
        if not keys[pygame.K_RIGHT]:
            rCheck = False
    if SCheck == True:
        if not keys[pygame.K_SPACE]:
            SCheck = False

    # Fill the screen with black
    screen.fill((0, 0, 0))
    # Draw the board
    pygame.draw.rect(screen, board_colour, (50, 100,700, 650))

    # Draw the player
    if Game.TurnOrder():
        pygame.draw.rect(screen, (255,0,0), (player_x, player_y, player_width, player_height))
    else:
        pygame.draw.rect(screen, (255,255,0), (player_x, player_y, player_width, player_height))
    # Draw the circle pieces:
    pw = 0
    ph = 5
    for Width in range(110,750,96):
        for Height in range(690,150,-100):
            if Game.gamepos[pw][ph] == -1:
                pygame.draw.circle(screen,(255,255,255),(Width,Height),40)
            elif Game.gamepos[pw][ph] == True:
                pygame.draw.circle(screen, (255, 0,0), (Width, Height), 40)
            elif Game.gamepos[pw][ph] == False:
                pygame.draw.circle(screen, (255, 255,0), (Width, Height), 40)
            ph -= 1
        pw += 1
        ph = 5

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)
    if Win:
        time.sleep(2)
        break



print(winTeam)

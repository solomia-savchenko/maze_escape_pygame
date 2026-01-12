import pygame
import random
from pathlib import Path

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Maze")

bg_color = (0, 0, 0)
cell_size = 40

assets_folder = Path(__file__).parent.joinpath("assets")

pygame.mixer.music.load(assets_folder.joinpath("background.mp3"))
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

sound_key = pygame.mixer.Sound(assets_folder.joinpath("sound_key.mp3"))
pygame.mixer.music.set_volume(1)

yay = pygame.mixer.Sound(assets_folder.joinpath("yay.mp3"))
pygame.mixer.music.set_volume(0.1)

sound_door = pygame.mixer.Sound(assets_folder.joinpath("sound_door.mp3"))
pygame.mixer.music.set_volume(1)

background2_img = pygame.image.load(assets_folder.joinpath("background2.png"))
background2_img = pygame.transform.scale(background2_img, (800, 600))

wall_img = pygame.image.load(assets_folder.joinpath("wall.png"))
wall_img = pygame.transform.scale(wall_img, (cell_size, cell_size))

key_img = pygame.image.load(assets_folder.joinpath("key.png"))
key_img = pygame.transform.scale(key_img, (cell_size, cell_size))

door_img = pygame.image.load(assets_folder.joinpath("door.png"))
door_img = pygame.transform.scale(door_img, (cell_size, cell_size))

smile_img = pygame.image.load(assets_folder.joinpath("smile.png"))
smile_img = pygame.transform.scale(smile_img, (300, 300))
smile_img = pygame.transform.scale(smile_img, (300, 300))


player_img = [pygame.image.load(assets_folder.joinpath(f"player{i}.png")) for i in range(1, 6)]
player_img = [pygame.transform.scale(player, (cell_size, cell_size)) for player in player_img]
player_id = 0


def draw_button(screen, text, color, x, y, w, h):
    pygame.draw.rect(screen, color, (x, y, w, h))
    font = pygame.font.SysFont(None, 36)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(
        text_surface,
        (
            x + (w - text_surface.get_width()) / 2,
            y + (h - text_surface.get_height()) / 2
         )
    )


def main_menu():

    menu_is_running = True
    while menu_is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 150 <= x < 650 and 200 <= y <= 300:
                    menu_is_running = False
                if 150 <= x <= 650 and 350 <= y <= 450:
                    menu_is_running = False
                    exit()

        screen.blit(background2_img, (0, 0))
        draw_button(screen, " Start game", (0, 150, 0), 150, 200, 500, 100)
        draw_button(screen, " Exit", (200, 0, 0), 150, 350, 500, 100)
        pygame.display.flip()


def win_menu():
    win_menu_is_running = True
    while win_menu_is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win_menu_is_running = False
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 250 <= x < 550 and 150 <= y <= 400:
                    yay.play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 150 <= x < 650 and 450 <= y <= 550:
                    menu_is_running = False
            

                    exit()
            

        screen.blit(background2_img, (0, 0))
        draw_button(screen, " Congratulations! You get out ", (57, 57, 57), 150, 50, 500, 100)
        screen.blit(smile_img, (250, 150))
        draw_button(screen, " Exit", (200, 0, 0), 150, 450, 500, 100)
        pygame.display.flip()

main_menu()

pygame.display.set_icon(key_img)

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

height = len(maze)
width = len(maze[0])

free_cells = []
for y in range(height):
    for x in range(width):
        if maze[y][x] == 0:
            free_cells.append((x, y))

key_position = random.choice(free_cells[1:-1])
door_position = free_cells[-1]
player_x, player_y = free_cells[0]
has_key = False

clock = pygame.time.Clock()
fps = 10

def start_screen():
    font = pygame.font.Font(None, 40)
    title = font.render("Maze", True, (255, 255, 255))
    story = font.render("You wake up in the maze...", True, (200, 200, 200))
    story2 = font.render("Find a key and open the door!", True, (200, 200, 200))

    play_button = pygame.Rect(300, 300, 200, 50)
    howto_button = pygame.Rect(300, 400, 200, 50)

    while True:
        screen.fill((0, 0, 0))
        screen.blit(title, (320, 100))
        screen.blit(story, (150, 180))
        screen.blit(story2, (100, 220))

        pygame.draw.rect(screen, (100, 200, 100), play_button)
        pygame.draw.rect(screen, (100, 100, 200), howto_button)

        play_text = font.render("PLAY", True, (0, 0, 0))
        howto_text = font.render("How to PLay", True, (255, 255, 255))

        screen.blit(play_text, (play_button.x + 60, play_button.y + 10))
        screen.blit(howto_text, (howto_button.x + 30, howto_button.y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return  
                if howto_button.collidepoint(event.pos):
                    howto_screen()

def howto_screen():
    font = pygame.font.Font(None, 36)
    back_button = pygame.Rect(300, 500, 200, 50)

    while True:
        screen.fill((0, 0, 0))
        controls = [
            " w - Move Up",
            " s - Move down",
            " a - Move left",
            " d - Move right",
            "The goal is to find a key and open the door."
        ]

        for i, line in enumerate(controls):
            text = font.render(line, True, (255, 255, 255))
            screen.blit(text, (100, 100 + i * 40))

        pygame.draw.rect(screen, (200, 100, 100), back_button)
        back_text = font.render("BACK", True, (0, 0, 0))
        screen.blit(back_text, (back_button.x + 60, back_button.y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    return 

start_screen()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and player_x > 0 and maze[player_y][player_x - 1] == 0:
                player_x -= 1
            if event.key == pygame.K_d and player_x < width - 1 and maze[player_y][player_x + 1] == 0:
                player_x += 1
            if event.key == pygame.K_w and player_y > 0 and maze[player_y - 1][player_x] == 0:
                player_y -= 1
            if event.key == pygame.K_s and player_y < height - 1 and maze[player_y + 1][player_x] == 0:
                player_y += 1

    screen.fill(bg_color)

    for y in range(height):
        for x in range(width):
            if maze[y][x] == 1:
                screen.blit(wall_img, (x * cell_size, y * cell_size))

    if not has_key:
        if (player_x, player_y) == key_position:
            has_key = True
            sound_key.play()
        else:
            screen.blit(key_img, (key_position[0] * cell_size, key_position[1] * cell_size))

    screen.blit(door_img, (door_position[0] * cell_size, door_position[1] * cell_size))
    screen.blit(player_img[player_id], (player_x * cell_size, player_y * cell_size))
    player_id = (player_id + 1) % len(player_img)

    if has_key and (player_x, player_y) == door_position:
        sound_door.play()
        running = False

    pygame.display.flip()
    clock.tick(fps)

win_menu()

pygame.quit()

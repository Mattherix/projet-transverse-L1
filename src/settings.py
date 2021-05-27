"""Tous les pramètres du jeux"""
TITLE = "DinoJump"
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = "arial"
HS_FILE = "highscore.txt"

# Propriete des joueurs
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20

# Plateforme de base (x,y,longueur,epaisseur)
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)]

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE

BACKGROUND_PATH = "assets/background"

# Musique et Sond
MUSICS_PATH = "musics"
MUSICS = {
    "menu": [
        ("Ship.ogg", 20, "parallax-mountain.png"),
    ],
    "game": [
        ("Central City.ogg", 30, "Sky.png"),
        ("Common Fight.ogg", 20, "Sky.png"),
        ("Yellow Forest.ogg", 20, "Sky.png"),
        ("Chiptronical.ogg", 10, "Sky.png"),
        ("Dangerous Dungeon.ogg", 10, "Sky.png"),
        ("Boss Fight.ogg", 10, "Sky.png")
    ],
    "game-over": [
        ("Game Over.ogg", 30, "game-over.jpg"),
        ("Major Loss.ogg", 10, "game-over.jpg")
    ]
}
SOUNDS_PATH = "sounds"
SOUNDS = {
    "jump": "Jump 1.wav"
}

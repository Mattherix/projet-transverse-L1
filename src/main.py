"""Fichier principale du programme"""
import pygame as pg
import random
from settings import *
from sprites import Player, Platform, Cloud
from os import path


class Game:
    """La classe représentant le jeu"""
    def __init__(self):
        """INITIALISATION ET CREATION DU JEU"""
        self.highscore = 0
        self.score = 0
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()
        self.mixer = pg.mixer
        self.musics = MUSICS

    def new(self):
        """Creer une nouvelle partie de jeu
           initialisation du score"""
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:  # regarder settings
            # Platform(plat[0], plat[1], ...)
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    # son et image (data)
    def load_data(self):
        """Charge les sauvegardes du joueur, les fichiers audio et les images"""
        self.dir = path.dirname(__file__)
        # Lire le sauvegarde du joueur
        file_location = path.join(self.dir, HS_FILE)
        try:
            with open(file_location, 'r') as f:
                try:
                    self.highscore = int(f.read())
                except ValueError:
                    self.highscore = 0
        except FileNotFoundError:
            with open(file_location, 'w') as f:
                f.write('0')
            self.highscore = 0

    def run(self):
        """Boucle du jeu"""
        self.playing = True
        self.play_music(self.musics['game'], 1000)
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        self.play_music(self.musics['game-over'], 1000)

    def update(self):
        """Update de l'état du jeu"""
        self.all_sprites.update()
        # Lorsqu'il y a une collision
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
                # La velocité du personnage s'arrete lorsqu'il retombe sur une plateforme

        # pour scroller le jeu
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()  # supprime les plateforme qui passe en dessous de l'écran
                    self.score += 10  # lorsqu'il monte il gagne des points

        # Tuer le joueur lorsqu'il tombe
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False

        # Faire apparaitre de nouvelles plateformes
        while len(self.platforms) < 6:  # nombre de plateforme à l'écran
            width = random.randrange(50, 100)  # parametre a changer en fonction de la resolution
            if random.randrange(0, 5):
                p = Platform(random.randrange(0, WIDTH - width),
                             random.randrange(-75, -30),
                             width, 20)
            else:
                p = Cloud(random.randrange(0, WIDTH - width),
                             random.randrange(-75, -30),
                             width, 20)
            self.platforms.add(p)
            self.all_sprites.add(p)

    def events(self):
        """Evenement du jeu"""
        for event in pg.event.get():
            # Fermeture de la fenetre
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        """Dessin de tous les elements du jeu"""

        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 22, WHITE, WIDTH / 2, 15)  # affichage du score du joueur
        pg.display.flip()

    def show_start_screen(self):
        """Écran d'accueil"""
        # TODO: Fenetre d'avant le jeu à parametrer
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 9)
        self.draw_text("et dirigez-vous à l'aide des fleches directionelles", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Appuyer sur Espace pour charger le saut", 22, WHITE, WIDTH / 2, HEIGHT / 3.5)
        self.draw_text("Appuyer sur un bouton pour commencer", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        self.draw_text("Meilleur score: " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT * 3 / 3.5)
        pg.display.flip()
        self.wait_for_key()  # application de la fonction wait-for-key

    def show_go_screen(self):
        """Affiche la fenetre de défaite"""
        if not self.running:
            return
        self.screen.fill(BGCOLOR)
        self.draw_text("C'est perdu! Dommage!", 55, WHITE, WIDTH / 2, HEIGHT / 9)
        self.draw_text("Score: " + str(self.score), 35, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Appuyer sur un bouton pour recommencer", 30, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        if self.score > self.highscore:  # remplacement meilleur score
            self.highscore = self.score
            self.draw_text("NOUVEAU SCORE!", 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
            with open(path.join(self.dir, HS_FILE), 'w') as f:  # nouveau meilleur score dans les data
                f.write(str(self.score))
        else:
            self.draw_text("Votre record est: " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        """Attendre que le joueur appuie sur une touche"""
        waiting = True
        while waiting:
            self.clock.tick(30)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        """Affiche le score du joueur"""
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def play_music(self, musics, fadeout):
        self.mixer.music.fadeout(fadeout)
        # On choisi une musique au hasard, chaque musique à un poids, k est la longueur de la liste renvoyé
        music_name = random.choices(
            [music[0] for music in musics],
            weights=[music[1] for music in musics],
            k=1
        )[0]
        self.mixer.music.load(path.join(self.dir, MUSICS_PATH, music_name))
        self.mixer.music.play(-1)
        self.mixer.music.set_volume(0.4)

    def play_sound(self, sound):
        self.mixer.Sound(path.join(self.dir, SOUNDS_PATH, sound)).play()



g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()

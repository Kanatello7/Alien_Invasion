import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_setting, screen, "Play")

    # Create an instance to store game statistics.
    stats = GameStats(ai_setting)
    sb = Scoreboard(ai_setting, screen, stats)
    # Make a ship
    ship = Ship(ai_setting, screen)
    # Make a group to store bullets in.
    bullets = Group()
    # Make an Alien
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_setting, screen, ship, aliens)

    while True:
        gf.check_events(ai_setting, screen, stats, sb, play_button, ship,
                        aliens, bullets)
        gf.update_screen(ai_setting, screen, stats, sb, ship, aliens,
                         bullets, play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_aliens(ai_setting, screen, stats, sb, ship, aliens,
                             bullets)
        gf.update_screen(ai_setting, screen, stats, sb, ship, aliens, bullets,
                         play_button)


run_game()

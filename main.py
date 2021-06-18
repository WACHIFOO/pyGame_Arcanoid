from classes.game import Game
from classes.player import Player
from classes.ball import Ball

import pygame

if __name__ == '__main__':
    game = Game()
    player = Player()
    ball = Ball()

    game.flip()
    x = 250
    y = 250
    speed = 0
    while game.playing:
        # Controlamos si se pulsa cerrar
        game.trigger_quit_game()

        # Iniciamos el latido
        game.start_hearthbeat()

        # Obtenemos la tecla pulsada y movemos el jugador
        pressed = pygame.key.get_pressed()
        player.movement(pressed)

        # Movemos la Bola
        ball.movement()

        # Checkeamos que la bola y el jugador se esten tocando
        collide = player.player_rect.colliderect(ball.ball_rect)

        if collide:
            ball.cae = False
            ball.movement()

        # Renderizamos el jugador
        player.draw(game.screen)

        # Renderizamos la bola
        ball.draw(game.screen)

        # Finalizamos el latido
        game.end_hearthbeat()
    game.quit_game()


from classes.game import Game
from classes.player import Player
from classes.ball import Ball
from classes.blocks import Blocks

import pygame

if __name__ == '__main__':
    game = Game()
    player = Player()
    ball = Ball()
    block = Blocks(10, 20)

    blocks = {}
    block_x = 0
    block_y = 10
    for i in range(27):
        object_block = Blocks(block_x, block_y)
        blocks[i] = {
            "object": object_block,
            "rect": object_block.block_rect,
        }

        # Controlamos la posicion
        if block_x < 500:
            block_x += 70
        else:
            block_y += 50
            block_x = 0

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
        collide_player = player.player_rect.colliderect(ball.ball_rect)

        if collide_player:
            ball.cae = False
            ball.movement()

        delete_blocks = []
        # Checkeamos que la bola y el bloque colisionen
        for block in blocks:
            collide_block = ball.ball_rect.colliderect(blocks[block]["rect"])
            if collide_block:
                ball.cae = not ball.cae
                ball.movement()
                # Si ha tocado el regalo nos guardamos cual es para borrarlo del array
                delete_blocks.append(block)

        # Borramos el bloque tocado
        for i in delete_blocks:
            del (blocks[i])

        # Renderizamos el jugador
        player.draw(game.screen)

        # Renderizamos la bola
        ball.draw(game.screen)

        # Renderizamos los bloques
        for block in blocks:
            blocks[block]["object"].draw(game.screen)

        # Finalizamos el latido
        game.end_hearthbeat()
    game.quit_game()

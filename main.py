from classes.game import Game

"""
# from classes.player import Player
# from classes.sardina import Sardina
# from classes.scoreUX import ScoreUX
"""
import pygame

if __name__ == '__main__':
    game = Game()
    game.flip()

    x = 250
    y = 250
    speed = 0
    while game.playing:
        # Controlamos si se pulsa cerrar
        game.trigger_quit_game()

        # Iniciamos el latido
        game.start_hearthbeat()

        # Test mover jugador
        keys = pygame.key.get_pressed()

        # Si hay movimiento aplicamos velocidad
        if 1 in keys:
            speed = 1.5
        else:
            if speed > 1.1:
                speed -= 0.1

        # Contrtolamos que tecla pulsa
        if keys[pygame.K_LEFT]:
            x -= 10
        if keys[pygame.K_RIGHT]:
            x += 10
        if keys[pygame.K_UP]:
            y -= 10
        if keys[pygame.K_DOWN]:
            y += 10

        # if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
        #     x -= 1
        #     y -= 1
        # elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
        #     x -= 1
        #     y += 1
        # elif keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
        #     x += 1
        #     y -= 1
        # elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        #     x += 1
        #     y += 1

        # Si llega a uno de los bordes que se vaya al otro lao
        print(x)
        # Derecha
        if x >= 499:
            x = 1
        # Izquieda
        if x <= 0:
            x = 499
        # Abajo
        if y >= 499:
            y = 1
        # Arriba
        if y <= 0:
            y = 499

        # print(str(x) + " - " + str(speed*x))
        # print(str(y) + " - " + str(speed*y))
        pygame.draw.circle(game.screen, (255, 255, 255), (x, y), 15)

        # Finalizamos el latido
        game.end_hearthbeat()
    game.quit_game()

    """
    game = Game()
    player = Player()
    sardina = Sardina()
    score = ScoreUX()
    game.flip()
    while game.playing:
        # Controlamos si se pulsa cerrar
        game.trigger_quit_game()

        # Iniciamos el latido
        game.start_hearthbeat()

        # Obtenemos la tecla pulsada y movemos el jugador
        pressed = pygame.key.get_pressed()
        player.movement(pressed)

        # Renderizamos el jugador
        player.draw(game.screen)

        # Controlamos si el jugador esta sobre la recompensa
        sardina.colision(player.player_rect)
        sardina.check_win()
        sardina.blit(game.screen)

        # Printamos la puntuacion
        score.draw(game.screen, sardina.puntuacion)

        # Finalizamos el latido
        game.end_hearthbeat()
    game.quit_game()
"""

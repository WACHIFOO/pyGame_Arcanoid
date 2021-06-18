import random

import pygame
from random import randint


class Ball:
    def __init__(self):
        self.force = 5  # Fuerza para el movimiento
        self.ball_image = pygame.image.load("sprites/apple.png")
        self.ball = pygame.transform.scale(self.ball_image, (50, 50))

        # Tema posicionamineto en pantalla
        self.ball_rect = self.ball.get_rect()
        self.ball_rect.x = 250
        self.ball_rect.y = 250

        # Rangos maximos de movimiento por pantalla
        self.max_derecha = pygame.display.get_window_size()[0] - self.ball.get_size()[0]
        self.max_izquierda = 0
        self.max_arriba = 0
        self.max_abajo = pygame.display.get_window_size()[1] - self.ball.get_size()[1]

        # variables para saber hacia donde va
        self.cae = randint(0, 1)
        self.bota = randint(0, 1)
        self.fuerzaBote = random.uniform(1, 1.3)

    def draw(self, screen):
        screen.blit(self.ball, self.ball_rect)

    def __check_limits(self):
        """
        Controlamos que no se pase del ux
        """
        if self.ball_rect.x > self.max_derecha:
            self.ball_rect.x = self.max_derecha
        elif self.ball_rect.x < 0:
            self.ball_rect.x = 0

    def movement(self):
        """
        Movemos la bola de manera random en el eje X y ponemos en negativo el eje Y
        :param key_pressed: pygame.key.get_pressed()
        """
        self.__caer()
        self.__botar()

    def __caer(self):
        """
        Movemos la bola para arriba o para abajo
        :return:
        """
        if self.cae:
            self.ball_rect.y += self.force
            # Si llega abajo cambiamos la fuerza para que rebote
            if self.ball_rect.y == 480:
                self.cae = False
                self.bota = randint(0, 1)
                self.fuerzaBote = random.uniform(1, 1.3)
        else:
            self.ball_rect.y -= self.force
            # Si llega abajo cambiamos la fuerza para que rebote
            if self.ball_rect.y == 20:
                self.cae = True
                self.bota = randint(0, 1)
                self.fuerzaBote = random.uniform(1, 1.3)

    def __botar(self):
        """
        Movemos la bola izquierda o derecha
        :return:
        """
        # Aplicamos fuerza a la izquierda o a la derecha
        fuerza_calculada = self.force * self.fuerzaBote
        if self.bota:
            self.ball_rect.x += fuerza_calculada
        else:
            self.ball_rect.x -= fuerza_calculada

        #  Controlamos si rebota horizontalmente
        control_horizontal = self.ball_rect.x < self.max_izquierda or self.ball_rect.x > self.max_derecha

        if control_horizontal:
            self.bota = randint(0, 1)
            self.fuerzaBote = random.uniform(1, 1.3)
            # Hacemos que no se bugee en las esquinas
            if self.ball_rect.x < self.max_izquierda:
                self.ball_rect.x = self.max_izquierda
            elif self.ball_rect.x > self.max_derecha:
                self.ball_rect.x = self.max_derecha

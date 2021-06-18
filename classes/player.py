import pygame


class Player:
    def __init__(self):
        self.force = 5
        self.player_image = pygame.image.load("sprites/leaf.png")
        self.player = pygame.transform.scale(self.player_image, (80, 80))
        self.player_rect = self.player.get_rect()
        self.player_rect.x = 250
        self.player_rect.y = 400
        self.max_derecha = pygame.display.get_window_size()[0] - self.player.get_size()[0]

    def draw(self, screen):
        screen.blit(self.player, self.player_rect)

    def __check_limits(self):
        """
        Controlamos que no se pase del ux
        """
        if self.player_rect.x > self.max_derecha:
            self.player_rect.x = self.max_derecha
        elif self.player_rect.x < 0:
            self.player_rect.x = 0

    def movement(self, key_pressed):
        """
        Nos movemos de izquierda a derecha
        :param key_pressed: pygame.key.get_pressed()
        """
        if key_pressed[pygame.K_LEFT]:
            self.player_rect.x -= self.force
        elif key_pressed[pygame.K_RIGHT]:
            self.player_rect.x += self.force
        self.__check_limits()

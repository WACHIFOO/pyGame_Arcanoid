import pygame


class Blocks:
    def __init__(self, x, y):
        self.force = 5
        self.blocks_image = pygame.image.load("sprites/presentBox.png")
        self.block = pygame.transform.scale(self.blocks_image, (80, 80))
        self.block_rect = self.block.get_rect()
        self.block_rect.x = x
        self.block_rect.y = y
        self.max_derecha = pygame.display.get_window_size()[0] - self.block.get_size()[0]

    def draw(self, screen):
        screen.blit(self.block, self.block_rect)

    # def __check_limits(self):
    #     """
    #     Controlamos que no se pase del ux
    #     """
    #     if self.block_rect.x > self.max_derecha:
    #         self.block_rect.x = self.max_derecha
    #     elif self.block_rect.x < 0:
    #         self.block_rect.x = 0
    #
    # def movement(self, key_pressed):
    #     """
    #     Nos movemos de izquierda a derecha
    #     :param key_pressed: pygame.key.get_pressed()
    #     """
    #     if key_pressed[pygame.K_LEFT]:
    #         self.block_rect.x -= self.force
    #     elif key_pressed[pygame.K_RIGHT]:
    #         self.block_rect.x += self.force
    #     self.__check_limits()

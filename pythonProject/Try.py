import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Crawler")
clock = pygame.time.Clock()

# Load Images
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")
tile_img = pygame.image.load("tile.png")


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(player_img, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 4

    def move(self, dx=0, dy=0):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move(-1, 0)
        if keys[pygame.K_RIGHT]:
            self.move(1, 0)
        if keys[pygame.K_UP]:
            self.move(0, -1)
        if keys[pygame.K_DOWN]:
            self.move(0, 1)


# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(enemy_img, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 2

    def update(self, player):
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        if self.rect.x > player.rect.x:
            self.rect.x -= self.speed
        if self.rect.y < player.rect.y:
            self.rect.y += self.speed
        if self.rect.y > player.rect.y:
            self.rect.y -= self.speed


# Level class
class Level:
    def __init__(self):
        self.tiles = []
        self.enemies = pygame.sprite.Group()
        self.load_level()

    def load_level(self):
        for row in range(0, HEIGHT, TILE_SIZE):
            for col in range(0, WIDTH, TILE_SIZE):
                if random.random() < 0.1:  # Random walls
                    self.tiles.append(pygame.Rect(col, row, TILE_SIZE, TILE_SIZE))
                elif random.random() < 0.05:  # Random enemy
                    self.enemies.add(Enemy(col, row))

    def draw(self, screen):
        for tile in self.tiles:
            screen.blit(tile_img, tile.topleft)


# Main Game Loop
def main():
    running = True
    player = Player(WIDTH // 2, HEIGHT // 2)
    level = Level()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(level.enemies)

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()
        for enemy in level.enemies:
            enemy.update(player)

        level.draw(screen)
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()

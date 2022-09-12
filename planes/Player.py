from weapons.Bullet import Bullet
from sprites import planeSprite, planeLeftSprite, planeRightSprite, planeBoomSprite
import time
import pygame


class Plane:
    def __init__(self, x, y):
        self.sprite = planeSprite
        self.x = x
        self.y = y
        self.health = 2
        self.size = 8
        self.speed = .8
        self.bullets = []
        self.gameOver = None
    
    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed

    def moveRight(self):
        self.x = self.x + self.speed
        self.sprite = planeRightSprite

    def moveLeft(self):
        self.x = self.x - self.speed
        self.sprite = planeLeftSprite
    
    def takeDamage(self):
        self.health = self.health - 1
        if self.health <= 0:
            self.gameOver = time.time() + 2

    def shoot(self):
        self.bullets.append(Bullet(self.x, self.y - self.size/2))

    def handleInputs(self):
        if self.gameOver:
            return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.moveLeft()
        if keys[pygame.K_RIGHT]:
            self.moveRight()
        if keys[pygame.K_UP]:
            self.moveUp()
        if keys[pygame.K_DOWN]:
            self.moveDown()
        if keys[pygame.K_SPACE]:
            self.shoot()

    def update(self, enemies):
        self.handleInputs()

        if self.gameOver and time.time() > self.gameOver:
            exit()

        for b in self.bullets:
            b.update(enemies)

        for e in enemies:
            xDistance = abs(self.x - e.x)
            yDistance = abs(self.y - e.y)
            if (xDistance + yDistance) < self.size:
                self.takeDamage()

    
    def draw(self, screen):
        if not self.gameOver:
            screen.blit(self.sprite, (self.x - self.size/2, self.y - self.size/2))
        else:
            screen.blit(planeBoomSprite, (self.x - self.size/2, self.y - self.size/2))
        self.sprite = planeSprite

        for b in self.bullets:
            b.draw(screen)

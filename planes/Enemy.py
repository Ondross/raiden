import pygame
from weapons.Bullet import Bullet
from util import WIDTH, RateLimiter


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.dead = False
        self.health = 1
        self.color = (0, 180, 180)
        self.recoilCounter = 0
        self.bullets = []
        self.speed = .8
        self.xDir = 1
        self.rateLimiter = RateLimiter()

    def update(self, player):
        speed = self.speed
        if self.recoilCounter > 0:
            speed = self.speed / 2

        if abs(self.y - player.y) < 50:
            if self.rateLimiter.shoot(1):
                self.bullets.append(Bullet(self.x, self.y, True))
            self.x = self.x + speed * self.xDir

            if self.x > WIDTH * .8:
                self.xDir = -1
            elif self.x < WIDTH * .2:
                self.xDir = 1
        else:
            self.y = self.y + speed

        for b in self.bullets:
            b.update([player])

    def takeDamage(self):
        self.health = self.health - 1
        self.recoilCounter = 5
        if self.health <= 0:
            self.dead = True

    def draw(self, screen):
        if not self.dead:
            color = self.color
            if self.recoilCounter > 0:
                color = (255, 0, 0)
            pygame.draw.rect(screen, color, (self.x - self.size / 2, self.y - self.size / 2, self.size, self.size))

        for b in self.bullets:
            b.draw(screen)
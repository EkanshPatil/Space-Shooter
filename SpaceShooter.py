import pgzrun
import random

WIDTH = 800
HEIGHT = 800

ship = Actor("ship")
ship.pos = (400,750)
bullets = []
enemies = []
score = 0

enemy = Actor("enemy")
enemy.pos = (random.randint(50,750),-50)
enemies.append(enemy)

def on_mouse_down(key):
    if key == keys.SPACE:
        bullet = Actor("bullet")
        bullet.pos = (ship.x,ship.y - 30)
        bullets.append(bullet)

def update():
    global score
    if keyboard.left:
        ship.x -= 10
    if keyboard.right:
        ship.x += 10
    ship.x = max(0,min(800,ship.x))
    for bullet in bullets:
        bullet.y -= 10
    if bullet.y < 0:
        bullets.remove(bullet)
    for enemy in enemies:
        enemy.y += 5
    if enemy.y > 800:
        enemy.y = -50
        enemy.x = random.randint(50,750)
    for bullet in bullets:
        if enemy.colliderect(bullet):
            bullets.remove(bullet)
            enemy.y = -50
            enemy.x = random.randint(50,750)
            score += 10

def draw():
    screen.clear()
    screen.blit("background",(0,0))
    ship.draw()
    for enemy in enemies:
        enemy.draw()
    screen.draw.text("score:{}".format(score),topleft=(20,30),color="yellow",fontsize=30)#


pgzrun.go()
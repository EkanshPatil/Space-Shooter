import pgzrun
import random
import time

WIDTH = 800
HEIGHT = 700


ship = Actor("ship")
ship.pos = (400,550)
count = 3
bullets = []
enemies = []
bombs = []
score = 0
ship.dead = False

for i in range(2):
    bomb = Actor("bomb")
    bomb.pos = (random.randint(50,750),-50)
    bombs.append(bomb)

for i in range(5):
    enemy = Actor("enemy")
    enemy.pos = (random.randint(50,750),-50)
    enemies.append(enemy)

def countdown():
    global count
    if count > 0:
        count -= 1
        clock.schedule(countdown,1)

def on_key_down(key):
    if ship.dead == False:
        if key == keys.SPACE:
            bullet = Actor("bullet")
            bullet.pos = (ship.x,ship.y - 30)
            bullets.append(bullet)   

def update():
    global score
    if count > 0:
        return
    if ship.dead == False:
        if keyboard.left:
            ship.x -= 10
        if keyboard.right:
            ship.x += 10
    ship.x = max(0,min(750,ship.x))
    for bullet in bullets:
        bullet.y -= 10
        if bullet.y < 0:
            bullets.remove(bullet)
    for enemy in enemies:
        enemy.y += 5
        if enemy.y > 600:
            enemy.y = -50
            enemy.x = random.randint(50,750)
        for bullet in bullets:
            if enemy.colliderect(bullet):
                sounds.laser.set_volume(0.5)
                sounds.laser.play()
                bullets.remove(bullet)
                enemy.y = -50
                enemy.x = random.randint(50,750)
                score += 10
        if enemy.colliderect(ship):
            sounds.shot.play()
            ship.dead = True
    for bomb in bombs:
        bomb.y += 5
        if bomb.y > 600:
            bomb.y = -50
            bomb.x = random.randint(50,750)
        for bullet in bullets:
            if bomb.colliderect(bullet):
                sounds.shot.play()
                ship.dead = True
        if bomb.colliderect(ship):
            ship.dead = True
            sounds.shot.play()


def draw():
    screen.clear()
    screen.fill("midnightblue")
    if count > 0:
        screen.draw.text(str(count),center=(400,350),color="white",fontsize=80)
        return
    if ship.dead == False:
        ship.draw()
        for enemy in enemies:   
            enemy.draw()
        for bullet in bullets:
            bullet.draw()
        for bomb in bombs:
            bomb.draw()
        screen.draw.text("score:{}".format(score),topleft=(20,30),color="yellow",fontsize=30)
    else:
        screen.draw.text("GAME OVER\n final score:{}".format(score),center=(400,350),color="red",fontsize=80)
        bombs.clear()
        enemies.clear()
        bullets.clear()
        
clock.schedule(countdown,1)
pgzrun.go()

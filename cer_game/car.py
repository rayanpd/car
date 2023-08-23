import pgzrun

WIDTH = 700
HEIGHT =  700
TITLE = "car_game"

intersection = Actor("intersection" , (350,350))
police = Actor("police" , (600,325))
thief = Actor("thief" , (350,600))
gameOver = Actor("game_over" , (350,350))

speed_police = 5
speed_thief = 0
game_over = False
score = 0

def update():
    global speed_police , speed_thief , game_over , score
    police.x -= speed_police
    if police.x <= -50:
        police.x = 750

    thief.y -= speed_thief
    if thief.y <= -50:
        score += 1
        thief.y = 750

    print(speed_thief)

    if thief.colliderect(police):
        game_over = True
        speed_police = 0
        speed_thief = 0
        print("gameOver")


def draw():

    screen.fill("gray")
    intersection.draw()
    police.draw()
    thief.draw()
    screen.draw.text(f"score : {score}" , color = "black" , topleft = (50,50) , fontsize = 25)

    if game_over == True:
        screen.fill("red")

    if game_over == True:
        gameOver.draw()
        screen.draw.text(f"{score}" , color = "black" , topleft = (350,500) , fontsize = 100)


def on_mouse_down(pos,button):
    global speed_thief
    if game_over == False:
        if button == mouse.LEFT and thief.collidepoint(pos):
            speed_thief += 1
        elif button == mouse.RIGHT and thief.collidepoint(pos):
            if speed_thief > 0:
                speed_thief -= 1


pgzrun.go()
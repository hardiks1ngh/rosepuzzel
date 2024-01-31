import random
from pygame import *
import time

init()
base_font = font.Font(None, 32)

screen = display.set_mode((715, 600))
display.set_caption("Petals around the roses")

dice6 = image.load("/Users/hardiksingh/Documents/Screenshot 2024-01-24 at 20.53.04.png")
dice6 = transform.scale(dice6, (100, 100))
dice5 = image.load("/Users/hardiksingh/Documents/Screenshot 2024-01-24 at 20.52.58.png")
dice5 = transform.scale(dice5, (100, 100))
dice4 = image.load("/Users/hardiksingh/Documents/Screenshot 2024-01-24 at 20.52.50.png")
dice4 = transform.scale(dice4, (100, 100))
dice3 = image.load("/Users/hardiksingh/Documents/Screenshot 2024-01-24 at 20.52.40.png")
dice3 = transform.scale(dice3, (100, 100))
dice2 = image.load("/Users/hardiksingh/Documents/Screenshot 2024-01-24 at 20.52.34.png")
dice2 = transform.scale(dice2, (100, 100))
dice1 = image.load("/Users/hardiksingh/Documents/Screenshot 2024-01-24 at 20.52.21.png")
dice1 = transform.scale(dice1, (100, 100))

dice_images = {
    1: dice1,
    2: dice2,
    3: dice3,
    4: dice4,
    5: dice5,
    6: dice6
}

def randomiseDiceImages(dice_images):
    dice_items = list(dice_images.items())
    random.shuffle(dice_items)
    shuffled_dice_images = dict(dice_items)
    return shuffled_dice_images


x, y = 0, 0

class petalsGame:
    def __init__(self, currentStreak, dice, correctTotal):
        self.currentStreak: int = currentStreak
        self.dice = []
        self.correctTotal = correctTotal
        self.reset()

    def new(self, currentStreak):
        currentStreak = 0
    
    def diceArray(self):
        dice_items = list(self.dice_images.items())
        random.shuffle(dice_items)
        self.dice_images = dict(dice_items)
        return self.dice_images

    def randomiseDiceArr(self, diceArrToUse=[]):
        diceArrToUse = list(self.dice_images.keys())
        random.shuffle(diceArrToUse)
        print(diceArrToUse)
        for element in diceArrToUse:
            if element == 3:
                self.correctTotal = self.correctTotal + 2
            if element == 5:
                self.correctTotal = self.correctTotal + 4
        return diceArrToUse, self.dice_images, self.correctTotal

    def reset(self):
        self.dice_images = randomiseDiceImages(dice_images)
        self.correctTotal = 0
        self.dice_values, self.dice_images, self.correctTotal = self.randomiseDiceArr()

    def checkAnswer(self, user_text):
        user_answer = int(user_text)
        if user_answer == self.correctTotal:
            self.currentStreak = self.currentStreak + 1
            print(f"correct answer, current streak is: {self.currentStreak}")
            return True
        else:
            print("incorrect")
            self.currentStreak = 0
            return False

input_box = Rect(275, 300, 160, 32)
user_text = ''
color_active = Color('lightskyblue3')

color_passive = Color('chartreuse4')
color = color_passive

#clock = time.Clock()

def drawDiceImage(arr):
    x = 12
    y = 50
    for key, image in arr.items():
        screen.blit(image, (x, y))
        x += 117.9
    display.update()

active = False
endGame = False
game = petalsGame(currentStreak=0, dice=[], correctTotal=0)
game.reset()

while not endGame:
    screen.fill((0, 153, 102))

    for e in event.get():
        if e.type == QUIT:
            endGame = True
        if e.type == MOUSEBUTTONDOWN:
            if input_box.collidepoint(e.pos):
                active = True
            else:
                active = False
        if e.type == KEYDOWN:
            if e.key == K_BACKSPACE:
                user_text = user_text[:-1]
            elif e.key == K_RETURN:
                if user_text:
                    user_answer = int(user_text)
                    if not game.checkAnswer(user_text):
                        exit()
                    else:
                        game.reset()
            elif e.unicode:
                user_text += e.unicode

    draw.rect(screen, (255, 0, 0), input_box)

    if active:
        color = color_active
    else:
        color = color_passive

    draw.rect(screen, color, input_box)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

    input_box.w = max(100, text_surface.get_width() + 10)
    display.flip()

    drawDiceImage(game.dice_images)

    display.update()
    #clock.tick(15)

from tkinter import *
import requests
import json
import textwrap
import pygame
import random


guessed = []
limbs = 0
word = ''
buttons = []
hangmanPics = [pygame.image.load('hangman0.png'), pygame.image.load('hangman1.png'),
                       pygame.image.load('hangman2.png'),
                       pygame.image.load('hangman3.png'), pygame.image.load('hangman4.png'),
                       pygame.image.load('hangman5.png'),
                       pygame.image.load('hangman6.png')]



class login(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x700")
        self.resizable(1, 1)
        self.iconbitmap('c:/Users/hello.ico')

    def label(self):
        self.backGroundImage = PhotoImage(file="DD.png")
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)
        self.canvas=Canvas(self, width=500, height=600)
        self.canvas.place(x=100, y=60)

        self.title=Label(self, text="MY PYTHON PROGRAMS ARE AS FOLLOWS:", font="Bold 25")
        self.title.place(x=00, y=0)

        '''self.userName = Label(self, text="UserName", font="8")
        self.userName.place(x=200, y=150)

        self.password = Label(self, text="Password", font="8")
        self.password.place(x=200, y=200)'''

    def Entry(self):
       '''  self.userName = Entry(self, borderwidth=0, highlightthickness=0, width=22)
        self.userName.place(x=320, y=155)

        self.password = Entry(self, borderwidth=0, show="+", highlightthickness=0)
        self.password.place(x=320, y=205, width=175) '''

    def Button(self):
        self.loginButtonImage=PhotoImage(file="sg.png")
        self.loginButton=Button(self, command=self.Login, border=5, text="Snake Game", width=15, relief=GROOVE, borderwidth=5)
        self.loginButton.place(x=250, y=100)

        #self.hangmanbtnimage = PhotoImage()
        self.hangmanbtn = Button(self, command=self.hangman, border=5, text="Hangman", width=15, relief=GROOVE, borderwidth=5)
        self.hangmanbtn.place(x=250, y=150)

        self.turtle = Button(self, command=self.turtle, border=5, text="Turtle Programs", width=15, relief=GROOVE, borderwidth=5)
        self.turtle.place(x=250, y=200)
    def Login(self):
        import turtle

        import time

        import random

        delay = 0.1

        score = 0

        high_score = 0

        wn = turtle.Screen()

        wn.title("Snake Game by Shashwat Mishra")

        wn.bgcolor("light blue")

        wn.setup(width=600, height=600)

        wn.tracer(0)

        head = turtle.Turtle()

        head.speed(0.0)

        head.shape("turtle")

        head.seth(90)

        head.color("dark green")

        head.penup()

        head.goto(0, 0)

        head.direction = "stop"

        # Snake food

        food = turtle.Turtle()

        food.speed(0)

        food.shape("circle")

        food.color("red")

        food.penup()

        food.goto(0, 100)

        segments = []

        # Pen

        pen = turtle.Turtle()

        pen.speed(0)

        pen.shape("square")

        pen.color("white")

        pen.penup()

        pen.hideturtle()

        pen.goto(0, 260)

        pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

        # Functions

        def go_up():
            if head.direction != "down":
                head.direction = "up"

        def go_down():
            if head.direction != "up":
                head.direction = "down"

        def go_left():
            if head.direction != "right":
                head.direction = "left"

        def go_right():
            if head.direction != "left":
                head.direction = "right"

        def move():
            if head.direction == "up":
                y = head.ycor()

                head.sety(y + 20)

            if head.direction == "down":
                y = head.ycor()

                head.sety(y - 20)

            if head.direction == "left":
                x = head.xcor()

                head.setx(x - 20)

            if head.direction == "right":
                x = head.xcor()

                head.setx(x + 20)

        # Keyboard bindings

        wn.listen()

        wn.onkeypress(go_up, "w")

        wn.onkeypress(go_down, "s")

        wn.onkeypress(go_left, "a")

        wn.onkeypress(go_right, "d")

        # Main game loop

        while True:

            wn.update()

            # Check for a collision with the border

            if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:

                time.sleep(0.1)

                head.goto(0, 0)

                head.direction = "stop"

                # Hide the segments

                for segment in segments:
                    segment.goto(1000, 1000)

                # Clear the segments list

                segments.clear()

                # Reset the score

                score = 0

                # Reset the delay

                delay = 0.1

                pen.clear()

                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                          font=("Courier", 24, "normal"))

                # Check for a collision with the food

            if head.distance(food) < 20:

                # Move the food to a random spot

                x = random.randint(-290, 290)

                y = random.randint(-290, 290)

                food.goto(x, y)

                # Add a segment

                new_segment = turtle.Turtle()

                new_segment.speed(0)

                new_segment.shape("square")

                new_segment.color("green")

                new_segment.penup()

                segments.append(new_segment)

                # Shorten the delay

                delay -= 0.001

                # Increase the score

                score += 10

                if score > high_score:
                    high_score = score

                pen.clear()

                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                          font=("Courier", 24, "normal"))

                # Move the end segments first in reverse order

            for index in range(len(segments) - 1, 0, -1):
                x = segments[index - 1].xcor()

                y = segments[index - 1].ycor()

                segments[index].goto(x, y)

            # Move segment 0 to where the head is

            if len(segments) > 0:
                x = head.xcor()

                y = head.ycor()

                segments[0].goto(x, y)

            move()

            # Check for head collision with the body segments

            for segment in segments:

                if segment.distance(head) < 20:

                    time.sleep(1)

                    head.goto(0, 0)

                    head.direction = "stop"

                    # Hide the segments

                    for segment in segments:
                        segment.goto(1000, 1000)

                    # Clear the segments list

                    segments.clear()

                    # Reset the score

                    score = 0

                    # Reset the delay

                    delay = 0.1

                    # Update the score display

                    pen.clear()

                    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                              font=("Courier", 24, "normal"))

            time.sleep(delay)

        wn.mainloop()

    def hangman(self):

        pygame.init()
        winHeight = 480
        winWidth = 700
        win = pygame.display.set_mode((winWidth, winHeight))

        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        LIGHT_BLUE = (102, 255, 255)

        btn_font = pygame.font.SysFont("arial", 20)
        guess_font = pygame.font.SysFont("monospace", 24)
        lost_font = pygame.font.SysFont('arial', 45)
        global word
        global buttons
        global guessed
        global hangmanPics

        global limbs

        def redraw_game_window():
            global guessed
            global hangmanPics
            global limbs
            win.fill(GREEN)
            # Buttons
            for i in range(len(buttons)):
                if buttons[i][4]:
                    pygame.draw.circle(win, BLACK, (buttons[i][1], buttons[i][2]), buttons[i][3])
                    pygame.draw.circle(win, buttons[i][0], (buttons[i][1], buttons[i][2]), buttons[i][3] - 2
                                       )
                    label = btn_font.render(chr(buttons[i][5]), 1, BLACK)
                    win.blit(label, (buttons[i][1] - (label.get_width() / 2), buttons[i][2] - (label.get_height() / 2)))

            spaced = spacedOut(word, guessed)
            label1 = guess_font.render(spaced, 1, BLACK)
            rect = label1.get_rect()
            length = rect[2]

            win.blit(label1, (winWidth / 2 - length / 2, 400))

            pic = hangmanPics[limbs]
            win.blit(pic, (winWidth / 2 - pic.get_width() / 2 + 20, 150))
            pygame.display.update()

        def randomWord():
            file = open('words.txt')
            f = file.readlines()
            i = random.randrange(0, len(f) - 1)

            return f[i][:-1]

        def hang(guess):
            global word
            if guess.lower() not in word.lower():
                return True
            else:
                return False

        def spacedOut(word, guessed=[]):
            spacedWord = ''
            guessedLetters = guessed
            for x in range(len(word)):
                if word[x] != ' ':
                    spacedWord += '_ '
                    for i in range(len(guessedLetters)):
                        if word[x].upper() == guessedLetters[i]:
                            spacedWord = spacedWord[:-2]
                            spacedWord += word[x].upper() + ' '
                elif word[x] == ' ':
                    spacedWord += ' '
            return spacedWord

        def buttonHit(x, y):
            for i in range(len(buttons)):
                if x < buttons[i][1] + 20 and x > buttons[i][1] - 20:
                    if y < buttons[i][2] + 20 and y > buttons[i][2] - 20:
                        return buttons[i][5]
            return None

        def end(winner=False):
            global limbs
            lostTxt = 'You Lost, press any key to play again...'
            winTxt = 'WINNER!, press any key to play again...'
            redraw_game_window()
            pygame.time.delay(1000)
            win.fill(GREEN)

            if winner == True:
                label = lost_font.render(winTxt, 1, BLACK)
            else:
                label = lost_font.render(lostTxt, 1, BLACK)

            wordTxt = lost_font.render(word.upper(), 1, BLACK)
            wordWas = lost_font.render('The player was: ', 1, BLACK)

            win.blit(wordTxt, (winWidth / 2 - wordTxt.get_width() / 2, 295))
            win.blit(wordWas, (winWidth / 2 - wordWas.get_width() / 2, 245))
            win.blit(label, (winWidth / 2 - label.get_width() / 2, 140))
            pygame.display.update()
            again = True
            while again:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        again = False
            reset()

        def reset():
            global limbs
            global guessed
            global buttons
            global word
            for i in range(len(buttons)):
                buttons[i][4] = True

            limbs = 0
            guessed = []
            word = randomWord()

        # MAINLINE

        # Setup buttons
        increase = round(winWidth / 13)
        for i in range(26):
            if i < 13:
                y = 40
                x = 25 + (increase * i)
            else:
                x = 25 + (increase * (i - 13))
                y = 85
            buttons.append([LIGHT_BLUE, x, y, 20, True, 65 + i])
            # buttons.append([color, x_pos, y_pos, radius, visible, char])

        word = randomWord()
        inPlay = True

        while inPlay:
            redraw_game_window()
            pygame.time.delay(10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    inPlay = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        inPlay = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickPos = pygame.mouse.get_pos()
                    letter = buttonHit(clickPos[0], clickPos[1])
                    if letter != None:
                        guessed.append(chr(letter))
                        buttons[letter - 65][4] = False
                        if hang(chr(letter)):
                            if limbs != 5:
                                limbs += 1
                            else:
                                end()
                        else:
                            print(spacedOut(word, guessed))
                            if spacedOut(word, guessed).count('_') == 0:
                                end(True)

        pygame.quit()
        # always quit pygame when done!

    def batman(self):
        import turtle

        bat = turtle.Turtle()

        bat.pensize(3)

        wn = turtle.Screen()
        wn.bgcolor("black")
        wn.title("Batman logo")

        bat.color("yellow", "black")
        bat.speed(6)

        bat.begin_fill()

        # turn 1
        bat.left(90)
        bat.circle(50, 85)
        bat.circle(15, 110)
        bat.right(180)

        # turn 2
        bat.circle(30, 150)
        bat.right(5)
        bat.forward(10)

        # turn 3
        bat.right(90)
        bat.circle(-70, 140)
        bat.forward(40)
        bat.right(110)

        # turn 4
        bat.circle(100, 30)
        bat.circle(30, 100)
        bat.left(50)
        bat.forward(50)
        bat.right(145)

        # turn 5
        bat.forward(30)
        bat.left(55)
        bat.forward(10)

        # reverse

        # turn 5
        bat.forward(10)
        bat.left(55)
        bat.forward(30)

        # turn 4
        bat.right(145)
        bat.forward(50)
        bat.left(50)
        bat.circle(30, 100)
        bat.circle(100, 30)

        # turn 3
        bat.right(90)
        bat.right(20)
        bat.forward(40)
        bat.circle(-70, 140)

        # turn 2
        bat.right(90)
        bat.forward(10)
        bat.right(5)
        bat.circle(30, 150)

        # turn 1
        bat.left(180)
        bat.circle(15, 110)
        bat.circle(50, 85)

        # end color filling
        bat.end_fill()
        wn.bgcolor("yellow")

        bat.hideturtle()
        wn.mainloop()


    def turtle(self):
        root = Tk()

        # root window title and dimension
        root.title("Turtle Programs")
        root.geometry("700x700")
        root.configure(bg="lightgreen")

        def batman():
            import turtle

            bat = turtle.Turtle()

            bat.pensize(3)

            wn = turtle.Screen()
            wn.bgcolor("black")
            wn.title("Batman logo")

            bat.color("yellow", "black")
            bat.speed(6)

            bat.begin_fill()

            # turn 1
            bat.left(90)
            bat.circle(50, 85)
            bat.circle(15, 110)
            bat.right(180)

            # turn 2
            bat.circle(30, 150)
            bat.right(5)
            bat.forward(10)

            # turn 3
            bat.right(90)
            bat.circle(-70, 140)
            bat.forward(40)
            bat.right(110)

            # turn 4
            bat.circle(100, 30)
            bat.circle(30, 100)
            bat.left(50)
            bat.forward(50)
            bat.right(145)

            # turn 5
            bat.forward(30)
            bat.left(55)
            bat.forward(10)

            # reverse

            # turn 5
            bat.forward(10)
            bat.left(55)
            bat.forward(30)

            # turn 4
            bat.right(145)
            bat.forward(50)
            bat.left(50)
            bat.circle(30, 100)
            bat.circle(100, 30)

            # turn 3
            bat.right(90)
            bat.right(20)
            bat.forward(40)
            bat.circle(-70, 140)

            # turn 2
            bat.right(90)
            bat.forward(10)
            bat.right(5)
            bat.circle(30, 150)

            # turn 1
            bat.left(180)
            bat.circle(15, 110)
            bat.circle(50, 85)

            # end color filling
            bat.end_fill()
            wn.bgcolor("yellow")

            bat.hideturtle()
            wn.mainloop()

        batman1 = Button(root, command=self.batman, text="Batman", width=15, border=5)
        batman1.place(x=100, y=100)
        def netflix():
            import turtle

            bat = turtle.Turtle()
            bat.hideturtle()
            bat.penup()
            bat.goto(-250, -285)
            bat.pendown()
            bat.pensize(3)
            bat.speed(0)

            wn = turtle.Screen()
            wn.bgcolor("dark blue")
            wn.title("NETFLIX And CHill ")

            bat.color("red", "black")

            bat.begin_fill()

            # background
            bat.forward(500)
            bat.circle(40, 90)
            bat.forward(500)
            bat.circle(40, 90)
            bat.fd(500)
            bat.circle(40, 90)
            bat.fd(500)
            bat.circle(40, 90)

            bat.end_fill()

            # logo
            bat.penup()
            bat.goto(-150, - 200)
            bat.pendown()

            # left side
            bat.color("dark red", "red")
            bat.begin_fill()
            bat.forward(100)
            bat.left(90)
            bat.forward(400)
            bat.left(90)
            bat.forward(100)
            bat.left(90)
            bat.forward(400)
            bat.left(90)
            bat.forward(100)
            bat.left(90)
            bat.forward(400)
            bat.right(150)
            bat.end_fill()

            # center

            bat.color("dark red", "red")
            bat.begin_fill()
            bat.forward(463)
            bat.left(60)
            bat.right(180)
            bat.fd(100)
            bat.right(60)
            bat.forward(463)
            bat.right(120)
            bat.fd(100)
            bat.right(60)
            bat.forward(464)
            bat.left(150)
            bat.end_fill()

            # Right

            bat.color("dark red", "red")
            bat.begin_fill()
            bat.forward(400)
            bat.left(90)
            bat.forward(100)
            bat.left(90)
            bat.forward(400)
            bat.left(90)
            bat.forward(100)
            bat.left(90)
            bat.forward(400)
            bat.end_fill()

            wn.mainloop()

        netflix1 = Button(root, command=netflix, text="Netflix", width=15, border=5)
        netflix1.place(x=100, y=150)

        def youtube():
            import turtle

            sc = turtle.Screen()
            sc.title("YouTube")
            sc.bgcolor("white")

            t = turtle.Turtle()
            t.penup()
            t.goto(-200, -150)
            t.pensize(10)
            t.color("red")
            t.speed(0)

            # back
            t.begin_fill()
            t.pendown()
            t.fd(400)
            t.circle(60, 90)
            t.fd(200)
            t.circle(60, 90)
            t.fd(400)
            t.circle(60, 90)
            t.fd(200)
            t.circle(60, 90)
            t.end_fill()

            # Front

            t.penup()
            t.color("white")

            t.goto(-40, -70)
            t.pendown()
            t.begin_fill()
            t.left(30)
            t.fd(150)
            t.left(120)
            t.fd(150)
            t.left(120)
            t.fd(150)
            t.left(120)
            t.end_fill()

            t.hideturtle()
            sc.mainloop()
        yt = Button(root, width=15, text="Youtube", border=5, command=youtube)
        yt.place(x=100, y=200)

        def covid():
            import turtle

            wn = turtle.Screen()
            wn.bgcolor("black")

            covid = turtle.Turtle()
            covid.pensize(2)
            covid.speed(0)
            covid.penup()
            covid.goto(0, 200)
            covid.pendown()

            for b in range(200):
                if b <= 150:
                    covid.color("red")
                    covid.right(b)
                    covid.forward(b * 3)
                else:
                    covid.color("red")
                    covid.right(b)
                    covid.forward(b * 3)
            covid.hideturtle()
            wn.mainloop()
            c19.configure(wn, command=self.covid, width=15, border=5, text="Corona")
        c19 = Button(root, command=covid, width=15, border=5, text="Corona")
        c19.place(x=100, y=250)
        root.mainloop()

'''  except UnboundLocalError:
            print("Couldnt find anything")
        except:
            print("Invalid Url")'''



'''print(x[0]['word'])
print(type(x))
b = json.dumps(x, indent=2)
print(type(b))'''



if __name__ == "__main__":
    Login = login()
    Login.label()
    Login.Entry()
    Login.Button()
    Login.mainloop()


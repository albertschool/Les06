from playsound import playsound
import time
import turtle
wn = turtle.Screen()
size = 250
h = 0.8
m = 0.52
l = 0.24
delay = 0.3
wn.setup(2*size,2*size)
wn.addshape("images/bg4.gif")
wn.addshape("images/dishl.gif")
wn.addshape("images/dishr.gif")
wn.addshape("images/plate.gif")
wn.addshape("images/sputnik.gif")
wn.addshape("images/blackdot.gif")
wn.bgpic("images/bg4.gif")
wn.listen()

# Init
playl = turtle.Turtle()
playl.pu()
playl.hideturtle()
playl.shape("images/dishl.gif")
playr = turtle.Turtle()
playr.pu()
playr.hideturtle()
playr.shape("images/dishr.gif")
posl = ([-h*size,-0.9*size],[-m*size,-0.9*size],[-l*size,-0.9*size])
posr = ([l*size,-0.9*size],[m*size,-0.9*size],[h*size,-0.9*size])
playPos = 1

high = turtle.Turtle()
high.pu()
high.hideturtle()
high.shape("images/sputnik.gif")
poshigh = ([-h*size,-0.6*size],[-150,2],[-100,110],[-50,177],[0,h*size],[50,177],[100,110],[150,2],[h*size,-0.6*size])
med = turtle.Turtle()
med.pu()
med.hideturtle()
med.shape("images/plate.gif")
posmed = ([-m*size,-0.6*size],[-90,-8],[-26,118],[26,118],[90,8],[m*size,-0.6*size])

livesT = turtle.Turtle()
livesT.pu()
livesT.hideturtle()
scoreT = turtle.Turtle()
scoreT.pu()
scoreT.hideturtle()
mesT = turtle.Turtle()
mesT.pu()
mesT.hideturtle()

# Functions
def moveleft():
    global posl, posr, playPos
    if (playPos>0):
        playPos-=1
        playl.goto(posl[playPos])
        playr.goto(posr[playPos])

def moveright():
    global posl, posr, playPos
    if (playPos<2):
        playPos+=1
        playl.goto(posl[playPos])
        playr.goto(posr[playPos])

def message(message):
    mesT.clear()
    mesT.pu()
    mesT.hideturtle()
    mesT.shape("images/blackdot.gif")
    mesT.color("red")
    mesT.goto(-150, 0)
    mesT.showturtle()
    mesT.write(str(message), font=("Ariel", 24))

def setscore(scr):
    scoreT.clear()
    scoreT.pu()
    scoreT.hideturtle()
    scoreT.shape("images/blackdot.gif")
    scoreT.color("red")
    scoreT.goto(-230, 220)
    scoreT.showturtle()
    scoreT.write("Score: " + str(scr), font=("Ariel", 16))

def setlives(live):
    livesT.clear()
    livesT.pu()
    livesT.hideturtle()
    livesT.shape("images/blackdot.gif")
    livesT.color("red")
    livesT.goto(150, 220)
    livesT.showturtle()
    livesT.write(str(live) + " Lives", font=("Ariel", 16))

def stage():
    global delay, score
    t = (score//100)+((score%100)//70)
    if ((score%100) > 40):
        s = 1
    else:
        s = 0
    stageDelay = delay*(1-(0.05*(t+s)))
    return stageDelay

def disqualification():
    global disqual, lives, liveStart, score, gameActive
    disqual -= 1
    lives = liveStart + disqual + (score // 100)
    setlives(lives)
    if (lives == 0):
        gameActive = False
        message("Game Over\n Press SPACE to restart")
    playsound("sounds/doorbell.wav")

def chkhigh():
    global playPos, highPos, score
    if ((playPos==0 and highPos==0) or (playPos==2 and highPos==(len(poshigh)-1))):
        playsound("sounds/clickshort.wav", False)
        score += 1
        setscore(score)
    else:
        disqualification()

def chkmed():
    global playPos, score
    if (playPos == 1):
        playsound("sounds/clickshort.wav", False)
        score += 1
        setscore(score)
    else:
        disqualification()

def gameon():
    global gameActive, delay, playPos, score
    global highPos, highDir, medPos, medDir
    while(gameActive):
        if (highPos == (len(poshigh) - 1)):
            chkhigh()
            highDir = -1
        elif (highPos < 1):
            chkhigh()
            highDir = 1
        highPos += highDir
        high.goto(poshigh[highPos])
        if (0<highPos and highPos<(len(poshigh) - 1)):
            playsound("sounds/beep.wav", False)
        time.sleep(stage())
        if (medPos == (len(posmed) - 1)):
            chkmed()
            medDir = -1
        elif (medPos < 1):
            chkmed()
            medDir = 1
        medPos += medDir
        med.goto(posmed[medPos])
        if (0<medPos and medPos<(len(posmed) - 1)):
            playsound("sounds/beep.wav", False)
        time.sleep(stage())

# Reset game
def resetgame():
    global posl, playPos, posr
    global highPos, highDir, poshigh
    global medPos, medDir, posmed
    global gameActive, disqual, liveStart, lives, score
    playl.turtlesize(1)
    playl.goto(posl[playPos])
    playl.showturtle()
    playr.turtlesize(1)
    playr.goto(posr[playPos])
    playr.showturtle()
    high.turtlesize(1)
    highPos = 1
    highDir = 1
    high.goto(poshigh[highPos])
    high.showturtle()
    med.turtlesize(1)
    medPos = 2
    medDir = 1
    med.goto(posmed[medPos])
    med.showturtle()
    gameActive = True
    disqual = 0
    liveStart = 3
    lives = liveStart
    setlives(lives)
    score = 0
    setscore(score)
    message("Start !")
    time.sleep(2)
    message("")
    gameon()

def restart():
    global gameActive
    gameActive = False
    resetgame()

# Main
wn.onkey(moveleft,"Left")
wn.onkey(moveright,"Right")
wn.onkey(restart,"space")
resetgame()

turtle.mainloop()
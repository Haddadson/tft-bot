#! python3
import pyautogui as pg
import sys
import PIL.ImageGrab
import win32gui
from time import sleep
import random

# Search game button
xSearchGame = 1175
ySearchGame = 840

# Accept game button
xAcceptGame = 1273
yAcceptGame = 712

# Coordinates of the first champion on shop
xChampions = 929
yChampions = 936

# Distance between champions on shop
distanceChampions = 175

# Buy level button
xbuyLevel = 730
ybuyLevel = 913

# Random position in board
xMoveLittleLegend1 = 1055
yMoveLittleLegend1 = 373

# Other random position in board
xMoveLittleLegend2 = 1401
yMoveLittleLegend2 = 308

# Central position in board
xMoveLittleLegend3 = 1280
yMoveLittleLegend3 = 464

# Quit game button (used while watching after death)
xclickQuit = 1142
yclickQuit = 538

# Any pixel in desktop outside the client
xPixelDesktop = 110
yPixelDesktop = 32

# Accept rewards from missions button
xAcceptMission = 1175
yAcceptMission = 815


def clickSearchGame():
    pg.moveTo(xSearchGame, ySearchGame, 1)
    pg.click()
#


def clickPlayAgain():
    clickSearchGame()
#


def clickAcceptGame():
    pg.moveTo(xAcceptGame, yAcceptGame)
    pg.click()
#


def buyChampion(quantidade=0):
    j = 0
    xInicial = xChampions

    while (j < quantidade):
        pg.moveTo(xInicial + (j*distanceChampions), yChampions, 0.5)
        pg.mouseDown()
        sleep(0.2)
        pg.mouseUp()

        j = j + 1
    #
#


def buyLevel(quantidadeCliques=0):
    j = 0
    pg.moveTo(xbuyLevel, ybuyLevel, 0.5)

    while (j < quantidadeCliques):
        j = j + 1

        pg.mouseDown()
        sleep(0.2)
        pg.mouseUp()
    #
#


def moveLittleLegend(caminho=0):
    # Random position 1
    if (caminho == 0):
        pg.moveTo(xMoveLittleLegend1, yMoveLittleLegend1, 0.5)
        pg.mouseDown(button='right')
        sleep(0.5)
        pg.mouseUp(button='right')
        return
    #

    # Random position 2
    if (caminho == 1):
        pg.moveTo(xMoveLittleLegend2, yMoveLittleLegend2, 0.5)
        pg.mouseDown(button='right')
        sleep(0.6)
        pg.mouseUp(button='right')
        return
    #

    # Central position
    if (caminho == 2):
        pg.moveTo(xMoveLittleLegend3, yMoveLittleLegend3, 0.5)
        pg.mouseDown(button='right')
        sleep(0.3)
        pg.mouseUp(button='right')
        return
    #
#


def clickQuitGame():
    pg.moveTo(xclickQuit, yclickQuit)
    pg.mouseDown()
    sleep(0.2)
    pg.mouseUp()
#


def clickAcceptMission(nVezes=1):
    j = 0

    while (j < nVezes):
        pg.moveTo(xAcceptMission, yAcceptMission)
        pg.click()
        sleep(10)
        j = j + 1
    #
#


print("Starting")

# Save instance of the client to bring it to the foreground
leagueClient = win32gui.FindWindow(0, "League of Legends")

pixelDesktop = PIL.ImageGrab.grab().load()[xPixelDesktop, yPixelDesktop]
print(pixelDesktop)
sleep(5)

try:
    while True:
        sleep(10)

        # Bring the client do the foreground after the game ends
        win32gui.SetForegroundWindow(leagueClient)
        win32gui.BringWindowToTop(leagueClient)

        # Enter in the queue
        print("Queuing...")
        clickSearchGame()

        # While not find a game, keeps clicking to accept game
        while (PIL.ImageGrab.grab().load()[xPixelDesktop, yPixelDesktop] == pixelDesktop):
            clickAcceptGame()
            sleep(1)
        #

        print("Match found!")

        # Wait 10s before the game starts
        sleep(10)

        # Save a pixel from the load screen
        pixelTelaLoad = PIL.ImageGrab.grab().load()[
            xPixelDesktop, yPixelDesktop]

        # Check if the game started comparing the pixel of loading screen
        while (PIL.ImageGrab.grab().load()[xPixelDesktop, yPixelDesktop] == pixelTelaLoad):
            pass
        #

        # Bring the game to the foreground after the game starts
        leagueGame = win32gui.FindWindow(0, "League of Legends (TM) Client")
        win32gui.SetForegroundWindow(leagueGame)
        win32gui.BringWindowToTop(leagueGame)

        print("Game started, waiting 15 minutes...")

        # Starts a timer of 18 minutes and do some actions
        x = 1080
        while (x > 0):
            x = x - 1
            sleep(1)

            if (x == 1065):
                moveLittleLegend(2)
            #

            if (x == 1017):
                buyChampion(2)
            #

            if (x == 1000):
                moveLittleLegend(2)
                buyChampion(2)
                moveLittleLegend(0)
                moveLittleLegend(1)
            #

            if (x == 899):
                moveLittleLegend(1)
                buyChampion(4)
                buyLevel(3)
            #

            if (x == 830):
                buyChampion(2)
                moveLittleLegend(0)
                buyLevel(1)
            #

            if (x == 775):
                buyChampion(1)
                buyLevel(1)
            #

            if (x == 709):
                moveLittleLegend(1)
                buyChampion(1)
                buyLevel(4)
            #

            if (x == 660):
                buyChampion(1)
                moveLittleLegend(2)
                buyLevel(1)
            #

            if (x == 590):
                moveLittleLegend(1)
                buyChampion(1)
                moveLittleLegend(0)
                buyLevel(6)
            #

            if (x == 320):
                buyChampion(3)
                buyLevel(3)
            #

            if (x == 260):
                buyLevel(1)
                buyChampion(2)
                moveLittleLegend(1)
            #

            if (x == 60):
                buyLevel(20)
                moveLittleLegend(0)
                moveLittleLegend(1)
            #

            if (x == 30):
                print("Last iteration")
                buyLevel(10)
                moveLittleLegend(0)
                buyChampion(5)
            #
        #

        timer = 0

        print("Waiting life hit 0 points...")

        # After 18 minutes, waits to die and keeps clicking to quit game until the game closes
        print(pixelDesktop)
        print(PIL.ImageGrab.grab().load()[xPixelDesktop, yPixelDesktop])
        while (PIL.ImageGrab.grab().load()[xPixelDesktop, yPixelDesktop] != pixelDesktop):
            clickQuitGame()
            sleep(20)

            # Each minute do some actions
            if (timer % 60 == 0):
                buyLevel(random.randint(1, 10))
                buyChampion(random.randint(1, 5))
                move = random.randint(1, 3)
                if (move == 2):
                    moveLittleLegend(random.randint(0, 2))

            #

            timer = timer + 20
            print(timer)
        #

        print("Go next..")

        # Wait some seconds after the game closes
        sleep(10)
        win32gui.SetForegroundWindow(leagueClient)
        win32gui.BringWindowToTop(leagueClient)
        sleep(5)

        # Click in the button to accept rewards from the missions
        clickAcceptMission(2)

        # Click to play again and wait some seconds
        sleep(70)
        print("Play again...")
        clickPlayAgain()
        sleep(45)
    #

except KeyboardInterrupt:
    print('\n')
#

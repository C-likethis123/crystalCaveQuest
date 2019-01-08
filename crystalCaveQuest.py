import win32api, win32con
from time import sleep, time
from PIL import ImageGrab, Image
from numpy import mean, array

#Global constants
toDashboard = (1476, 512)
clickQuest = (779, 622)
toNextScreen = (1536, 450)
finalSpell = (1449, 682)
doneButton = (1089, 578)
stun = (892, 680)
attack = (1056, 665)
multi = (1309, 674)

toBottom = (1529, 576)
toTop1 = (978, 460)
toTop2 = (1513, 314)
goAcross = (994, 278)
acrossBridge = (1528, 279)
fountain = (1057, 351)
toCrystalCave = (1063, 321)

toCrystalTree = (1091, 179)
endQuest = (1096, 685)
openScroll = (1168, 792)
potions = (1349, 509)
closeScroll = (1071, 676)
back = (664,482)
        
        
def leftClick():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)


def leftDown():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
        sleep(0.1)
        print("Left down")

def leftUp():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)
        sleep(0.1)
        print("Left release")

def clickHere(cord):
        win32api.SetCursorPos((cord[0], cord[1]))
        sleep(2)
        leftClick()
        sleep(2)
     
def get_cords():
        x,y = win32api.GetCursorPos()
        print(x,y)


def monsterHasDied():
        sleep(4)
        box = (1023,554, 1156, 586)
        healthBar = ImageGrab.grab(box)
        healthBar = array(healthBar)
        healthBar[:, :, 1] *= 0
        healthBar[:, :, 2] *= 0
        oneList = []
        for sublist in healthBar:
                for channel in sublist:
                        oneList.append(channel)



        brightness = mean(oneList)
        print(brightness)
        if (brightness > 50):
                return True
        else:
                print("the brightness is %f" % brightness)
                return False





def startGame():
        #get the coords from entering the quest.
        clickHere(toDashboard)
        clickHere(clickQuest)


def attackMonster():
        clickHere(finalSpell)
        sleep(4)
        monsterDied = monsterHasDied()
        if monsterDied == True:
                clickHere(doneButton)
        else:
                while monsterDied == False:
                        clickHere(attack)
                        print("in loop attack")
                        monsterDied = monsterHasDied()




                print("exited loop")
                monsterDied = 0
                clickHere(doneButton)




def attackTwoMonsters():
        clickHere(multi)
        sleep(4)
        monsterDied = monsterHasDied()

        if monsterDied == True:
                clickHere(doneButton)
        else:
                while monsterDied == False:
                        clickHere(attack)
                        print("in loop attack2")
                        monsterDied = monsterHasDied()
                        print(monsterDied)


        
                print("exited loop attack2")
                monsterDied = 0
                clickHere(doneButton)


        

def firstScreen():
        for monster in range(0,2):
                clickHere(toNextScreen)
                attackMonster()

                

        clickHere(toNextScreen)
        sleep(1)


def secondScreen():
        for monster in range(0,2):
                sleep(1)
                clickHere(toNextScreen)
                sleep(1)
                attackMonster()



        clickHere(toNextScreen)
        attackTwoMonsters()
        
        clickHere(toNextScreen)


def thirdScreen():
        clickHere(toBottom)
        attackMonster()

        clickHere(toBottom)

def fourthScreen():
        clickHere(toNextScreen)
        attackMonster()
        clickHere(back)


def fifthScreen():
        clickHere(toTop1)
        clickHere(toTop2)
        attackMonster()

        clickHere(toTop2)


def sixthScreen():
        for monster in range(0,5):
                clickHere(toTop2)
                attackMonster()


        clickHere(toTop2)
        

def bridge():
        clickHere(toTop2)
        sleep(3)

        for clicks in range(0,5):
                clickHere(toTop2)
                sleep(1)



        sleep(1)
        clickHere(goAcross)
        clickHere(acrossBridge)
        sleep(5)


def eight():
        clickHere(fountain)
        sleep(5)

        clickHere(toNextScreen)
        attackMonster()

        clickHere(toNextScreen)


def entranceToCave():
        clickHere(toCrystalCave)
        attackTwoMonsters()
        clickHere(toCrystalCave)


def crystalWall():
        clickHere(toCrystalCave)
        sleep(2)

        attackMonster()
        
        clickHere(toCrystalTree)


def crystalTree():
        clickHere(toCrystalTree)
        attackTwoMonsters()

        clickHere(toCrystalTree)
        sleep(3)

        attackMonster()

        clickHere(toCrystalCave)
        sleep(2)
        
        #take screenshot
        #if screenshot is the shard thing, click Ok
        #else, go about the business. 


def ending():
        clickHere(endQuest)
        clickHere(openScroll)
        clickHere(potions)
        clickHere(closeScroll)

        
def main():
       startTime = time()

       startGame()
       
       firstScreen()
       
       secondScreen()

       thirdScreen()
       
       fourthScreen()

       fifthScreen()

       sixthScreen()

       bridge()

       eight()

       entranceToCave()

       crystalWall()

       crystalTree()

       ending()
       
       timeTaken = time() - startTime
       print("This round of games took %f seconds" % timeTaken)
       
       print("ending, starting new game...")
       sleep(5)


def mainloop():
        while True:
                main()



mainloop()

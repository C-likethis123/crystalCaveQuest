import win32api, win32con
from time import sleep
from PIL import ImageGrab, Image
from numpy import mean, array

class Coord:
        #When starting game
        toDashboard = (1476, 512)
        clickQuest = (779, 622)
        toNextScreen = (1536, 450)
        finalSpell = (1449, 682)
        doneButton = (1089, 578)
        stun = (892, 680)
        attack = (1056, 665)
        double = (1170, 685)
        triple = (1210, 684)
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


def checkMonsterMissed():
        sleep(4)
        box = (1240,794, 1334, 809)
        healthBar = ImageGrab.grab(box)
        healthBar = array(healthBar)
        healthBar[:, :, 1] *= 0
        healthBar[:, :, 2] *= 0
        oneList = []
        for sublist in healthBar:
                for channel in sublist:
                        oneList.append(channel)





        if (mean(oneList) > 0):
                return True
        else:
                return False





def startGame():
        #get the coords from entering the quest.
        clickHere(Coord.toDashboard)
        clickHere(Coord.clickQuest)


def attackMonster():
        clickHere(Coord.finalSpell)
        sleep(4)
        monsterDied = not checkMonsterMissed()
        if monsterDied == True:
                clickHere(Coord.doneButton)
        else:
                while monsterDied == False:
                        clickHere(Coord.attack)
                        print("in loop attack")
                        monsterDied = checkMonsterMissed()



                print("exited loop")
                monsterDied = 0
                clickHere(Coord.doneButton)




def attackTwoMonsters():
        clickHere(Coord.multi)
        sleep(4)
        monsterDied = not checkMonsterMissed()

        if monsterDied == True:
                clickHere(Coord.doneButton)
        else:
                while monsterDied == False:
                        clickHere(Coord.attack)
                        print("in loop attack2")
                        monsterDied = checkMonsterMissed()
                        print(monsterDied)

        
                print("exited loop attack2")
                monsterDied = 0
                clickHere(Coord.doneButton)


        

def firstScreen():
        for monster in range(0,2):
                clickHere(Coord.toNextScreen)
                attackMonster()

                

        clickHere(Coord.toNextScreen)
        sleep(1)


def secondScreen():
        for monster in range(0,2):
                sleep(1)
                clickHere(Coord.toNextScreen)
                sleep(1)
                attackMonster()



        clickHere(Coord.toNextScreen)
        attackTwoMonsters()
        
        clickHere(Coord.toNextScreen)


def thirdScreen():
        clickHere(Coord.toBottom)
        attackMonster()

        clickHere(Coord.toBottom)

def fourthScreen():
        clickHere(Coord.toNextScreen)
        attackMonster()
        clickHere(Coord.back)


def fifthScreen():
        clickHere(Coord.toTop1)
        clickHere(Coord.toTop2)
        attackMonster()

        clickHere(Coord.toTop2)


def sixthScreen():
        for monster in range(0,5):
                clickHere(Coord.toTop2)
                attackMonster()


        clickHere(Coord.toTop2)
        

def bridge():
        clickHere(Coord.toTop2)
        sleep(3)

        for clicks in range(0,5):
                clickHere(Coord.toTop2)
                sleep(1)



        sleep(1)
        clickHere(Coord.goAcross)
        clickHere(Coord.acrossBridge)
        sleep(5)


def eight():
        clickHere(Coord.fountain)
        sleep(5)

        clickHere(Coord.toNextScreen)
        attackMonster()

        clickHere(Coord.toNextScreen)


def entranceToCave():
        clickHere(Coord.toCrystalCave)
        attackTwoMonsters()
        clickHere(Coord.toCrystalCave)


def crystalWall():
        clickHere(Coord.toCrystalCave)
        sleep(2)
        clickHere(Coord.stun)
        sleep(2)
        clickHere(Coord.double)
        sleep(3)
        clickHere(Coord.triple)
        sleep(3)
        
        clickHere(Coord.doneButton)
        clickHere(Coord.toCrystalTree)


def crystalTree():
        clickHere(Coord.toCrystalTree)
        attackTwoMonsters()

        clickHere(Coord.toCrystalTree)
        sleep(3)
        clickHere(Coord.stun)
        sleep(3)
        
        clickHere(Coord.double)
        sleep(3)
        clickHere(Coord.triple)
        sleep(3)
        clickHere(Coord.finalSpell)

        clickHere(Coord.doneButton)
        sleep(1)
        clickHere(Coord.toCrystalCave)


def ending():
        clickHere(Coord.endQuest)
        clickHere(Coord.openScroll)
        clickHere(Coord.potions)
        clickHere(Coord.closeScroll)

        
def main():
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
       print("ending, starting new game...")
       sleep(5)


def mainloop():
        while True:
                main()



mainloop()

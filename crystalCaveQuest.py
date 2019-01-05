import win32api, win32con
import time

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

class otherData:
        first_screen = (2,0)
        second_screen = (2,1)
        third_screen = (2,0) #one at top, other at bottom
        
        
        
def leftClick():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)


def leftDown():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
        time.sleep(0.1)
        print("Left down")

def leftUp():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)
        time.sleep(0.1)
        print("Left release")

def clickHere(cord):
        win32api.SetCursorPos((cord[0], cord[1]))
        time.sleep(2)
        leftClick()
        time.sleep(2)
     
def get_cords():
        x,y = win32api.GetCursorPos()
        #x = x - x_pad
        #y = y - y_pad
        print(x,y)

def startGame():
        #get the coords from entering the quest.
        clickHere(Coord.toDashboard)
        clickHere(Coord.clickQuest)


def attackMonster():
        clickHere(Coord.finalSpell)
        clickHere(Coord.doneButton)



def attackTwoMonsters():
        clickHere(Coord.multi)
        clickHere(Coord.doneButton)


        

def firstScreen():
        for monster in range(0,2):
                clickHere(Coord.toNextScreen)
                attackMonster()

                

        clickHere(Coord.toNextScreen)


def secondScreen():
        for monster in range(0,2):
                clickHere(Coord.toNextScreen)
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
        print("clicked toTop2 once")
        time.sleep(3)

        for clicks in range(0,3):
                clickHere(Coord.toTop2)
                print("toTop2 once")
                time.sleep(1)




        clickHere(Coord.goAcross)
        print("clicked go across")
        clickHere(Coord.acrossBridge)
        print("going across the bridge")
        time.sleep(5)


def eight():
        clickHere(Coord.fountain)
        time.sleep(5)

        clickHere(Coord.toNextScreen)
        attackMonster()

        clickHere(Coord.toNextScreen)


def entranceToCave():
        clickHere(Coord.toCrystalCave)
        attackTwoMonsters()
        clickHere(Coord.toCrystalCave)


def crystalWall():
        clickHere(Coord.toCrystalCave)

        clickHere(Coord.stun)
        clickHere(Coord.double)
        time.sleep(2)
        clickHere(Coord.triple)
        time.sleep(2)
        
        clickHere(Coord.doneButton)
        clickHere(Coord.toCrystalCave)


def crystalTree():
        clickHere(Coord.toCrystalTree)
        attackTwoMonsters()

        clickHere(Coord.toCrystalTree)
        clickHere(Coord.stun)
        clickHere(Coord.double)
        clickHere(Coord.triple)
        clickHere(Coord.finalSpell)

        clickHere(Coord.doneButton)
        clickHere(Coord.toCrystalCave)


def ending():
        clickHere(Coord.endQuest)
        clickHere(Coord.openScroll)
        clickHere(Coord.potions)
        clickHere(Coord.closeScroll)

        
def main():
       startGame()
       print("in game now")
       
       firstScreen()
       print("finished first screen")
       
       secondScreen()
       print("finished second screen")
       
       thirdScreen()
       print("finished third screen")
       
       fourthScreen()
       print("finished fourth screen")

       fifthScreen()
       print("finished fifth screen")

       sixthScreen()
       print("finished sixth screen")

       bridge()
       print("finished bridge area")

       eight()
       print("finished eighth screen")

       entranceToCave()
       print("got through entrance area")

       crystalWall()
       print("got through crystal cave")

       crystalTree()
       print("got through crystal tree")

       ending()
       print("got through ending, prepared for another round")

       time.sleep(5)


while True:
        main()

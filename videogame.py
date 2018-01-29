import pygame

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("this is cool!")
pygame.init()

background = pygame.image.load('game-temp-background.jpg')
screen.blit(self.background, (0,0))

def forest():

    print "fill in later1"
    #get out of my code
    answer = raw_input("fill in later2").lower()
    if answer == "down" or answer == "s":
        print "fill in later3"
    elif answer == "up" or answer == "w":
        print "fill in later4.1"

    answer = raw_input("fill in later 5").lower()
    if answer == "up" or answer == "w":
        print "fill in later5.1"
    
    elif answer == "down" or answer == "s":
        print "fill in later5.2"
    elif answer == "left" or answer == "a":
        print "fill in later5.3"
    elif answer == "right" or answer == "d":

           pass
 
    elif answer == "down" or answer == "s":
        print "fill in later4.2"
    elif answer == "left" or answer == "a":
        print "fill in later4.3"
    elif answer == "right" or answer == "d":
        print "fill in later4.4"

        answer = raw_input("fill in later4").lower()
        if answer == "left" or answer == "a":
         print "fill in later5"

    elif answer == "right" or answer == "d":
        print "insert story here"
    elif answer == "down" or answer == "s":
       print "insert story here"
    elif answer == "up" or answer == "w":
       print "insert story here"
#some easter eggs in the story include: a fire

    else:
        print "fill in later (GAME OVER/didn't choose anything"
        forest()

forest()

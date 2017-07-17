import pygame
import os
import random

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image
images=['kanye.png','chance.png','tpain.png','jcole.png','drake.png','childish.png']
cards={}
nums=list(range(1,13))
for image in images:
    for i in range(2):
        location=random.choice(nums)
        cards[location]=image
        nums.remove(location)           
pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
clock = pygame.time.Clock()
solved=[]
temp=[]
while not done:
        for event in pygame.event.get():
                screen.fill((255, 255, 255))
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if(len(temp)==2):
                        if(cards[temp[0]]==cards[temp[1]]):
                            solved.append(temp[0])
                            solved.append(temp[1])
                        temp=[]
                    if(len(solved)==12):
                        print("You win!")
                        pygame.mixer.music.load('finish.wav')
                        pygame.mixer.music.play(0)
                        done=True
                    else:
                        (mouseX, mouseY) = pygame.mouse.get_pos()
                        if(mouseX<200 and mouseY<200 and 1 not in solved):
                            temp.append(1)
                        elif(mouseX<400 and mouseY<200 and 2 not in solved):
                            temp.append(2)
                        elif(mouseX<600 and mouseY<200 and 3 not in solved):
                            temp.append(3)
                        elif(mouseX<800 and mouseY<200 and 4 not in solved):
                            temp.append(4)
                        elif(mouseX<200 and mouseY<400 and 5 not in solved):
                            temp.append(5)
                        elif(mouseX<400 and mouseY<400 and 6 not in solved):
                            temp.append(6)
                        elif(mouseX<600 and mouseY<400 and 7 not in solved):
                            temp.append(7)
                        elif(mouseX<800 and mouseY<400 and 8 not in solved):
                            temp.append(8)
                        elif(mouseX<200 and mouseY<600 and 9 not in solved):
                            temp.append(9)
                        elif(mouseX<400 and mouseY<600 and 10 not in solved):
                            temp.append(10)
                        elif(mouseX<600 and mouseY<600 and 11 not in solved):
                            temp.append(11)
                        elif(mouseX<800 and mouseY<600 and 12 not in solved):
                            temp.append(12)
                    
                        
        counter=1
        for i in range(0,601,200):
            for j in range(0,601,200):
                if counter in temp or counter in solved:
                    screen.blit(get_image(cards[counter]), (j, i))
                else:
                    screen.blit(get_image('mystery.png'), (j, i))
                counter+=1
        pygame.display.flip()
        clock.tick(60)
        

# import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
from game_functions import *
from blue_print_lookup import *
from math import cos, sin, sqrt




pygame.init()
display = (800,600)
screen = pygame.display.set_mode(display,DOUBLEBUF|OPENGL|RESIZABLE)



glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0]/display[1]), 1, 10000)

glTranslatef(0, 0, -500)


glMatrixMode(GL_MODELVIEW)
# gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)







glLoadIdentity()


displayCenter = [screen.get_size()[i] // 2 for i in range(2)]
mouseMove = [0, 0]
pygame.mouse.set_pos(displayCenter)


global ship1_speed_x, ship1_speed_y, ship1_speed_z
global ship2_speed_x, ship2_speed_y, ship2_speed_z
ship1_speed_x, ship1_speed_y, ship1_speed_z, ship1_pitch = 0, 0, 0, 0
ship2_speed_x, ship2_speed_y, ship2_speed_z, ship2_pitch = 0, 0, 0 , 0


up_down_angle = 0.0
paused = False
run = True
player_speed = 0




while run:

    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False
            if event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                paused = not paused
                pygame.mouse.set_pos(displayCenter) 
        if not paused: 
            if event.type == pygame.MOUSEMOTION:
                mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
            pygame.mouse.set_pos(displayCenter)    

    if not paused:
        # get keys
        keypress = pygame.key.get_pressed()
        #mouseMove = pygame.mouse.get_rel()


        glLoadIdentity()

        # apply the look up and down
        up_down_angle += mouseMove[1]*0.1
        glRotatef(up_down_angle, 1.0, 0.0, 0.0)

        

        print(viewMatrix)
   

       


        # init the view matrix
        glPushMatrix()
        glLoadIdentity()

        # apply the movment 
        if keypress[pygame.K_w]:
            glTranslatef(0,0,10)

        if keypress[pygame.K_s]:
            glTranslatef(0,0,-10)

        if keypress[pygame.K_d]:
            glTranslatef(-5,0,0)
        if keypress[pygame.K_a]:
            glTranslatef(5,0,0)

        if keypress[pygame.K_c]:
            glTranslatef(0,5,0)
        if keypress[pygame.K_x]:
            glTranslatef(0,-5,0)


        # apply the left and right rotation
        glRotatef(mouseMove[0]*0.1, 0.0, 1.0, 0.0)

        
        # glRotatef(mouseMove[1]*0.1, 1.0, 0.0, 0.0)





        # multiply the current matrix by the get the new view matrix and store the final
        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        # apply view matrix
        glPopMatrix()
        glMultMatrixf(viewMatrix)


        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glTranslatef(0 + ship1_speed_x, 0, -500 + ship1_speed_z)
        Ship.draw_ship(COBRA_MK_3)        
        glPopMatrix()
        ship1_speed_z += 2
        ship1_speed_x += -0

        glPushMatrix()
        glTranslatef(0 + ship2_speed_x, 0,  + ship2_speed_z)
        Ship.draw_ship(COBRA_MK_3)        
        glPopMatrix()
        ship2_speed_z += 0
        ship2_speed_x += -0




        draw_cross_hairs(screen)
        pygame.display.flip()
        pygame.time.wait(10)



pygame.quit()

import sys, math, pygame
from pygame.locals import *
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from blue_print_lookup import *







def solidship(VERTICES,EDGES):
	glEnable(GL_DEPTH_TEST)
	glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)


	glBegin(GL_TRIANGLE_STRIP)

	# glBegin(GL_TRIANGLE_FAN)

	for x in EDGES:
		for vertex in x:
			glColor3fv ((0,0,0))
			glVertex3fv(VERTICES[vertex])
	glEnd()


	glLineWidth(3)
	glEnable(GL_POLYGON_OFFSET_FILL)
	glPolygonOffset(2,2)


	glBegin(GL_LINES)
	for edge in EDGES:
		for cubeVertex in edge:
			glColor3fv ((300,300,300))
			glVertex3fv(VERTICES[cubeVertex])
	glEnd()







def draw_cross_hairs(gameDisplay):

	glMatrixMode(GL_PROJECTION)
	glPushMatrix()
	glLoadIdentity()

	glOrtho(- gameDisplay.get_width() // 2, gameDisplay.get_width() // 2, -gameDisplay.get_height() // 2, gameDisplay.get_height() // 2, 1, -1)

	glMatrixMode(GL_MODELVIEW)
	glPushMatrix()
	glLoadIdentity()
	glDisable(GL_DEPTH_TEST)


	glColor3f(255,255,255)
	glPointSize(10.0)

	glBegin(GL_LINES)
	glVertex2f(5, 0.0)
	glVertex2f(gameDisplay.get_height() // 35, 0)
	glEnd()

	glBegin(GL_LINES)
	glVertex2f(-5, 0.0)
	glVertex2f(-gameDisplay.get_height() // 35, 0)
	glEnd()


	glBegin(GL_LINES)
	glVertex2f(0, 5)
	glVertex2f(0, gameDisplay.get_height() // 35)
	glEnd()

	glBegin(GL_LINES)
	glVertex2f(0, -5)
	glVertex2f(0, -gameDisplay.get_height() // 35)
	glEnd()

	glEnable(GL_DEPTH_TEST)

	glMatrixMode(GL_PROJECTION)
	glPopMatrix()
	glMatrixMode(GL_MODELVIEW)
	glPopMatrix()






def to_center(x, y,gameDisplay):
	return x + gameDisplay.get_width() // 2, y + gameDisplay.get_height() // 2





















# def attack_ship(ship, x_cord, y_cord, z_cord):
# 	glPushMatrix()
# 	# resultant_speed = frame_speed + ship_speed
# 	glTranslatef(x_cord, y_cord, z_cord)
# 	# glRotated(a2, 0, 0, -1)
# 	Ship.draw_ship(ship)
# 	glPopMatrix()




















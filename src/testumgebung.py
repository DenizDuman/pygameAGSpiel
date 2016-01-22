# -*- coding: utf-8 -*-
import pygame
import sys
import math

sprites = {}
sprites["Kugel"] = pygame.image.load("C:\Programmieren\Python\pygameAGSpiel\media\Kugel.png")
sprites["Blume"] = pygame.image.load("C:\Programmieren\Python\pygameAGSpiel\media\Blume_01.png")
sprites["Spieler"] = pygame.image.load("C:\Programmieren\Python\pygameAGSpiel\media\Spieler.png")


BREITE = 1080
HOEHE = 1920
pygame.init()
fenster = pygame.display.set_mode((HOEHE, BREITE))
fps = pygame.time.Clock()

x_richtung = 50
x_change = 0
y_richtung= 100


	

gewonnen = False
abgebrochen = False

while not gewonnen and not abgebrochen:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			abgebrochen = True
		elif event.type == pygame.MOUSEBUTTONUP:
			print(event.pos)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				x_change += 10
			if event.key == pygame.K_a:
				x_change += -10
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a:
					x_change += 10
				if event.key == pygame.K_d:
					x_change += -10
			if event.key == pygame.K_SPACE:
				y_richtung-=10
				
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a or event.key == pygame.K_d:
				x_change = 0
				
			
	x_richtung += x_change
					
			
	
	
	fenster.fill((255,255,255))
	fenster.blit(sprites["Spieler"], (x_richtung,y_richtung))
	pygame.display.update()
	fps.tick(30)
	pygame.display.set_caption("Fps: " + str((round( fps.get_fps(), 2))))

	
sys.exit()
pygame.quit()


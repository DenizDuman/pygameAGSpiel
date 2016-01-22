# -*- coding: utf-8 -*-
import pygame
import sys
import math

sprites = {}
sprites["Kugel"] = pygame.image.load("C:\Programmieren\Python\pygameAGSpiel\media\Kugel.png")
sprites["Blume"] = pygame.image.load("C:\Programmieren\Python\pygameAGSpiel\media\Blume_01.png")
#sprites["Spieler"] = pygame.image.load("gelb.gif")


HOEHE = 500
BREITE = 500
pygame.init()
fenster = pygame.display.set_mode((HOEHE, BREITE))
fps = pygame.time.Clock()

gewonnen = False
abgebrochen = False

while not gewonnen and not abgebrochen:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			abgebrochen = True
		elif event.type == pygame.MOUSEBUTTONUP:
			print(event.pos)
			
	
	
	fenster.fill((255,255,255))
	fenster.blit(sprites["Blume"], (50,50))
	pygame.display.update()
	fps.tick(30)
	pygame.display.set_caption("Fps: " + str((round( fps.get_fps(), 2))))

	
sys.exit()
pygame.quit()


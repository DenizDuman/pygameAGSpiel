# -*- coding: utf-8 -*-
import pygame, sys , math, random


class Kugel:
	fluggeschwindigkeit = 10
	kugelPosition = ( -100, -100)
	def __init__( self, startPosition, blickrichtung):
		self.kugelPosition = startPosition
		self.flugrichtung = blickrichtung  / math.fabs(blickrichtung)
	def kugelBewegen(self):
		self.kugelPosition = (self.kugelPosition[0] + self.fluggeschwindigkeit * self.flugrichtung, self.kugelPosition[1] - random.randint(-2, 2))
		
		
		
		
		
		
		
def jump( durchlauf):
	sprunghoehe = 48
	x = int(sprunghoehe * math.sin(math.pi / 60 * durchlauf)) - int(sprunghoehe * math.sin(math.pi / 60 * (durchlauf - 1)))
	return x
	
	
def schiess( kugeln, spielerPosition, blickrichtung):
	neuKugel = Kugel(spielerPosition,blickrichtung)
	kugeln.append(neuKugel)
	return kugeln
def bewegeKugeln(kugeln):
	for RN in kugeln:
		RN.kugelBewegen()
def maleKugeln(kugeln):
	for RN in kugeln:
		fenster.blit(sprites["Kugel"], RN.kugelPosition)
	
def maleSpieler(spielerPosition):
	fenster.blit(sprites["Spieler"], (spielerPosition[0] - 37,spielerPosition[1] - 40))
	
	
	
	
	
	
sprites = {}
sprites["Kugel"] = pygame.image.load("C:\Programmieren\Python\pygameAGSpiel\media\Kugel.png")
sprites["Blume"] = pygame.image.load("C:\Programmieren\Python\pygameAGSpiel\media\Blume_01.png")
sprites["Spieler"] = pygame.image.load("C:\Programmieren\Python\pygameAGSpiel\media\Spieler.png")


BREITE = 1080
HOEHE = 1920
pygame.init()
fenster = pygame.display.set_mode((HOEHE, BREITE))
fps = pygame.time.Clock()


spielerPosition = ( 50, 500)
x_change = 0
geschwindigkeit = 5
blickrichtung = 1 # blickrichtung > 0 rechts          blickrichtung < 0 links

sprungAktiviert = False
sprungDauer = 0
y_change = 0

geschossen = False
kugeln = []

gewonnen = False
abgebrochen = False

while not gewonnen and not abgebrochen:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			abgebrochen = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			geschossen = True
		if event.type == pygame.MOUSEBUTTONUP:
			geschossen = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				x_change += geschwindigkeit
			if event.key == pygame.K_a:
				x_change -= geschwindigkeit
			if event.key == pygame.K_SPACE:
				sprungAktiviert = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				x_change += geschwindigkeit
			if event.key == pygame.K_d:
				x_change -= geschwindigkeit
			if event.key == pygame.K_SPACE:
				sprungAktiviert = False
			
	
	if sprungAktiviert or sprungDauer <= 63 and sprungDauer:
		y_change = jump( sprungDauer)
		sprungDauer += 1
	
	if sprungDauer == 63:
		sprungDauer = 0
		y_change = 0
	if geschossen:
		kugeln = schiess( kugeln, spielerPosition, blickrichtung)
		geschossen = False
	
	if x_change:
		blickrichtung = x_change
	spielerPosition = (spielerPosition[0] + x_change, spielerPosition[1] - y_change)
	bewegeKugeln(kugeln)
			
	

	fenster.fill((255,255,255))
	maleSpieler(spielerPosition)
	maleKugeln(kugeln)
	pygame.display.update()
	fps.tick(60)
	pygame.display.set_caption("Fps: " + str((round( fps.get_fps(), 2))))

	
sys.exit()
pygame.quit()


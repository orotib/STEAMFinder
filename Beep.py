from winsound import Beep
import time

A = 220
B = 247
C = 262
D = 294
E = 330
F = 349
G = 370
H = 390
I = 411
J = 430
K = 450
L = 470
M = 495
N = 515


def normal():
	#boci-boci
	beat = 200
	Beep(C, beat)
	Beep(E, beat)
	Beep(C, beat)
	Beep(E, beat)
	Beep(G, int(1.8*beat))
	Beep(G, int(1.8*beat))

	Beep(C, beat)
	Beep(E, beat)
	Beep(C, beat)
	Beep(E, beat)
	Beep(G, int(1.8*beat))
	Beep(G, int(1.8*beat))

	Beep(J, beat)
	Beep(I, beat)
	Beep(H, beat)
	Beep(G, beat)
	Beep(F, int(1.8*beat))
	Beep(G, int(1.8*beat))

	Beep(G, beat)
	Beep(F, beat)
	Beep(E, beat)
	Beep(D, beat)
	Beep(C, int(1.8*beat))
	Beep(C, int(1.8*beat))

def stattrak():
	#star wars
	beat = 375
	Beep(440, beat)
	Beep(440, beat)
	Beep(440, beat)
	Beep(349, int(0.7*beat))
	Beep(523, int(0.3*beat))
	Beep(440, beat)
	Beep(349, int(0.7*beat))
	Beep(523, int(0.3*beat))
	Beep(440, 2*beat)
	Beep(659, beat)
	Beep(659, beat)
	Beep(659, beat)
	Beep(698, int(0.7*beat))
	Beep(523, int(0.3*beat))
	Beep(415, beat)
	Beep(349, int(0.7*beat))
	Beep(523, int(0.3*beat))
	Beep(440, 2*beat)

def souvenir():
	#yankee doodle
	beat = 185;

	Beep(262, beat) # C
	Beep(262, beat) # C
	Beep(294, beat) # D
	Beep(330, beat) # E

	Beep(262, beat) # C
	Beep(330, beat) # E
	Beep(294, 2*beat) # D (double length)

	Beep(262, beat) # C
	Beep(262, beat) # C
	Beep(294, beat) # D
	Beep(330, beat) # E

	Beep(262, 2*beat) # C (double length)
	Beep(247, 2*beat) # B (double length)

	Beep(262, beat) # C
	Beep(262, beat) # C
	Beep(294, beat) # D
	Beep(330, beat) # E

	Beep(349, beat) # F
	Beep(330, beat) # E
	Beep(294, beat) # D
	Beep(262, beat) # C

	Beep(247, beat) # B
	Beep(196, beat) # G
	Beep(220, beat) # A
	Beep(247, beat) # B

	Beep(262, 2*beat) # C (double length)
	Beep(262, 2*beat) # C (double length)

def knife():
	#funky town
	beat = 210
	Beep(392, beat) #Frequency (Hz), Duration(ms)
	Beep(392, beat)
	Beep(349, beat)
	Beep(392, int(2.5*beat))
	Beep(294, int(2*beat))
	Beep(294, beat)
	Beep(392, beat)
	Beep(523, beat)
	Beep(494, beat) 
	Beep(392, beat)
	time.sleep(0.7)
	Beep(392, beat) #Frequency (Hz), Duration(ms)
	Beep(392, beat)
	Beep(349, beat)
	Beep(392, int(2.5*beat))
	Beep(294, int(2*beat))
	Beep(294, beat)
	Beep(392, beat)
	Beep(523, beat)
	Beep(494, beat) 
	Beep(392, beat)

def bestbuy():
	beat = 140
	for i in xrange(5):
		Beep(500, beat)
		Beep(1000, beat)
		Beep(1500, beat)
		Beep(2000, beat)
		Beep(2500, beat)
		Beep(3000, beat)
		Beep(3500, beat)
		time.sleep(0.2)

def makeSound(cat):
	if cat == 'StatTrak':
		stattrak() #star wars
	elif cat == 'normal':
		normal() #boci-boci
	elif cat == 'Souvenir':
		souvenir() #yankee doodle
	elif cat == 'Knife':
		knife() #funky town
	elif cat == 'StatTrak+':
		bestbuy()

souvenir()
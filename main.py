#-----------------------------------------------
#  Date  : 11. 2017
#  Autor : Benny
#
#  This is the main File
#-----------------------------------------------

import sys
import time
import os
import getch
import drawengine as g
import player
import Obj
import titlescreen
import village
import outskirts

#Engine Class is the hub for the important objects and changes rooms		
class Engine:
	run = True; 
	player = player.Player();
	matrix = [["" for i in range(102)] for i in range(52)];

	def __init__(self):
		self.matrix = g.Graphics.creatematrix([Obj.Obj(0,0,g.Graphics.drawrect(100,50,1," "))],self.matrix)
		#this is the room switcher
		#room_i 1-3 is title screen
		#room_i 1(n) is in the village
		#room_i 2(n) is the outskirts
		#room_i 3(n) is the forest
		#room_i 4(n) is the Castle / City
		#room_i 10(n) is for the Maps
		#room_i every room that doesn't exist in the if statement is ending the game
		while(self.run):
			if(self.player.room_i == 1):
				room = titlescreen.Titlescreen(self.player, self.matrix, 3);
				self.player = room.player;
				del room;
			elif(self.player.room_i == 2):
				room = titlescreen.Intro(self.player,self.matrix);
				self.player = room.player;
			elif(self.player.room_i == 3):
				room = titlescreen.Loadingscreen(self.player, self.matrix, 3);
				self.player = room.player;
				del room;
			elif(self.player.room_i >= 10 and self.player.room_i < 20):
				room = village.Village(self.player,10,19);
				self.player = room.player;
				del room;
			elif(self.player.room_i >= 20 and self.player.room_i < 30):
				room = outskirts.Greenfield(self.player,20,29);
				self.player = room.player;
				del room;
			else:
				self.run = False;
def main():
	engine = Engine();

main();
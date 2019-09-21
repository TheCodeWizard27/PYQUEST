#-----------------------------------------------
#  Date  : 11. 2017
#  Autor : Benny
#
#  This file contains:
#  The Menu Class
#-----------------------------------------------

import sys
import time
import os
import getch
import drawengine as g
import Obj
import getch

#Father of all Menu Rooms
class Menu:
	objlen = None; #Number of Switchable Menu elements
	matrix = None;
	background = None; #background defaults to white space
	player = None; #player object that holds valuable info
	menu_i = 1; #(menu_index) for knowing which menu element is active
	room_obj = []; #drawn objects
	run = True; #main loop runs as long as run is <True>
	
	#gets singel key press and moves selection in menu
	def input(self):
		key = ord(getch.getch());
		
		#move around in the menu
		if(key == 115):
			if(self.menu_i < self.objlen):
				self.menu_i += 1;
			else:
				self.menu_i = 1;
				
		elif(key == 119):
			if(self.menu_i > 1):
				self.menu_i -= 1;
			else:
				self.menu_i = self.objlen;
		
		elif(key == 13):
			return self.menu_i;
			
		elif(key == 27):
			return 99;
	
	#updating the menu elements needs to be overritten
	def update(self, menu_i):
		pass
	
	#declaration of every element
	def declarations(self):
		self.room_obj = [];
	
	#default initializer can be overritten
	def __init__(self, player, matrix, objlen):
		#passes valuable info
		self.player = player;
		self.objlen = objlen;
		self.matrix = [[" " for i in range(102)] for i in range(52)];
		self.background = [Obj.Obj(0,0,g.Graphics.drawmatrix(matrix))];
		self.declarations();
		
		#main loop
		while(self.run):
			g.Graphics.draw(None,self.background,self.room_obj,self.matrix,0.01);
			self.update(self.input());
		
#-----------------------------------------------
#  Date  : 11. 2017
#  Autor : Benny
#
#  This file contains:
#1 Obj Class
#2 Hitbox Class
#-----------------------------------------------

import sys
import time
import os
import getch

#class for every drawable object
class Obj:
	x = 0;
	y = 0;
	texture = "";
	
	def __init__(self,x,y,texture):
		self.x = x;
		self.y = y;
		self.texture = texture;

#invisible Hitboxes for events and borders
class Hitbox:
	inside = True;
	x = 0;
	y = 0;
	height = 0;
	width = 0;
	visibility = True;
	
	def checkbox(self, player):
		if(not self.inside):
			#checks if player is inside hitbox
			if(self.x <= player.char.x and self.x + self.width >= player.char.x):
				if(self.y <= player.char.y and self.y + self.height >= player.char.y):
					return True;
			return False;
		else:
			#checks if player is outside of hitbox
			if(self.x <= player.char.x and self.x + self.width >= player.char.x):
				if(self.y <= player.char.y and self.y + self.height >= player.char.y):
					return False;
			return True;

	def __init__(self,width,height,x,y,inside):
		self.inside = inside; #definens if hitbox check if player inside or outside
		self.width = width;
		self.height = height;
		self.x = x;
		self.y = y;
#-----------------------------------------------
#  Date  : 11. 2017
#  Autor : Benny
#
#  This file contains:
#  The Room Class
#-----------------------------------------------

import sys
import time
import os
import getch
import drawengine as g
import getch
import sub_menus

#Father of all Rooms
class Room:
	matrix = None; #The Matrix that holds the information for every x/y
	player = None; #Player Object holds valuable info about skills / stats / room
	room_obj = []; #all the Objects that need to be drawn in order to be drawn
	hud = []; #gets drawn over everything in order obviously
	solid_hitbox = []; #hitboxes that restrict your movement and puts you back
	trigger_hitbox = []; #triggerhitboxes trigger an action
	
	#standart function that can be overwriten
	def update(self):
		#checking solid hitboxes
		for i in range(0,len(self.solid_hitbox)):
			while (self.solid_hitbox[i].checkbox(self.player)):
				self.player.playerposres();
				
		#updating the drawn hud
		self.room_obj[len(self.room_obj) -1].x = self.player.char.x;
		self.room_obj[len(self.room_obj) -1].y = self.player.char.y;
		
		self.hud[6].texture = "Action [" + self.player.checksurround(self.matrix)+"]";
		
		self.hud[1].texture = "Name : " + str(self.player.name);
		self.hud[2].texture = "LVL  : " + str(self.player.stats["LVL"]);
		self.hud[3].texture = "HP   : " + str(self.player.stats["HP"]);
		self.hud[4].texture = "MP   : " + str(self.player.stats["MP"]);
		self.hud[5].texture = "Gold : " + str(self.player.stats["gold"]);
		self.hud[7].texture = "x    : " + str(self.player.char.x);
		self.hud[8].texture = "y    : " + str(self.player.char.y);	
		
	#room specific events
	def events(self):
		pass
		
	def input(self):
		#gets single key input and does smth
		key = ord(getch.getch());
		
		if(key in [119,97,100,115]):
			self.player.move_player(key); #standart player movement
		elif(key == 27):
			room = sub_menus.StartMenu(self.player, self.matrix, 4); #opens startmenu
			self.player = room.player;
			del room;
	
	#functions for declaring the objects of the room outside of this class
	def declarations(self):
		self.room_obj = [];
		self.hud = [];
		self.solid_hitbox = [];
		self.trigger_hitbox = [];
	
	#main initializer function can be overritten
	def __init__(self,player,min,max):
		self.player = player;
		self.matrix = [["" for i in range(102)] for i in range(52)];
		self.declarations();
		
		#main game loop
		while(self.player.room_i >= min and self.player.room_i <= max):
			g.Graphics.draw(self.hud,None,self.room_obj,self.matrix,0.01);
			self.input();
			self.events();
			self.update();
		
#-----------------------------------------------
#  Date  : 11. 2017
#  Autor : Benny
#
#  This file contains:
#  All the Village / Town / City room classes
#-----------------------------------------------

import sys
import time
import os
import getch
import hud
import drawengine as g
import super_room as s_m
import Obj
import external as x
import random
import battle

#village room 10
class Village(s_m.Room):
	def events(self):				
		#checking trigger hitboxes
		if(self.trigger_hitbox[0].checkbox(self.player)):
			self.player.room_i = 20;
			self.player.setposx(2);
		if(self.trigger_hitbox[1].checkbox(self.player)):
			room = battle.Battle(random.randint(0,3),self.player);
			del room;
		
	def declarations(self):
		#reseting arrays
		self.room_obj = [];
		self.hud = [];
		self.solid_hitbox = [];
		self.trigger_hitbox = [];
		
		#room objects initialization
		self.room_obj.append(Obj.Obj(1,1,x.texture_load("textures",2)));
		self.room_obj.append(Obj.Obj(20,20,g.Graphics.drawrect(20,10,1,"/")));
		
		self.room_obj.append(self.player.char);
		
		self.player.setposx(10);
		self.player.setposy(10);
		
		#hud
		self.hud = hud.Hud.return_hud();
		
		#solid hitboxes
		self.solid_hitbox.append(Obj.Hitbox(98,43,1,2,True));
		
		#trigger hitboxes
		self.trigger_hitbox.append(Obj.Hitbox(0,50,99,0,False));
		self.trigger_hitbox.append(Obj.Hitbox(19,10,20,20,False));#Debbuging Hitbox for testing pls delete late
		
		self.update();
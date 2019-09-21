#-----------------------------------------------
#  Date  : 11. 2017
#  Autor : Benny
#
#  This file contains:
#  All Greenfield rooms
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

#greenfield room 20
class Greenfield(s_m.Room):
	def events(self):		
		#checking trigger hitboxes
		#left screen transition
		if(self.trigger_hitbox[0].checkbox(self.player)):
			self.player.room_i = 10;
			self.player.setposx(96);
			
	def declarations(self):
		self.room_obj = [];
		self.hud = [];
		self.solid_hitbox = [];
		self.trigger_hitbox = [];
		
		self.player.setposx(2);
		
		#room objects initialization		
		self.room_obj.append(Obj.Obj(1,1,x.texture_load("textures",3)));
		self.room_obj.append(Obj.Obj(30,25,x.texture_load("textures",4)));
		self.room_obj.append(Obj.Obj(20,15,x.texture_load("textures",5)));
		self.room_obj.append(Obj.Obj(15,15,"?"));
		self.room_obj.append(Obj.Obj(1,40,x.texture_load("textures",6)));
		
		self.room_obj.append(self.player.char);
		
		#gui
		self.hud = hud.Hud.return_hud();
		
		#solid hitboxes
		self.solid_hitbox.append(Obj.Hitbox(98,40,0,3,1));
		self.solid_hitbox.append(Obj.Hitbox(1,2,21,16,0));
		self.solid_hitbox.append(Obj.Hitbox(3,0,20,17,0));
		
		#trigger hitboxes
		self.trigger_hitbox.append(Obj.Hitbox(0,50,0,0,0));
		
		self.update();
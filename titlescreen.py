#-----------------------------------------------
#  Date  : 11. 2017
#  Autor : Benny
#
#  This file contains:
#  All the Titlescreen classes
#-----------------------------------------------

import sys
import time
import os
import getch
import Obj
import sub_menus
import drawengine as g
import super_menu as s_m
import external as x
import getch
import player

#titlescreen room 1
class Titlescreen(s_m.Menu):
	def update(self, menu_i):
		#resets menu
		self.room_obj[4].texture = "  New Game";
		self.room_obj[5].texture = "  Load Game";
		self.room_obj[6].texture = "  Exit Game";
		
		if(menu_i != None):
			self.run = False;
			if (self.menu_i == 1):
				#goes into the char creation screen
				self.player.room_i = 2;
			elif(self.menu_i == 2):
				#opens loading titlescreen
				self.player.room_i = 3;
			else:
				#just ends the main loop
				self.player.room_i = 99;
				
		self.room_obj[self.menu_i + 3].texture = self.room_obj[self.menu_i + 3].texture + " ◄";

	def declarations(self):
		self.room_obj = [];
		self.matrix = [["" for i in range(102)] for i in range(52)];
		
		#creating'n loading all objects required for this room
		self.room_obj.append(Obj.Obj(1,28,x.texture_load("textures",9)));
		self.room_obj.append(Obj.Obj(30,16,x.texture_load("textures",1)));
		self.room_obj.append(Obj.Obj(30,25,x.texture_load("textures",1)));
		self.room_obj.append(Obj.Obj(30,34,x.texture_load("textures",1)));
		self.room_obj.append(Obj.Obj(35,18,"  New Game ◄"));
		self.room_obj.append(Obj.Obj(35,27,"  Load Game"));
		self.room_obj.append(Obj.Obj(35,36,"  Exit Game"));
		self.room_obj.append(Obj.Obj(29,5,x.texture_load("textures",0)));

#loading save state room 3
class Loadingscreen(s_m.Menu):
	def load(self, load):
		#loading previous save in the load file
		save = x.sv_load(load);
		self.player.name = str(save[0]);
		self.player.stats["gold"] = int(save[1],2);
		self.player.stats["LVL"] = int(save[2],2);
		self.player.stats["HP"] = int(save[3],2);
		self.player.stats["MP"] = int(save[4],2);
		self.player.stats["STR"] = int(save[5],2);
		self.player.stats["INT"] = int(save[6],2);
		self.player.stats["DEX"] = int(save[7],2);
		self.player.stats["VIT"] = int(save[8],2);
		#self.player.equipment["head"] = int(save[9],2);
		self.player.equipment["head"] = 70;
		self.player.equipment["body"] = int(save[10],2);
		self.player.equipment["arms"] = int(save[11],2);
		self.player.equipment["pants"] = int(save[12],2);
		self.player.equipment["boots"] = int(save[13],2);
		self.player.equipment["shield"] = int(save[14],2);
		self.player.equipment["weapon"] = int(save[15],2);
		
		for i in range(0, len(self.player.inventory)):
			self.player.inventory[i] = int(save[i + 16],2);
		for i in range(0, len(self.player.h_inventory)):
			for j in  range(2):
				self.player.h_inventory[i][j] = int(save[i*2 + j + 16 + len(self.player.inventory)],2);

	def update(self, menu_i):
		if(menu_i != 99 and menu_i != None):
			self.run = False;
			if (self.menu_i == 1):
				self.load(0);
				self.player.room_i = 10;
			elif(self.menu_i == 2):
				self.load(1);
				self.player.room_i = 10;
			else:
				self.load(2);
				self.player.room_i = 10;
		elif(menu_i == 99):
			self.run = False;
			self.player.room_i = 1;

		self.room_obj[4].texture = self.room_obj[4].texture.replace(" ◄","");
		self.room_obj[5].texture = self.room_obj[5].texture.replace(" ◄","");
		self.room_obj[6].texture = self.room_obj[6].texture.replace(" ◄","");
		
		if(self.menu_i == 1):
			self.room_obj[4].texture = self.room_obj[4].texture + " ◄";
		elif(self.menu_i == 2):
			self.room_obj[5].texture = self.room_obj[5].texture + " ◄"
		else:
			self.room_obj[6].texture = self.room_obj[6].texture + " ◄";

	def declarations(self):
		self.room_obj = [];
		self.matrix = [["" for i in range(102)] for i in range(52)];
		
		#creating'n loading all objects required for this room
		loadtext1 = "";
		loadtext2 = "";
		loadtext3 = "";
		
		save1 = x.sv_load(0);
		save2 = x.sv_load(1);
		save3 = x.sv_load(2);

		if(save1[0] == ""):
			loadtext1 = "Empty";
		else:
			loadtext1 = str(save1[0]) + " LVL: " + str(int(save1[2],2)) + " ◄";

		if(save2[0] == ""):
			loadtext2 = "Empty";
		else:
			loadtext2 = str(save2[0]) + " LVL: " + str(int(save2[2],2));

		if(save3[0] == ""):
			loadtext3 = "Empty";
		else:
			loadtext3 = str(save3[0]) + " LVL: " + str(int(save3[2],2));
		
		self.room_obj.append(Obj.Obj(1,28,x.texture_load("textures",9)));
		self.room_obj.append(Obj.Obj(30,16,x.texture_load("textures",1)));
		self.room_obj.append(Obj.Obj(30,25,x.texture_load("textures",1)));
		self.room_obj.append(Obj.Obj(30,34,x.texture_load("textures",1)));
		self.room_obj.append(Obj.Obj(35,18,loadtext1));
		self.room_obj.append(Obj.Obj(35,27,loadtext2));
		self.room_obj.append(Obj.Obj(35,36,loadtext3));
		self.room_obj.append(Obj.Obj(29,5,x.texture_load("textures",0)));
		
#intro room 2
class Intro:
	player = None;
	matrix = None;
	room_obj = [];

	def input(self):
		key = ord(getch.getch());
		if(key == 27):
			self.player.room_i = 1;

		if (self.room_obj[3].texture != ""):
			if (key == 8):
				self.room_obj[3].texture = self.room_obj[3].texture[:len(self.room_obj[3].texture)-1];
			elif(key == 13):
				questbox = sub_menus.Questbox(g.Graphics.creatematrix(self.room_obj,self.matrix));
				if (questbox.answer()):
					self.player = player.Player();
					self.player.name = self.room_obj[3].texture;
					self.player.room_i = 10;
				del questbox;

		if (key != 8 and key != 13):
			if(len(self.room_obj[3].texture) <= 9):
				self.room_obj[3].texture = self.room_obj[3].texture + chr(key);

	def __init__(self, player, matrix):
		self.player = player;
		self.matrix = [["" for i in range(102)] for i in range(52)];
		self.menu_i = 1;
		self.room_obj = [];

		self.room_obj.append(Obj.Obj(29,1,g.Graphics.drawrect(40,6,1," ")));
		self.room_obj.append(Obj.Obj(29,9,g.Graphics.drawrect(40,6,1," ")));
		self.room_obj.append(Obj.Obj(34,3,"How does thou call thyself?"));
		self.room_obj.append(Obj.Obj(33,11,""));

		while(self.player.room_i == 2):
			g.Graphics.draw(None,None,self.room_obj,self.matrix,0.01);
			self.input();
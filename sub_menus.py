#-----------------------------------------------
#  Date  : 11. 2017
#  Autor : Benny
#
#  This file contains:
#1 Stats Class
#2 Inventory Class
#3 StartMenu Class
#4 Subinventory Class
#5 Questbox class
#-----------------------------------------------

import sys
import time
import os
import getch
import external as x
import super_menu as s_m
import drawengine as g
import Obj

class Stats:
	matrix = None;
	background = None;
	player = None;
	room_obj = [];
	menu_i = 1;
	run = True;

	def input(self):
		key = ord(getch.getch());
		
		if(key == 27):
			self.run = False;
		
	def update(self):
		print();

	def __init__(self, player, matrix):
		self.player = player;
		self.room_obj = [];
		self.matrix = [[" " for i in range(102)] for i in range(52)];
		self.background = [Obj.Obj(0,0,g.Graphics.drawmatrix(matrix))];
		
		#creating'n loading all objects required for this room
		self.room_obj.append(Obj.Obj(21,1,g.Graphics.drawrect(78,42,1," ")));
		self.room_obj.append(Obj.Obj(22,3,g.Graphics.drawhline(76,1)));
		self.room_obj.append(Obj.Obj(23,2,"Statistics"));
		
		self.update();
			
		while(self.run):
			g.Graphics.draw(None,self.background,self.room_obj,self.matrix,0.01);
			self.input();
			self.update();		
		
class Inventory(s_m.Menu):		
	def update(self, key):
		if(key != 99 and key != None):
			item_i = 0;
			if(self.menu_i > 10 and self.menu_i < 18):
				if("empty" in self.room_obj[self.menu_i+5].texture.lower()):
					item_i = 3;
				else:
					item_i = 2;
			else:
				if(self.player.inventory[self.menu_i-1] < 70 and self.player.inventory[self.menu_i-1] > 0):
					item_i = 0;
				elif(self.player.inventory[self.menu_i-1] == 0):
					item_i = 3;
				else:
					item_i = 1;
			
			room = Sub_inventory(self.matrix,item_i);
			answer = room.answer();
			del room;
			
			if(item_i == 1):
				#need to add move function
				if(answer == 1):
					if(self.player.inventory[self.menu_i-1] >= 70 and self.player.inventory[self.menu_i-1] < 80):
						#hats
						item = self.player.equipment["head"];
						self.player.equipment["head"] = self.player.inventory[self.menu_i-1];
						self.player.inventory[self.menu_i-1] = item;
					elif(self.player.inventory[self.menu_i-1] >= 80 and self.player.inventory[self.menu_i-1] < 90):
						#body armor
						item = self.player.equipment["body"];
						self.player.equipment["body"] = self.player.inventory[self.menu_i-1];
						self.player.inventory[self.menu_i-1] = item;
					elif(self.player.inventory[self.menu_i-1] >= 90 and self.player.inventory[self.menu_i-1] < 100):
						#gloves
						item = self.player.equipment["arms"];
						self.player.equipment["arms"] = self.player.inventory[self.menu_i-1];
						self.player.inventory[self.menu_i-1] = item;
					elif(self.player.inventory[self.menu_i-1] >= 100 and self.player.inventory[self.menu_i-1] < 110):
						#pants
						item = self.player.equipment["pants"];
						self.player.equipment["pants"] = self.player.inventory[self.menu_i-1];
						self.player.inventory[self.menu_i-1] = item;
					elif(self.player.inventory[self.menu_i-1] >= 110 and self.player.inventory[self.menu_i-1] < 130):
						#boots
						item = self.player.equipment["boots"];
						self.player.equipment["boots"] = self.player.inventory[self.menu_i-1];
						self.player.inventory[self.menu_i-1] = item;
					elif(self.player.inventory[self.menu_i-1] >= 130 and self.player.inventory[self.menu_i-1] < 140):
						#shields
						item = self.player.equipment["shield"];
						self.player.equipment["shield"] = self.player.inventory[self.menu_i-1];
						self.player.inventory[self.menu_i-1] = item;
					elif(self.player.inventory[self.menu_i-1] >= 140 and self.player.inventory[self.menu_i-1] <= 170):
						#weapons
						item = self.player.equipment["weapon"];
						self.player.equipment["weapon"] = self.player.inventory[self.menu_i-1];
						self.player.inventory[self.menu_i-1] = item;
					
					
				elif(answer == 2):
					questbox = Questbox(self.matrix);
					if(questbox.answer()):
						self.player.inventory[self.menu_i-1] = 0;
			elif(item_i == 2):
				if(answer == 1):
					inventory_full = self.player.add_item(self.player.equipment[self.room_obj[self.menu_i+5].texture.split(" ")[0]]);
					
					if(not inventory_full):
						self.player.equipment[self.room_obj[self.menu_i+5].texture.split(" ")[0]] = 0;
					else:
						Infomsg(self.matrix, "Inventory is full");
						
				elif(answer == 2):
					questbox = Questbox(self.matrix);
					if(questbox.answer()):
						self.player.equipment[self.room_obj[self.menu_i+5].texture.split(" ")[0]] = 0;
			elif(item_i == 0):
				if(answer == 1):
					print();#need to add use events
				elif(answer == 2):
					questbox = Questbox(self.matrix);
					if(questbox.answer()):
						self.player.inventory[self.menu_i-1] = 0;
						
		elif(key == 99):
			self.run = False;

		self.player.inventory.sort(reverse=True)
		
		for i in range(0,len(self.player.inventory)):
			if(self.player.inventory[i] != 0):
				vorsatz = " " + str(i+1) if i+1 < 10 else str(i+1); 
				self.room_obj[i+6].texture = vorsatz + ": [ " + self.player.item_list[self.player.inventory[i]] + " ]";
			else:
				vorsatz = " " + str(i+1) if i+1 < 10 else str(i+1); 
				self.room_obj[i+6].texture = vorsatz + ": [ " + "Empty" + " ]";
				
		self.room_obj[16].texture = "head  [ " + self.player.item_list[self.player.equipment["head"]] + " ]";
		self.room_obj[17].texture = "body  [ " + self.player.item_list[self.player.equipment["body"]] + " ]";
		self.room_obj[18].texture = "arms  [ " + self.player.item_list[self.player.equipment["arms"]] + " ]";
		self.room_obj[19].texture = "pants [ " + self.player.item_list[self.player.equipment["pants"]] + " ]";
		self.room_obj[20].texture = "boots [ " + self.player.item_list[self.player.equipment["boots"]] + " ]";
		self.room_obj[21].texture = "weapon : [ " + self.player.item_list[self.player.equipment["weapon"]] + " ]";
		self.room_obj[22].texture = "shield : [ " + self.player.item_list[self.player.equipment["shield"]] + " ]";
		
		self.room_obj[self.menu_i+5].texture = self.room_obj[self.menu_i+5].texture + " ◄";
		
	def declarations(self):
		self.room_obj = [];
		
		#creating'n loading all objects required for this room
		self.room_obj.append(Obj.Obj(21,1,g.Graphics.drawrect(78,42,1," ")));
		self.room_obj.append(Obj.Obj(22,3,g.Graphics.drawhline(76,1)));
		self.room_obj.append(Obj.Obj(23,2,"Equipement"));
		self.room_obj.append(Obj.Obj(22,26,g.Graphics.drawhline(76,1)));
		self.room_obj.append(Obj.Obj(23,25,"Inventory"));
		self.room_obj.append(Obj.Obj(23,4,x.texture_load("textures",7)));
		for i in range(1,11):
			self.room_obj.append(Obj.Obj(23,26+i," "+str(i)+":[ Empty ]" if(i<10) else str(i)+":[ Empty ]"));
		
		self.room_obj.append(Obj.Obj(61,5,"[ Empty ]"));
		self.room_obj.append(Obj.Obj(61,9,"[ Empty ]"));
		self.room_obj.append(Obj.Obj(61,11,"[ Empty ]"));
		self.room_obj.append(Obj.Obj(61,17,"[ Empty ]"));
		self.room_obj.append(Obj.Obj(61,20,"[ Empty ]"));
		self.room_obj.append(Obj.Obj(52,22,"Weapon : [ " + self.player.item_list[self.player.equipment["weapon"]] + " ]"));
		self.room_obj.append(Obj.Obj(52,23,"Shield : [ " + self.player.item_list[self.player.equipment["shield"]] + " ]"));
		
		self.update(None);
			
#start menu where you can access your inventory stats and the map		
class StartMenu(s_m.Menu):
	def update(self, menu_i):
		#resets all menu elements
		for i in range(3,8):
			self.room_obj[i].texture = self.room_obj[i].texture.replace(" ◄","");
		
		self.room_obj[self.menu_i + 3].texture = self.room_obj[self.menu_i + 3].texture + " ◄";
		
		if(menu_i != 99 and menu_i != None):
			if(self.menu_i == 1):
				room = Inventory(self.player, self.matrix, 17);
				self.player = room.player;
				del room;
			elif(self.menu_i == 2):
				room = Stats(self.player, self.matrix);
				self.player = room.player;
				del room;
			elif(self.menu_i == 3):
				room = Stats(self.player, self.matrix);
				self.player = room.player;
				del room;
			elif(self.menu_i == 4):
				questbox = Questbox(g.Graphics.creatematrix(self.room_obj,self.matrix));
				if (questbox.answer()):
					self.player.room_i = 1;
					self.run = False;
				del questbox;
		elif(menu_i == 99):
			self.run = False;
		
	def declarations(self):
		self.room_obj = [];
		
		#objects of window
		self.room_obj.append(Obj.Obj(1,1,g.Graphics.drawrect(20,42,1," ")));
		self.room_obj.append(Obj.Obj(2,3,g.Graphics.drawhline(18,1)));
		self.room_obj.append(Obj.Obj(2,36,x.texture_load("textures",8)));
		self.room_obj.append(Obj.Obj(3,2,"Menu"));
		self.room_obj.append(Obj.Obj(3,4,"Inventory ◄"));
		self.room_obj.append(Obj.Obj(3,6,"Stats"));
		self.room_obj.append(Obj.Obj(3,8,"Map"));
		self.room_obj.append(Obj.Obj(3,10,"Exit"));

#gets specifig action of inventory item
class Sub_inventory:
	menu_i = 1;
	matrix = [];
	background = [];
	room_obj = [];
	run = True;
	
	def answer(self):
		return self.menu_i;
	
	def input(self):
		key = ord(getch.getch());
		if(key == 115):
			if(self.menu_i < 3):
				self.menu_i = self.menu_i +1;
			else:
				self.menu_i = 1;
		if(key == 119):
			if(self.menu_i > 1):
				self.menu_i = self.menu_i -1;
			else:
				self.menu_i = 3;
		elif(key == 27):
			self.menu_i = 4;
			self.run = False;
		elif(key == 13):
			self.run = False;
			
		for i in range(3):
			self.room_obj[i+1].texture = self.room_obj[i+1].texture.replace("◄", " ");
			self.room_obj[i+1].texture = self.room_obj[i+1].texture.replace("►", " ");
		
		self.room_obj[self.menu_i].texture = "►" + self.room_obj[self.menu_i].texture[1:len(self.room_obj[self.menu_i].texture)-2] + " ◄";
		
	def __init__(self, matrix, item_i):
		self.room_obj = [];
		self.matrix = [["" for i in range(102)] for i in range(52)];
		self.background = [Obj.Obj(0,0,g.Graphics.drawmatrix(matrix))];
		
		self.room_obj.append(Obj.Obj(43,22,g.Graphics.drawrect(14,6,1," ")));
		if(item_i == 0):
			#if item in inventory range but index between 1 and 70 
			self.room_obj.append(Obj.Obj(45,23,"► Use ◄"));
		elif(item_i == 1):
			#if item in inventory range but index between 70 and 170
			self.room_obj.append(Obj.Obj(45,23,"► Equip ◄"));
		elif(item_i == 2):
			#if item in equipment range
			self.room_obj.append(Obj.Obj(45,23,"► Unequip ◄"));
		elif(item_i == 3):
			#if item selected emtpy just close
			self.run = False;
			self.menu_i = 3;
			
		self.room_obj.append(Obj.Obj(45,25,"  drop  "));
		self.room_obj.append(Obj.Obj(45,27,"  cancel  "));
		
		while(self.run):
			g.Graphics.draw(None,self.background,self.room_obj,self.matrix,0.01);
			self.input();
			
			
#verifys action of user
class Questbox:
	menu_i = 1;
	matrix = [];
	background = [];
	room_obj = [];
	run = True;
	
	def answer(self):
		if (self.menu_i == 1):
			return True;
		else:
			self.menu_i = 1;
			return False;
	
	def input(self):
		key = ord(getch.getch());
		if(key == 97 or key == 100):
			if (self.menu_i == 1):
				self.room_obj[2].texture = "  yes  ";
				self.room_obj[3].texture = "► no ◄";
				self.menu_i = 2;
			else:
				self.room_obj[2].texture = "► yes ◄";
				self.room_obj[3].texture = "  no  ";
				self.menu_i = 1;
		elif(key == 13):
			self.run = False;
	
	def __init__(self, matrix):
		self.room_obj = [];
		self.matrix = [["" for i in range(102)] for i in range(52)];
		self.background = [Obj.Obj(0,0,g.Graphics.drawmatrix(matrix))];
		
		self.room_obj.append(Obj.Obj(37,16,g.Graphics.drawrect(20,6,1," ")));
		self.room_obj.append(Obj.Obj(41,18,"ARE YOU SURE?"));
		self.room_obj.append(Obj.Obj(40,21,"► yes ◄"));
		self.room_obj.append(Obj.Obj(48,21,"  no  "));
		
		while(self.run):
			g.Graphics.draw(None,self.background,self.room_obj,self.matrix,0.01);
			self.input();
	
class Infomsg:
	matrix = [];
	background = [];
	room_obj = [];
	
	def __init__(self, matrix, text):
		self.room_obj = [];
		self.matrix = [["" for i in range(102)] for i in range(52)];
		self.background = [Obj.Obj(0,0,g.Graphics.drawmatrix(matrix))];
		
		self.room_obj.append(Obj.Obj(37,16,g.Graphics.drawrect(25,6,1," ")));
		self.room_obj.append(Obj.Obj(39,19,text));
		
		g.Graphics.draw(None,self.background,self.room_obj,self.matrix,0.01);
		getch.getch();
	
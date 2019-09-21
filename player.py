#-----------------------------------------------
#  Date  : 11. 2017
#  Autor : Benny
#
#  This file contains:
#  The Player Class
#-----------------------------------------------

import sys
import time
import os
import getch
import Obj

#player class
class Player:
	char = None;
	facing = 0; #0 is up / 1 is down / 2 is right / 3 is left
	speed = 0.1
	name = "";
	last_room_i = 1;
	room_i = 1; #0 is debug
	stats = {"LVL":1,"gold":10,"HP":100,"MP":100,"STR":8,"INT":8,"DEX":8,"VIT":8};
	equipment = {"head":0,"body":0,"arms":0,"pants":0,"boots":0,"shield":0,"weapon":0}
	
	#--------------------------------------------------------------------------------------------------
	#
	#item lists
	
	#item index range definition
	#1-39 materials
	#40-69 usables
	#70-79 hats
	#80-89 body armors
	#90-99 gloves
	#100-109 pants
	#110-129 boots
	#130-139 shields
	#140-170 weapons
	
	item_list = {0:"Empty",1:"Stick",2:"stone",3:"copper",4:"iron",5:"adamant",6:"warpite",7:"wood",
	70:"SantasHat"
	};
	
	#
	#--------------------------------------------------------------------------------------------------
	#
	#enemy lists
	
	enemies = {0:"TestSlime",1:"TestGolbin",2:"TestBandit"}
	
	#
	#--------------------------------------------------------------------------------------------------
	inventory = [0 for i in range(10)];
	h_inventory = [[0,0] for i in range(40)];
	
	def __init__(self):
		self.char = Obj.Obj(15,15,"҈");
	
	#returns char infront of player
	def checksurround(self, matrix):
		if(self.facing == 0):
			return matrix[self.char.y - 1][self.char.x];
		elif(self.facing == 1):
			return matrix[self.char.y + 1][self.char.x];
		elif(self.facing == 2):
			return matrix[self.char.y][self.char.x + 1];
		else:
			return matrix[self.char.y][self.char.x - 1];
		
	def setposx(self,x):
		self.char.x = x;
		self.x = x;
	
	def setposy(self,y):
		self.char.y = y;
		self.y = y;
	
	#moves player coordinate acordingly to key input
	def move_player(self, direction):
		if(direction == 119):
			self.char.y = self.char.y -1;
			self.facing = 0;
			time.sleep(self.speed);
		elif(direction == 97):
			self.char.x = self.char.x -1;
			self.facing = 3;
			time.sleep(self.speed/2);
		elif(direction == 100):
			self.char.x = self.char.x +1;
			self.facing = 2;
			time.sleep(self.speed/2);
		elif(direction == 115):
			self.char.y = self.char.y +1;
			self.facing = 1;
			time.sleep(self.speed);
	
	def move_inventory(self, item1_i, item2_i):
		item1_value = self.inventory[item1_i];
		item2_value = self.inventory[item2_i];
		self.inventory[item1_i] = item2_value;
		self.inventory[item2_i] = item1_value;
	
	def add_item(self, item):
		item_i = 1;
		
		for i in range(0,len(self.inventory)):
			if(self.inventory[i] == 0 and item_i > 0):
				item_i -= 1;
				self.inventory[i] = item;
		
		#if inventory full
		if (item_i == 1):
			return True;
	
	#resets player one position back
	def playerposres(self):
		if(self.facing == 0):
			self.char.y = self.char.y +1;
		elif(self.facing == 1):
			self.char.y = self.char.y -1;
		elif(self.facing == 2):
			self.char.x = self.char.x -1;
		elif(self.facing == 3):
			self.char.x = self.char.x +1;
			
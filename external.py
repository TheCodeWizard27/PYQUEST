#-----------------------------------------------
#  Date  : 11. 2017
#  Autor : Benny
#
#  This file contains:
#  All the external file Functions
#-----------------------------------------------

import sys
import time
import os
import getch

#loads specifig texture and returns it as a string
def texture_load(filename, texture):
	file = open(filename, "r", encoding="utf-8");
	string = file.readlines()[texture].split("\\n");
	return "\n".join(string);

#returns array of save	
def sv_load(load):
	file = open("load", "r", encoding="utf-8");
	array = file.readlines()[load].split("0b");
	return array;

#saves stats of player	
def sv_save(player,slot):
	file = open("load", "r");
	string = file.readlines();
	
	#if empty or corrupt reset to just a b c
	if(len(string) != 3):
		string = ["a","b","c"];		
	
	file.close();
		
	file = open("load", "w", encoding="utf-8");
	save = player.name + str(bin(player.stats["gold"]));
	save = save + str(bin(player.stats["LVL"]));
	save = save + str(bin(player.stats["HP"])) + str(bin(player.stats["MP"]));
	save = save + str(bin(player.stats["STR"])) + str(bin(player.stats["INT"]));
	save = save + str(bin(player.stats["DEX"])) + str(bin(player.stats["VIT"]));
	save = save + str(bin(player.equipment["head"]))+str(bin(player.equipment["body"]));
	save = save + str(bin(player.equipment["arms"]))+str(bin(player.equipment["pants"]));
	save = save + str(bin(player.equipment["boots"]))+str(bin(player.equipment["shield"]));
	save = save + str(bin(player.equipment["weapon"]));
	for i in range(0, len(player.inventory)):
		save = save + str(bin(player.inventory[i]));
	for i in range(0, len(player.h_inventory)):
		for j in range(2):
			save = save + str(bin(player.h_inventory[i][j]));
	string[0] = string[0].replace("\n","");
	string[1] = string[1].replace("\n","");
	string[2] = string[2].replace("\n","");
	string[slot] = save;
	file.write("\n".join(string));
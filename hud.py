#-----------------------------------------------
#  Date  : 11. 2017
#  Autor : Benny
#
#  This file contains:
#  The Hud class
#-----------------------------------------------

import sys
import time
import os
import getch
import Obj
import drawengine as g

#gui
class Hud:
	def return_hud():
		obj_list = [];
		
		obj_list.append(Obj.Obj(1,44,g.Graphics.drawrect(98,5,1," ")));#obj 0 border
		obj_list.append(Obj.Obj(2,44,""));#obj 1
		obj_list.append(Obj.Obj(2,45,""));#obj 2
		obj_list.append(Obj.Obj(2,46,""));#obj 3
		obj_list.append(Obj.Obj(2,47,""));#obj 4
		obj_list.append(Obj.Obj(20,45,""));#obj 5
		obj_list.append(Obj.Obj(20,46,""));#obj 6
		
		#for debbuging only
		obj_list.append(Obj.Obj(2,48,""));
		obj_list.append(Obj.Obj(20,48,""));
		
		return obj_list;
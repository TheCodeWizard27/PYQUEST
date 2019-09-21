#-----------------------------------------------
#  Date  : 11. 2017
#  Autor : Benny
#
#  The Drawengine
#-----------------------------------------------

import sys
import time
import os
import getch
import Obj

#drawing engine
class Graphics:
	#draws to screen
	def draw(hud, background, objects, matrix, timeout):
		os.system('cls');
		
		#create background to matrix defaults to empty box
		if(background == None):
			matrix = Graphics.creatematrix(objects,Graphics.creatematrix([Obj.Obj(0,0,Graphics.drawrect(100,50,1," "))],matrix));
		else:
			matrix = Graphics.creatematrix(objects,Graphics.creatematrix(background, matrix));
			
		#draws without or with hud
		if(hud != None):
			sys.stdout.write(Graphics.drawmatrix(Graphics.creatematrix(hud,matrix)));
		else:
			sys.stdout.write(Graphics.drawmatrix(matrix));
			
		#screen timer
		time.sleep(timeout);
	
	#adds objects to matrix
	def creatematrix(objects,matrix):
		for obj in objects:
			texture = obj.texture.split("\n");
			for y in range(0,len(texture)):
				for x in range(0,len(texture[y])):
					matrix[obj.y + y][obj.x + x] = texture[y][x];
		return matrix;
	
	#turns matrix into 2D string
	def drawmatrix(matrix):
		string = [];
		for i in matrix:
			string.append("".join(i));
		return "\n".join(string);
	
	#returns a horizontal line as a string
	def drawhline(width,type):
		charset = [" ","─","═","█"];
		
		return charset[type]*width;
	
	#returns a vertical line as a string
	def drawvline(height,type):
		charset = [" ","│","║","█"];
		
		return (charset[type]+"\n")*height;
	
	#return a rectangle as a string
	def drawrect(width,height,type,fill):
		charset = ["    ","┌┐│└┘","╔╗║╚╝","█████"];
		
		rect = charset[type][0] + Graphics.drawhline(width-2,type) + charset[type][1] + "\n";
		for i in range(height-1):
			rect = rect + charset[type][2] + fill*(width-2) + Graphics.drawvline(1,type);
		return rect + charset[type][3] + Graphics.drawhline(width-2,type) + charset[type][4];
		

#-----------------------------------------------
#  Date  : 11. 2017
#  Autor : Benny
#
#  This file contains:
#  The Battle Class 
#-----------------------------------------------

import sys
import time
import os
import getch
import drawengine as g
import Obj

#The Battle Class
class Battle:
    matrix = None;
    player = None;
    room_obj = [];
    monster_i = 0;  #which monster appears
    run = True;
    
    def input(self):
        key = getch.getch();
    
    def __init__(self, monster_i, player):
        self.room_obj = []; #reseting array
        self.player = player;
        self.monster_i = monster_i,
        self.matrix = [[" " for i in range(102)] for i in range(52)];
        
        #battle screen objects definition
        self.room_obj.append(Obj.Obj(1,2,"Test"));
        
        #main game loop
        while(self.run):
            g.Graphics.draw(None,None,self.room_obj,self.matrix,0.01);
            self.input();
/*
#  Copyright (C) 2014  Rafael Senties Martinelli
#  	
#
#  This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License 3 as published by
#   the Free Software Foundation.
#
#  This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software Foundation,
#   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA.
*/

import java.util.Random;
import java.lang.Math;

public class Position{

	private int xMax=60; 	// Si cette valeur est modifiEe il faut modifier CarteX de la classe Main
	private int yMax=15;	// Si cette valeur est modifiEe il faut modifier CarteY de la classe Main
	protected int x,y;
	
	
	public void Position(){
		
		Random rand = new Random();
		int randx = rand.nextInt((this.xMax - 1) + 0) + 0;
		int randy = rand.nextInt((this.yMax - 1) + 0) + 0;
		
		this.SetPosition(randx,randy);	
	}
	
	
	public void SetPosition(int x, int y){
		this.SetX(x);
		this.SetY(y);
	}
	
	public int GetX(){
		return this.x;
	}
	
	public int GetY(){
		return this.y;
	}
	
	public void SetX(int xcord){
		
		int difference;
	
		if (xcord >= 0 && xcord < xMax){
			this.x=xcord;
		}
		
		// Si l'animal veut sortir de la carte, il est renvoyE dans la direction contraire
		else if (xcord < 0){
			this.x=xcord*-1;
		}
		
		else if (xcord >= xMax){
			difference=xcord-xMax;
			this.x=xMax-difference-1;
		}
	
	}
	
	public void SetY(int ycord){
		int difference;
		
		if (ycord >= 0 && ycord < yMax){
			this.y=ycord;
		}
		
		else if (ycord < 0){
			this.y=ycord*-1;
		}
		
		else if (ycord >= yMax){
			difference=ycord-yMax;
			this.y=yMax-difference-1;
		}
	}


	// cette methode n'est jamais utilisEe. Elle a ETE crEe pour faire bouger les annimaux
	// afaimEes vers leurs cible, mais le code pour deplacer les annimaux n'a pas EtE crEe.
	public double Distance(Position pos){
		int dx,dy,px,py;
		double distance;
	
		px=pos.GetX();
		py=pos.GetY();
		
		dx=this.x-px;
		dy=this.y-py;
		
		distance=Math.sqrt(Math.pow(dx,2)+Math.pow(dy,2));
		return distance;
	}
}

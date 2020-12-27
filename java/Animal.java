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

public class Animal extends Vivant{

	protected String Mange;
	protected int Faim; // le nombre d'objects que l'animal peut manger dans 1 tour
	protected int RangeDeChasse; // a combien de distance l'animal peut manger
	protected int NbCycles; // le nombre de fois que le animal s'est deplacE sans manger
	protected int MaxFaim; // le degrE de faim qu'il faut pour que l'annimal meurt

	public void Animal(){
		this.NbCycles=0;
	}
	
	public void Deplacer(){
		
		Random rand = new Random();

		int randx = rand.nextInt(( 1 - 0) + 1);
		int randy = rand.nextInt(( 1 - 0) + 1);
		

		int signex = rand.nextInt(( 1 - 0) + 1);
		int signey = rand.nextInt(( 1 - 0) + 1);
		
		if (signex==1){
			this.position.SetX(this.position.GetX()-randx);
		}
		else{
			this.position.SetX(this.position.GetX()+randx);
		}
	
		if (signey==1){
			this.position.SetY(this.position.GetY()-randy);
		}
		else{
			this.position.SetY(this.position.GetY()+randy);
		}
			
	}
	
	public String Mange(){
		return this.Mange;
	}
	
	public int GetFaim(){
		return this.Faim;
	}
	
	public int GetRangDeChasse(){
		return this.RangeDeChasse;
	}
	
	public int GetNbCyles(){
		return this.NbCycles;
	}
	
	public int GetMaxFaim(){
		return this.MaxFaim;
	}
	
	public void SetNbCyles(int cyc){
		this.NbCycles=cyc;
	}
	
}

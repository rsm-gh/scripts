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

public class Loup extends Animal {

	public Loup(){
		this.SetNom("Loup");
		this.Symbole="X";
		this.Mange="O"; //Mouton
		this.Faim=1;
		this.RangeDeChasse=2;
		
		Random rand = new Random();
		this.MaxFaim= rand.nextInt((100 - 50) + 1) + 50;
	}
}

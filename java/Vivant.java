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

public class Vivant {

	protected Position position;
	protected String Nom;
	protected String Symbole;
	
	public Vivant(){
		this.position=new Position();
		this.position.Position();
	}
	
	public String GetNom(){
		return this.Nom;
	}
	
	public String GetSymbole(){
		return this.Symbole;
	}
	
	public void SetNom(String nom){
		this.Nom=nom;
	}
}

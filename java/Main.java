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

import java.lang.*;
import java.util.Random;

public class Main{

	// Variables du jeu
	protected static int CarteX=60;	// Si cette valeur est modifiEe il faut modifier xMax de la classe Position
	protected static int CarteY=15; // Si cette valeur est modifiEe il faut modifier yMax de la classe Position
	protected static int NbLoups=4;
	protected static int NbMoutons=15;
	protected static int NbHerbes=100;
	protected static int ActCarte=200; // Actualization de la carte en milisecondes
	
	///////////////////////////////////////////////////////////////////////////////////////////////////////////
	///////////////////////////////////////////////////////////////////////////////////////////////////////////
	///////////////////////////////////////////////////////////////////////////////////////////////////////////


	// Tableau d' afichage
	protected static String carte[][] = new String[CarteX][CarteY];
	
	// Liste qui contient les objects loups moutons etc
	protected static Loup Loups[] = new Loup[NbLoups];
	protected static Mouton Moutons[] = new Mouton[NbMoutons];
	protected static Herbe Herbes[] = new Herbe[NbHerbes];
	
	
	// Carte qui contient le ID des objects. Le ID est le numero de la ligne des listes
	
	/* Amelioration:
	Il serait mieux de pouvoir creer une Carte qui accepte different types d'objects,
	(loups,herbe,moutons). Cela eviterai davoir plusieurs cartes.
	
	*/
	
	protected static int carte_loups[][] = new int[CarteX][CarteY];
	protected static int carte_herbes[][] = new int[CarteX][CarteY];
	protected static int carte_moutons[][] = new int[CarteX][CarteY];

	public static int Vie=NbLoups+NbMoutons;
	public static int LoupsMortsDeFaim=0;
	public static int MoutonsMortsDeFaim=0;
	public static int HerbesManges=0;
	public static int MoutonsManges=0;
	
	protected static int Total=NbLoups+NbMoutons;

	public static void main (String[] args) {

		/* Au debut plusieurs objects peuvent apparaitre au meme endroit. En suite,
		  les animaux ne sont jamais mis dans une position deja ocuppEe par un autre animal.
		  Cela veux dire que pendant le deroulement du jeux seulement plusieurs herbes peuvent etre superposEes */


		InitializerCarte();  // il n'y a pas besoin des faire des methodes pour ces inits car ils sont appelEs 
		InitializerLoups();	 // qu'une seule fois. Cependant ca rends plus clair le Main!
		InitializerMoutons();
		InitializerHerbes();
		
		
		while (Vie > 0){
			
			AfficherHerbes();
			
			DeplacerLoups();
			MangerMoutons();
			ImprimerCarte();
			
			DeplacerMoutons();
			MangerMoutons(); // si un mouton se deplace vers un loup, le loup le mange!
			MangerHerbe();
			ImprimerCarte();
			
			Sleep(ActCarte);
		}
	}
	
	
	public static void Sleep(int time){
		try {
			Thread.sleep(time);
		} 
		catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	
	public static void ImprimerCarte(){
		
		// Ceci imprime la carte
		System.out.print("\033[H\033[2J");
		System.out.print("+");
		for( int i = 0; i < CarteX; ++i){
			System.out.print("-");
		}
		System.out.print("+");
		System.out.println("");
		
		for( int j = 0; j < CarteY; ++j){
			System.out.print("|");
			for( int i = 0; i < CarteX; ++i){
   				//carte[i][j]="O";
				System.out.print(carte[i][j]);
			}
			System.out.print("|");
			System.out.println("");
		}
		
		
		System.out.print("+");
		for( int i = 0; i < CarteX; ++i){
			System.out.print("-");
		}
		System.out.print("+");
		System.out.println("");
		
		
		// Ceci imprime les donEes
		int nb;
		
		nb=0;
		for( int i = 0; i < NbLoups; ++i){
			if (Loups[i] != null ){
				nb=nb+1;
			}
		}
		Vie=nb;
		System.out.print("Loups: "+nb+"/"+NbLoups+"   ");
		
		
		nb=0;
		for( int i = 0; i < NbMoutons; ++i){
			if (Moutons[i] != null ){
				nb=nb+1;
			}
		}
		Vie=Vie+nb;
		System.out.print("Moutons: "+nb+"/"+NbMoutons+"   ");
		
		
		nb=0;
		for( int i = 0; i < NbHerbes; ++i){
			if (Herbes[i] != null ){
				nb=nb+1;
			}
		}
		System.out.print("Herbes: "+nb+"/"+NbHerbes+"   ");
		
		System.out.print("Animaux: "+Vie+"/"+Total+"   ");
		System.out.println("");
		System.out.println("");
		System.out.println("Morts de Faim: "+LoupsMortsDeFaim+" Loups et "+MoutonsMortsDeFaim+" Moutons.");
		System.out.println("MangEs: "+MoutonsManges+" Moutons et "+HerbesManges+" Herbes.");
	}
	
	
	public static void InitializerCarte(){
		for( int j = 0; j < CarteY; ++j){
			for( int i = 0; i < CarteX; ++i){
   				carte[i][j]=" ";
				
				// Je profite pour initializer les cartes des ids moutons loups etc
				carte_loups[i][j]=-1;
				carte_moutons[i][j]=-1;
				carte_herbes[i][j]=-1;
				
			}
			System.out.println("");
		}
	}
	
	public static void InitializerLoups(){

		for( int i = 0; i < NbLoups; ++i){
			Loups[i]=new Loup();
			carte_loups[Loups[i].position.GetX()][Loups[i].position.GetY()]=i;
		}
	}
	
	public static void InitializerMoutons(){

		for( int i = 0; i < NbMoutons; ++i){
			Moutons[i]=new Mouton();
			carte_moutons[Moutons[i].position.GetX()][Moutons[i].position.GetY()]=i;
		}
	}
	
	public static void InitializerHerbes(){
		for( int i = 0; i < NbHerbes; ++i){
			Herbes[i]=new Herbe();
			carte_herbes[Herbes[i].position.GetX()][Herbes[i].position.GetY()]=i;
		}
	}
	
	
	public static void AfficherHerbes(){
		
		Herbe this_Herbe;
		int posx,posy;
		
		for( int i = 0; i < NbHerbes; ++i){
			
			this_Herbe=Herbes[i];
			
			if (this_Herbe != null){
			
				posx=this_Herbe.position.GetX();
				posy=this_Herbe.position.GetY();
				
				carte[posx][posy]=this_Herbe.GetSymbole();
			}
		}
	}
	
	
	public static void DeplacerLoups(){
		
		Loup this_loup;
		int posx,posy,vieuxx,vieuxy;
		
		for( int i = 0; i < NbLoups; ++i){
			
			this_loup=Loups[i];
			
			if (this_loup != null){
			
				vieuxx=this_loup.position.GetX();
				vieuxy=this_loup.position.GetY();
				
				do{
					this_loup.Deplacer();
				
					posx=this_loup.position.GetX();
					posy=this_loup.position.GetY();	
				
				}
				while(carte[posx][posy]==this_loup.GetSymbole());
				// ceci evite d'avoir deux loups dans la meme position

				this_loup.SetNbCyles(this_loup.GetNbCyles()+1);
				
				carte[vieuxx][vieuxy]=" ";
				carte[posx][posy]=this_loup.GetSymbole();
					
				carte_loups[vieuxx][vieuxy]=-1;
				carte_loups[posx][posy]=i;

			}
		}
	}
	
	public static void MangerHerbe(){
		
		Mouton this_mouton;
		int posx,posy,faim,rang;
		
		for( int i = 0; i < NbMoutons; ++i){
			
			this_mouton=Moutons[i];
			
			if (this_mouton != null){
				
				posx=this_mouton.position.GetX();
				posy=this_mouton.position.GetY();
				
				rang=this_mouton.GetRangDeChasse();
				
				// Regarder au tour s'il peut manger... 
				faim=0;
				for (int k = posx-rang; k <=posx+rang; k++){
					for (int j = posy-rang; j <= posy+rang; j++){
						if (k >= 0 && k<CarteX && j >= 0 && j<CarteY){ // On ne peut que manger a l'interieur des tableaux
							if (carte_herbes[k][j] >= 0){ // Nous avons trouvE une victime!
								faim=faim+1;
								
								if (faim <= this_mouton.GetFaim()){
									
									
									if (faim > 1){
										posx=this_mouton.position.GetX();
										posy=this_mouton.position.GetY();
									}
								
									Herbes[carte_herbes[k][j]]=null; 
									carte_herbes[k][j]=-1;
								
									// On deplace le mouton a la position de l'herbe			
									carte_moutons[posx][posy]=-1;
									carte_moutons[k][j]=i;
									
									carte[posx][posy]=" ";
									carte[k][j]=this_mouton.GetSymbole();
									
									this_mouton.position.SetX(k);
									this_mouton.position.SetY(j);
									
									HerbesManges=HerbesManges+1;
								}
								else{
									return;
								}
							}
						}
					}
				}
				if(this_mouton.GetNbCyles()>=this_mouton.GetMaxFaim()){
					Moutons[i]=null; // le mouton meurt de faim
					carte[posx][posy]=" ";
					carte_moutons[posx][posy]=-1;
					MoutonsMortsDeFaim=MoutonsMortsDeFaim+1;
				}
			}
		}
	}
	
	public static void MangerMoutons(){
		
		Loup this_loup;
		int posx,posy,faim,rang;
		
		for( int i = 0; i < NbLoups; ++i){
			
			this_loup=Loups[i];
			
			if (this_loup != null){
				
				posx=this_loup.position.GetX();
				posy=this_loup.position.GetY();
				
				rang=this_loup.GetRangDeChasse();
				
				// Regarder au tour s'il peut manger... 
				faim=0;
				for (int k = posx-rang; k <=posx+rang; k++){
					for (int j = posy-rang; j <= posy+rang; j++){
						if (k >= 0 && k<CarteX && j >= 0 && j<CarteY){ // On ne peut que manger a l'interieur des tableaux
							if (carte_moutons[k][j] >= 0){ // Nous avons trouvE une victime!
								faim=faim+1;
								
								if (faim <= this_loup.GetFaim()){
								
									if (faim > 1){
										posx=this_loup.position.GetX();
										posy=this_loup.position.GetY();
									}
								
								
									this_loup.SetNbCyles(0);
								
									// On tue le mouton!
									Moutons[carte_moutons[k][j]]=null; 
									carte_moutons[k][j]=-1;
								
									// On deplace le loup a la position du mouton			
									carte_loups[posx][posy]=-1;
									carte_loups[k][j]=i;
									
									carte[posx][posy]=" ";
									carte[k][j]=this_loup.GetSymbole();
									
									this_loup.position.SetX(k);
									this_loup.position.SetY(j);
									
									MoutonsManges=MoutonsManges+1;
								}
							}
						}
					}
				}		
				if(this_loup.GetNbCyles()>=this_loup.GetMaxFaim()){
					Loups[i]=null; // le loup meurt de faim
					carte[posx][posy]=" ";
					carte_loups[posx][posy]=-1;
					LoupsMortsDeFaim=LoupsMortsDeFaim+1;
				}
			}
		}
	}
	
	

	public static void DeplacerMoutons(){
		
		Mouton this_mouton;
		int posx,posy,vieuxx,vieuxy;
		
		for( int i = 0; i < NbMoutons; ++i){
			
			this_mouton=Moutons[i];
			
			if (this_mouton != null){
				vieuxx=this_mouton.position.GetX();
				vieuxy=this_mouton.position.GetY();
				
				this_mouton.Deplacer();
				
				posx=this_mouton.position.GetX();
				posy=this_mouton.position.GetY();
				
				
				do{
					this_mouton.Deplacer();
				
					posx=this_mouton.position.GetX();
					posy=this_mouton.position.GetY();
				
				}
				while(carte[posx][posy]==this_mouton.GetSymbole());
				// ceci evite d'avoir deux moutons sur la meme position
				
				this_mouton.SetNbCyles(this_mouton.GetNbCyles()+1);
				
				carte[vieuxx][vieuxy]=" ";
				carte[posx][posy]=this_mouton.GetSymbole();
					
				carte_moutons[vieuxx][vieuxy]=-1;
				carte_moutons[posx][posy]=i;
			}
		}
	}	
}

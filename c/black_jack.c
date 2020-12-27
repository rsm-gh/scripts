/*
#  Copyright (C) 2014  Rafael Senties Martinelli
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

// Version 0.0

/* 
  
  Play Black Jack in the terminal.
  
  I had to do this game for the university (the code had to be in french). The game works fine, but it has at least two bugs:
  
        - "scanf": I had to double the values of scanf because if not it is skipped. 
        - So some times the user has to input the enter key two times.
        ~ I believe that there is an error when counting the player cards (Remember that the bank has one extra point).
        * 
*/

#define NB_JEU 5    // Nombre des paquets des cartes. ( commencent par 0 et < 10)

#include <stdio.h>
#include <unistd.h>
#include <time.h>                   
#include <stdlib.h>                 

#define RED "\033[31m"
#define RESET "\033[0m"
#define GREEN   "\033[32m"
#define YELLOW  "\033[33m" 

int NB_JOUEURS; 
int cube[13][3][NB_JEU]={0};
char type_de_carte[13][6]={"A","2","3","4","5","6","7","8","9","10","Valet","Dame","Roi"};


void carte_en_string(int carte_id){
    int i,c,k;
    char *type;
    
    if (carte_id < 100){
        carte_id=carte_id*10;
    }
    
    k=carte_id%10;
    c=((carte_id-k)%100)/10;
    i=(carte_id-c-k)/100;

    //printf("\n %d,%d,%d,%d,%s",carte_id,i,c,k," "); // debug
    
    type=type_de_carte[i];
    
    if (c==0){
        printf("%s%s%s%s ",RED,type,"♦",RESET );    
    }
    if (c==1){
        printf("%s%s%s%s ",RED,type,"♥",RESET );            
    }
    if (c==2){
        printf("%s♣ ",type);            
    }
    if (c==3){
        printf("%s♠ ",type);            
    }
    if (c>3){
        printf(RED,"\nErreur dans void carte_en_string",RESET );            
    }
}


void afficher_le_sabot(){
    int i,c,k,etat;
    printf("\nHauteur;Couleur;jeu;etat");         
    for (i=0;i<13; i++){
        for(c=0; c<3; c++){
            for(k=0; k<NB_JEU; k++){
                etat=cube[i][c][k];
                printf("\n %d,%d,%d,%d",i,c,k,etat);
            }
        }
    }
}

void repartir_carte(int joueur){
    int i,c,k,etat,nb_cartes;
    etat=1;
    
    // On trouve une carte qui n'a pas Ã©tÃ© utilisÃ©e ( e=0 )
    while (etat!=0){
        i=rand()%12;
        c=rand()%3;
        k=rand()%NB_JEU;
        etat=cube[i][c][k];
    }
    
    // On attribut la carte au joueur
    nb_cartes=calculer_nb_de_cartes(joueur);
    
    //printf("\n %d,%d",nb_cartes,joueur); // debugage
    //printf("\n %d,%d,%d,%d",i,c,k,etat); // debugage
    
    cube[i][c][k]=joueur*100+nb_cartes+1;
}   

int calculer_nb_de_cartes(int joueur){
    int i,c,k,etat,cartes;
    cartes=-1; //  les cartes commencent a  0. Ex 100, 200, 300
    
    if (joueur>0){ // prevention du BUG_000

        // on escane le cube
        for (i=0;i<13; i++){
            for(c=0; c<3; c++){
                for(k=0; k<NB_JEU; k++){
                    etat=cube[i][c][k];

                    // si la carte appartient Ã  l'utilisateur..
                    if (etat>0 && etat>=joueur*100 && etat<=joueur*100+99){
                        cartes+=1;
                    }
                }
            }
        }
        return cartes;
    }
}

int calculer_les_points(int joueur){
    int i,c,k,etat,conteur_az,points;
    points=0;
    conteur_az=0;
    
    if (joueur>0){

        for (i=0;i<13; i++){
            for(c=0; c<3; c++){
                for(k=0; k<NB_JEU; k++){
                    etat=cube[i][c][k];
                    //printf("\n %d",etat);
                    // si la carte appartient Ã  l'utilisateur..
                    if (etat>0 && etat>=joueur*100 && etat<=joueur*100+99){
                        
                        // on aditione les points
                            if (i==0){ // si c'est un az
                                points=points+11;
                                conteur_az=+1;
                            }
                            else{
                                if (i>=9 && i<13){ // 10,valet,dame,roi
                                    points=points+10;
                                }
                                if(i>0 && i<9){
                                    points=points+i+1;
                                }
                            }
                            //printf("\n %s,%d,%s,%d","hauteur",i,"points",points); //debug
                    }
                }
            }
        }
        
        while (points>21 && conteur_az>0){
            points=points-10;
            conteur_az=-1;
        }
        return points;
    }
}   



void afficher_les_cartes(int joueur,int cachees){
    int nb_cartes,i,c,k,etat,ordre_de_carte;
    nb_cartes=calculer_nb_de_cartes(joueur);
    int tableau_des_cartes[nb_cartes];
    
    // trouver et rentrer les cartes dans l'ordre au tableau
    if (joueur>0){
        for (i=0;i<13; i++){
            for(c=0; c<3; c++){
                for(k=0; k<NB_JEU; k++){
                    etat=cube[i][c][k];
                    
                    // si la carte appartient Ã  l'utilisateur..
                    if (etat>0 && etat>=joueur*100 && etat<=joueur*100+99){
                        ordre_de_carte=etat-joueur*100;
                        //printf("\n %s,%d,%d","ordre des cartes, nb_cartes",ordre_de_carte,nb_cartes); //debug
                        tableau_des_cartes[ordre_de_carte]=i*100+c*10+k;
                    }
                }
            }
        }
        if (cachees==0 || cachees==3){
            if (cachees==0){
                printf("   Cartes: ");
            }
            for (i=0;i<=nb_cartes;i++){
                carte_en_string(tableau_des_cartes[i]);
            }
        }
        if (cachees==1){
            for (i=0;i<nb_cartes;i++){
                carte_en_string(tableau_des_cartes[i]);
            }
        }
    }
}



void imprimer_lavancement(int i){
    int o,nb_cartes,points;
    
    printf("\033c");
    
    printf("\nTerminal Black Jack: ");
    
    for (o=1;o<NB_JOUEURS;o++){
        
        if (o<i || o>i){
            points=calculer_les_points(o);
            nb_cartes=calculer_nb_de_cartes(o);
            
            if (o>1){
                printf(" <> ");
            }           
            
            if (points>21){
                printf(" %s%s%s",RED,"Perdu",RESET);
            }
            else{
                if (points==21 && nb_cartes==1){
                    printf(" %s %s%s",YELLOW,"BJ",RESET);
                }
                else{
                    afficher_les_cartes(o,1);
                }
            }
        }
        if (o==i){
            if (o>1){
                printf(" <> ");
            }
            printf(" %s%s%s",GREEN,"En Jeu",RESET);
        }
    }
    
    // la machine afiche ses cartes
    printf(" <> ");
    afficher_les_cartes(NB_JOUEURS,1);
    
    // Le joueur active regarde ces cartes
    printf("\n\n");
    afficher_les_cartes(i,0);
}


int main(void){
    int i,c,k,o,points,etat,cartes,nb_cartes1,gagnant,terminer,decision,pointsmachine,cartesmachine;
    srand (time(NULL));
    
    decision=0;
    while (decision<=0){
        printf("\033c");
        printf("\n%s\n%s\n\n%s%s%s\n%s","GPL3 - (C) Rafael Senties Martinelli <rafael@senties-martinelli.com>","Site Web: rsm.imap.cc/GNU-Linux",GREEN,"Terminal Black Jack",RESET,"Entrez le numero de joueurs: ");
        scanf("%d", &decision);
    }
    NB_JOUEURS=decision+1;
    
    terminer=0;
    while (terminer==0){
        
        // Ici on reparti les deux premieres cartes Ã  tous les joueurs
        i=1;
        printf("\033c");
        for (i=1;i<=NB_JOUEURS;i++){
            repartir_carte(i);
            repartir_carte(i);
            //printf("\033c");
        }
        //afficher_le_sabot(); // debugage
        
        printf("\033c");
        printf("\n\n%s","Appuyez sur entree pour afficher les cartes du premier joeur.");
        getchar();
        getchar();
        
        // Chaque joueur demande des cartes
        for (i=1;i<NB_JOUEURS;i++){
            decision=1;
            o=0;
            
            // Les joueurs choisisent leurs cartes
            while (decision>0){
                
                decision=-1;
                while (decision<0 || decision>1){
                    imprimer_lavancement(i);
                    printf("\n\n%s","Voulez vous une autre carte? (0/1): ");
                    scanf("%d", &decision);
                }
                
                if (decision==1){
                    repartir_carte(i);
                    points=calculer_les_points(i);
                    //printf("\n %d",points); //debug
                    if (points>21){
                        imprimer_lavancement(i);
                        printf("\n\n%s%s%s%s",RED,"Vous avez depassE 21.",RESET,"Vous avez perdu.");
                        printf("\n%s","Appuyez sur entree pour passer au prochain joueur.");
                        getchar();
                        getchar(); 
                        decision=0;
                        o=1;
                    }
                }
            }
            
            if (i<NB_JOUEURS-1 && o==0){
                printf("\033c");
                printf("\n\n%s","Appuyez sur entree pour passer au prochain joueur.");  
                getchar();
                getchar();
            }
        }
        
        // Maintenant c'est la machine qui joue
        points=calculer_les_points(NB_JOUEURS);
        while (points<17){
            repartir_carte(NB_JOUEURS);
            points=calculer_les_points(NB_JOUEURS);
        }
        
        
        // Voir qui a le plus de points et le moins de cartes..
        // Aficher toutes les cartes et annoncer le gagnant
        printf("\033c");
        printf("\n%s","Terminal Black Jack: ");
        for (o=1;o<=NB_JOUEURS;o++){
            if (o>1){
                printf("<> ");
            }
            afficher_les_cartes(o,3);
        }
        
        
        
        cartesmachine=calculer_nb_de_cartes(NB_JOUEURS);
        pointsmachine=calculer_les_points(NB_JOUEURS);
        
        for (i=1;i<NB_JOUEURS;i++){
            points=calculer_les_points(i);
            
            if (points>21){
                printf("\n%s %d %s","Le joueur:",i,"a perdu");
            
            }
            else{
                if (pointsmachine>21){
                    printf("\n%s %d %s","Le joueur:",i,"a gagnE");
                }
                else{
                    if (pointsmachine<21){
                        pointsmachine=pointsmachine+1;
                    }
                    if (points>=pointsmachine){
                        cartes=calculer_les_points(i);
                        if (cartesmachine>cartes){
                            printf("\n%s %d %s","Le joueur:",i,"a gagnE");
                        }
                        if (cartesmachine<cartes){
                            printf("\n%s %d %s","Le joueur:",i,"a perdu");
                        }
                        if (cartesmachine==cartes){
                            printf("\n%s %d %s","Il faut comparer les cartes pour voir si:",i,"a perdu ou gagnE");
                        }
                    }
                    else{
                        printf("\n%s %d %s","Le joueur:",i,"a perdu");  
                    }
                }
            }
        }
        
        
        
        
        
        // enlever toutes les cartes utilisEs et conter celles qui sont utilisables
        o=0;
        for (i=0;i<13; i++){
            for(c=0; c<3; c++){
                for(k=0; k<NB_JEU; k++){
                    etat=cube[i][c][k];
                    if (etat>0){
                        cube[i][c][k]=-1;
                    }
                    if (etat==0){
                        o+=1;
                    }
                }
            }
        }
        
        
        
        
        if (o>NB_JOUEURS*5){
            printf("\n\n%s\n","Appuyez sur une touche pour recommencer.");  
            getchar();
            getchar();
        }
        else{
            printf("\n\n%s\n","Il ne reste pas beaucoup de cartes dans le sabot. Il sera melangE.");
            for (i=0;i<13; i++){
                for(c=0; c<3; c++){
                    for(k=0; k<NB_JEU; k++){
                        cube[i][c][k]=0;
                    }
                }
            }
            getchar();
        }
    }
    
    return 0;
}

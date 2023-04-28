Project:
Develop a software program in Python

Project Description:
This program was created to help in organization of chess tournaments.

How to run the program:

	1) Place your command line in /YOUR_FOLDER and then "git clone https://github.com/Alexandre-Kolobov/Projet_4.git"
	
	2)In the folder make "pip install -r requirements.txt" to set up the right configuration
	
	3)Now you are ready to execute the program. In the commande line make "python gestionnaire_des_tournois.py".
	
How to use it:
	The program has three main menus with its submenus:
	1. Rapports - this choice will allow you to consult rapports for each tournament
		1. Afficher la liste des tournois existant dans la base - show all saved tournaments 
		2. Afficher la liste des joueurs existant dans la base - show all saved players 
		3. Afficher les informations detaillées d'un tournois - show detailed informations about one tournament
		    1. Afficher les joueurs participants - show players in tournament
			2. Afficher les matchs joués - show played matchs
			3. Revenir au menu des rapports - back to the main menu 
			4. Quitter le logiciel - to close the program
		4. Revenir au menu des tournois - back to the main menu
		5. Quitter le logiciel - to close the program
		

	2. Sélectionner un tournois dans la base des tournois - this choice will allow you to load one tournament (you can continue the tournament or check its information if the tournament is finished)
		If the tournament is finished you will see:
			1. Afficher les joeurs participants au tournoi - show players in tournament
			2. Afficher les matchs - show played matchs
			3. Revenir au menu des tournois - back to the main menu
			4. Quitter le logiciel - to close the program
		If the tournament is not finished you will resume from the place it was saved
		
	3. Créer un nouveau tournois - this choice allow you to create a new tournament and also to create new players
		After entering name, place and additional infromations of tournament, you will see this menu:
		    1. Afficher la liste des joueurs existant dans la base  - show all saved tournaments 
			2. Afficher la liste des joueurs participant au tournoi - show players in tournament
			3. Ajouter un joueur au tournois - add player from the detabase to tournament
			4. Créer un nouveau joueur - create a new player
			5. Démmarer le tournois - start tournament
			6. Sauvegarder et quitter - to close the program
			7. Revenir au menu des tournois - back to the main menu
	
	4. Quitter le logiciel - to close the program
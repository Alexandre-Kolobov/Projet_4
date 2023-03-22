class View():
    def get_player_informations(self):
        while True:
            first_name = str(input("Tapez le prénom du joueur: "))
            if first_name.isalpha():
                break
            else:
                print ("Le prénom du joueur doit contenir que des lettres et ne pas être vide")
        
        

        family_name = input("Tapez le nom du joueur: ")
        birth_date = input("Tapez la date de naissance du joueur (DDMMYYYY): ")
        add_player = input("Voulez vous ajouter un autre joueur (Y/N)? ")
        
        return first_name, family_name, birth_date, add_player

    

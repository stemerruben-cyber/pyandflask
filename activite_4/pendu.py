import random
from unidecode import unidecode

class Pendu :

  # Variables temporaires
  lettres_devinees = []
  mot_a_deviner = ""
  mot_a_afficher = ""
  vies = 0

  # Fonction permettant d'initialiser le pendu
  # Renvoie la data (=état du jeu) correspondante
  def initialiser(mot_a_deviner, vies):
    mot_a_deviner = unidecode(mot_a_deviner).upper()
    print("le mot à deviner est "+mot_a_deviner)
    data = {
     "mot_a_deviner" : mot_a_deviner, # Le mot à deviner (en MAJUSCULES)
     "mot_a_afficher" : "-" * len(mot_a_deviner),   # Le mot à afficher
     "lettres_testees" : [],        # Liste des lettres déjà devinées
     "vies" : vies,                  # Nombre de vies restantes
     "victoire" : False,             # True si le mot a été trouvé
     "defaite" : False,              # True si plus de vies
     "input" : ""                    # Lettre ou mot entré par l'utilisateur
    }
    return data

  # Fonction principale à appeler en lui fournissant la data
  # La data est un dictionnaire avec les clés suivantes :
  #    mot_a_deviner, mot_a_afficher, lettres_devinees,
  #    vies, victoire, defaite, dernier_input
  # L'input est simplement la chaîne de caractère donnée au pendu
  def deviner(data, input):
    # On récupère toutes les données dans des variables temporaires
    global mot_a_afficher
    global mot_a_deviner
    global vies
    global lettres_devinees
    lettres_devinees = data["lettres_testees"]
    mot_a_deviner = data["mot_a_deviner"]
    mot_a_afficher = data["mot_a_afficher"]
    vies = data["vies"]
    entree = unidecode(input).upper()
    
    # On prépare la data (=état du jeu) qui sera envoyé en retour
    data_retour = {
      "dernier_input" : entree,
      "victoire" : False,
      "defaite" : False
    }

    # On appelle les fonctions deviner_lettre ou deviner_mot qui font tout le boulot
    if len(entree) == 1:
      message = Pendu.deviner_lettre(entree)
    else:
      message = Pendu.deviner_mot(entree)

    # On met à jour la data qui sera envoyée en retour
    data_retour["vies"] = vies
    data_retour["mot_a_deviner"] = mot_a_deviner
    data_retour["mot_a_afficher"] = mot_a_afficher
    data_retour["lettres_testees"] = lettres_devinees
    #data_retour["message"] = message
    data_retour["victoire"] = not "-" in mot_a_afficher
    if vies <= 0 :
      data_retour["defaite"] = True

    # Et enfin on retourne notre data !
    return data_retour

  # Fonction gérant le fait de deviner la présence de la lettre voulue dans le mot
  def deviner_lettre(lettre):
    global lettres_devinees
    global mot_a_deviner
    global vies
    if lettre in lettres_devinees:
      return "Cette lettre a déjà été devinée !"
    else:
      lettres_devinees.append(lettre)
      print(lettre+" / "+mot_a_deviner)
      if lettre in mot_a_deviner:
        Pendu.remplacer_lettre(lettre)
        return "Bonne lettre !"
      else:
        Pendu.enlever_vie()
        return "La lettre n'est pas dans le mot ! Il vous reste " + str(vies) + " vies."

  # Fonction gérant le fait de deviner le mot
  def deviner_mot(mot):
    global mot_a_afficher
    global mot_a_deviner
    global vies
    if mot == mot_a_deviner:
      mot_a_afficher = mot
      return ""
    else:
      Pendu.enlever_vie()
      return "Désolé, ce n'est pas ce mot ! Il vous reste " + str(vies) + " vies."

  # Enlève une vie
  def enlever_vie():
    global vies
    vies = vies - 1

  # Actualise le mot à afficher en remplaçant les "-" concernés par la lettre donnée
  def remplacer_lettre(lettre):
    global mot_a_afficher
    global mot_a_deviner
    for i in range(len(mot_a_deviner)):
      if mot_a_deviner[i] == lettre:
        mot = list(mot_a_afficher)
        mot[i] = lettre
        mot_a_afficher = ''.join(mot)
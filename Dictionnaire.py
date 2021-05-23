#coding:utf-8 #pour encoder les (é-à) etc. Toujours en haut complètement


Pour sublimetext (CTRL+Shift + P et tapper SSP) pour syntaxe python 

Pour linux dans la consol = python3 allo.py 
Pour Windows dans la consol = allo.py

int(1-32) float(2.4-3.6) str("allo") bool(True-False) on appel sa Caster une donner # Ne les mélange pas  pour les analysé !!!
x = float(3) # Réponse: 3.0

print(type(2.2))# Affiche le type de class

help(XXX) # Pour voir tout les fonctions d'une class

MaVariable ou nom pour fonction MaFonction # Appeller une variable ou une fonction, lettre majuscule au début des mots.

------------------------------------------------------------------------------------------------------------ Module --------------------
#les import mettre en haut en dessous du coding
import os # Importation d'une bibliothque autre que celle de base de python
os.fonction() # Avec le import on appelle la fonction dans le os a l'aide de . ensuite la fonction()

from math import sqrt  # Depuis la bibliotheque math tu importe la fonction sqrt et le * veut dire tout a place du sqrt (une class dans une class)
# Avec from on enleve le math. avant la fonction sqrt()

# Modularité créé des fichier code.py (block) Si je cré un fichier programme.py avec une fonction def allo(): print("allo tout le monde")
import programme # Va importé le fichier(dans le meme dossier) que jai créé avec des fonctions (autre dossier, import dossier.programme as programme)
programme.allo() # Va appeller dans le fichier programme, la fonction allo et l'exécute (qui cré un dossier de lien en cache)
if __name__ == '__main__': # Appellation dans un modul pour tester des fonctions appeller en dessous du if
	fonction1()
	fonction2()


------------------------------------------------------------------------------------------------------------ Print --------------------
print("allo") # Le print sert à afficher dans la consol et les " À mettre pour les mots " et rien pour les chiffres
print("Teste \n saut de ligne ")   # Saut de ligne
print("\t teste espace \t voila ")   # Espace avant le texte (tableture)


------------------------------------------------------------------------------------------------------------ Variable -----------------
#mettre les variable en haut en dessous des import
AgePersonne=35 #Syntax de nomentlature de variable Majuscule pour debuter un nom pas d'espacement
Benoit=True #Les True et False son avec lettre majuscule au début ou 0 et 1
Naissance="31 Juillet" #Variable avec mot

print(AgePersonne) # afficher la valeur de la variable
print("Age de la personne est de", AgePersonne)#affiche la phrase + le résultat de la valeur

Valeur=True # Donner de la variable est True
Valeur=int(Valeur) # Transforme la valeur True en int(chiffre)
print(Valeur) # Affiche 1 par ce que le 1=True et 0=False


------------------------------------------------------------------------------------------------------------ Chaine de caractères -----
a="allo"
#La chaine fait une copie et la modifie
b=a.upper() #Tout mettre en majuscule
b=a.lower() #Tout mettre en minuscule
b=a.capitalize() #Mettre en majuscule le début de chaque phrase
b=a.title() #Mettre en majuscule le début de chaque mot
b=a.strip() #Enleve tout les espaces
b=a.replace("X", "Y", 2) #remplace tout les X par Y (sur 2 optionel)
b=a.center(50, "-") #Mettre en majuscule le début de chaque mot -----allo-----
print(a.find(llo)) #recherche si le mot est la et si oui il affiche a partir de quel nombre il commence a partir de 0
print(a.index(llo)) #meme chose que find mais éleve une exception si pas la. (try)
phrase="Allo comment ça va" 
print(phrase.split(" ")) #transforme la variable en list de 4 parties
#Vérifier les: isidentifier() (class def etc) iskeyword() islower() (si il a une lettre majuscule) isupper() a faire avec un if-else
	#isalpha() isalphanum() isdigit() isdecimal isnumeric()


------------------------------------------------------------------------------------------------------------ Calcul -------------------
Pour un égal ==
Additionner += 
Soustraire -= 
Multiplier *=

a=38
Ex: a += 4
print(a) # Égal 42

Ex: b=(a+4)
print(b) # Égal 42


------------------------------------------------------------------------------------------------------------ Format ------------------
a="Benoit"
b="Marie-Jo"
print(f"{a} est en amour avec {b}") #Afficher les variable dans les {}
OU
print("{} est en amour avec {}".format (a, b)) #Afficher les variable dans les {}


------------------------------------------------------------------------------------------------------------ Temps et date -----------
import time
import datetime

%d : jour (01 à 31) - %A : jour (Monday) - %a : jour (Mon.)
%m : mois (01 à 12) - %B : mois (April) - %b : mois (Apr.)
%Y : année (2020) - %y (20)
%H : heures (00 à 24)
%I : minutes (00 à 59)
%S : secondes (00 à 59)
%p : AM/PM
%Z : fuseau horaire (Canada)

print(time.strftime("%A,%B,%Y,%p,%Z")) #Affiche la date etc.
print(datetime.datetime(2002, 5, 5, 12, 59, 59))#Affiche bien le AAAA/M/J H-M-S ou juste time pour H-M-S et juste date pour AAAA/M/J
print(date.today()) #Affiche la date (from datetime import date)
print(time.time()) #Affiche le nombre de sec depuis le 1er Janvier 1970

start=(time.time())#Enregistre le nombre de sec depuis le 1er Janvier 1970
time.sleep(2) #Fait une pause de 2 sec
fin=(time.time())#Enregistre le nombre de sec depuis le 1er Janvier 1970
print(f"{fin - start}Sec. entre les 2")#Fait une sousstraction pour avoir le temp entre les 2 variables


------------------------------------------------------------------------------------------------------------ Liste Conteneur ---------
List=["#1", "#2", "#3", 3, 124]

#La List ce modifie par elle même donc pas de copie
#Sauf pour import copy - List2 = copy.deepcopy (List)
print (List) #Afficher la list sur la memme ligne
for List1 in List:
	print(List1) #Afficher la list 1 élément apres l autre sur chaque ligne
print (List[2]) #Affiche le 2 élément à partir de 0
List.sort() #Mettre en ordre alphabétique
List.reverse() #Inversser la list de sens
List[3] = 4 #Change la valeur du 3eme élément à partir de 0
List.append ("Ajout") # Ajouter un élément dans la list au bout
List.insert(1, "AjoutEntre") # Ajouter un élément dans la list avant le 1er élément
del List [5] #Supprime le 5eme élément
List.remove("#2") #Supprime le nom de l'élément
print(List.count("#2")) # Affiche combien de fois le nom "#2" est dans la list 
List1 += List2 #Ne fait que 1 List dans List1 et List2 encore pareil
phrase= " ".join(List) # Transformer List en STR


------------------------------------------------------------------------------------------------------------ Dictionaire Conteneur ----- 
#Le dict ce modifie par lui même donc pas de copie
#Sauf pour faire une copie : dic2 = dic1.copy()
dicti = {"Ben":"c'est un nom", 24:768} #clef Ben et valeur c'est ...
print (dicti)#Afficher le dictionaire sur la memme ligne
print (dicti["Ben"]) # Affiche la valeur de Ben du dictionaire
dicti["ajout"] = "Description" # ajout au dicionaire ou modifier la descrition
dicti.pop("Ben") #Supprime le Ben du dictionaire ou del dicti["Ben"]
supprim=dicti.pop("Ben") #print supp affiche la valeur suprimer
for clef in dicti.keys(): #remplacer cle par values pour afficher les valeur, items pour afficher les 2
	print(clef)# Affiche les clef une a la suite


------------------------------------------------------------------------------------------------------------- Tuples Conteneur ---------
#Le tuple ce modifie ne se modifie pas
(tuuple)=(454, "ok") #pour 1 seul tuple (454,)
print (tuuple[1]) #Affiche le 1 élément à partir de 0 exeption si dépasse le nombre d élément

def getposition ():
	positionX= 24
	positionY= 355
	return (positionX, positionY)
poX, poY = getposition()
print(f"position {poX}/{poY}")


------- Input ----------------------------------------------------------------------------------------------- Input --------------------
VotreNom=input("Quel est votre nom : ") # Affiche la phrase à répondre par le client
print(f"Votre nom est : {VotreNom}")# Affiche la phrase + le résultat de l'utilisateur en mode Format

Prix=input("Je vais vous transformé un prix :") #Demande un prix avant Tx
Prix=float (Prix) #Transformation du "prix" en nombre décimal
PrixTx=Prix + Prix * 14.975/100 #Calcule de la taxe
print(f"Prix avec Tx :{PrixTx}") #Afficher le prix avec le calul en mode Format
#Ne pas oublier de faire des try en exception pour un utilisateur qui inscrie n'importe quoi


------------------------------------------------------------------------------------------------------------- Calcule Math -------------
import math
#import cmath pour plus de calcul poussé
num = 12.4

print ("Entier supérieur:{}".format(math.ceil(num)))
print ("Entier inférieur:{}".format(math.floor(num)))
print ("Racine carré:{}".format(math.sqrt(num)))
print ("Puissance:{}".format(math.pow(num)))
print ("Valeur absolue:{}".format(math.fabs(num)))
print ("Factoriel:{}".format(math.factorial(num)))
print ("Exponentiel:{}".format(math.exp(num)))
print ("Logarithme:{}".format(math.log2(num,)))#log nombre = la base
print ("Sinus:{}".format(math.sin(num)))
print ("Cosinus:{}".format(math.cos(num)))
print ("Tangante:{}".format(math.tan(num)))
print ("Arc Sinus:{}".format(math.asin(num)))
print ("Arc Tangante:{}".format(math.atan(num)))
print ("Arc Cosinus:{}".format(math.acos(num)))
print ("Degrée vers Radian:{}".format(math.radians(num)))
print ("Radian Vers degrée:{}".format(math.degrees(num)))

print ("PI:{}".format(math.pi))
print ("e:{}".format(math.e))

print ("Est-ce pas un nombre ?:{}".format(math.isnan(num)))#Réponse False si c'est un nombre


------------------------------------------------------------------------------------------------------------- Condition ----------------
# condition if / elif / else  -Il faut avoir fait saut de ligne et TAB
# <= Plus petit ou égal, != Différent de 
lettre="b" #Valeur de la variable choisi
if lettre in "aeiouy": #SI la valeur de lettre est dans "aeiouy" affiche en dessous
	print("C'est une voyelle")
else:#SINON la valeur de lettre n'est pas dans "aeiouy" affiche en dessous
	print("C'est une consonne")

age=35 #Valeur de la variable choisi
if age > 18: #SI la valeur de age est plus grande que la valeur 18, affiche en dessous
	print("Tu es majeur")
elif age == 18: #OU SI la valeur de age est égal que la valeur 18, affiche en dessous
	print("Tu es majeur")
else :#SINON , affiche en dessous
	print("Tu es mineur")

moteur=True #Valeur de la variable choisi ou False
if moteur : #SI la valeur est vrai, affiche en dessous
	print("C'est en marche")
else:#SINON , affiche en dessous
	print("Ne fonctionne pas")


------------------------------------------------------------------------------------------------------------- Exeption -----------------
# Les exeptions sont là pour dire au client quil na pas entré la bonne valleur (une lettre au lieu d un nombre) 
Nombre1=2 # Variable 1 ok 
Nombre2=input("Entré un nombre ? ")# Entré un nombre pour la 2 eme variable

try:
	Nombre2 = float(Nombre2) #On met la variable en nombre Float 0.X
	print("Réusultat = {} ".format(Nombre1 / Nombre2)) # On divise le nombre 1 par le nombre 2 choisix
except ZeroDivisionError: # Si le cilent met 0 comme 2 eme variable
	print(" Pas de Zéro dsl") # Il affiche ça fin du programme
except ValueError:# Si le cilent met une lettre comme 2 eme variable fin du programme
	print("Vous n'avez pas entré un nombre !!! ")# Il affiche ça
except:
	raise ZeroDivisionError("Message pour le cliant") #Je fait moi même lever l exception Zero et j'affiche un message
else:
	print("Voila votre résultat ci-haut") # Sinon affiche ça
finally:
	pass #ou print ... À la fin de tout les choix ci haut il fait cette fonction


------------------------------------------------------------------------------------------------------------- Fichier ------------------
import shutil  
import os
# R = Lire le fichier   W = écrire par dessus   A = Écrire pour ajouter       \n = Saut de ligne

f = open('/home/new-breed/Bureau/PYTHON/TESTE/6666.txt','x') #Créé un fichier.txt 

file = open('/home/new-breed/Bureau/PYTHON/TESTE/666.txt', "r") # Lire dans un fichier ligne par ligne
for line in file:
    print(line)
file.close()

with open ("/home/new-breed/Bureau/PYTHON/TESTE/666.txt", "a") as f: #Écrire d'un fichier
	f.write (" Écrire dans un fichier textes. \n" )
	f.close ()

Copyfil = shutil.copyfile('Liste.txt', '/home/new-breed/Bureau/PYTHON/TESTE/Liste.txt') #Faire une copy de fichier

shutil.copystat('/home/new-breed/Bureau/PYTHON/Liste.txt', '/home/new-breed/Bureau/666.txt')# Copier le data du fichier dans un autre
 
os.remove("/home/new-breed/Bureau/PYTHON/TESTE/6666.txt") # Supprimer un fichier


------------------------------------------------------------------------------------------------------------- Boucle -------------------
i = 0 #le i veut dire compteur  et le compteur est a 0 
Multiple = input("Nombre de répétition? ") # Entré un nombre de fois que lon veut voir le mot allo
M = int(Multiple) # Créé la variabl M qui est la variable Multiple en la mettant en nombre(int)

while i < M :      #i est plus petit que ( le chifrre voulue) Donc va à la fonction si bas
	print("allo")  # affiche le mot allo
	i += 1 #Additionne 1 au compteur

abc = True #Valeur True a abc
while abc: # Boucle de abc démarré, aller à la fonction
 	choix = input("votre choix:") # Fonction d'écrire un choix

 	if choix == "encore": # SI le choix est (encore), aller a la fonction
 		continue #Continuer recommence la Boucle
 	elif choix == "Quit": # OU SI le choix est (Quit), aller a la fonction
 		break #break Sortir la boucle
 	elif choix == "Fermer":# OU SI le choix est (Fermer), aller a la fonction
 		abc = False # Change la variable True vers False, ce qui fait qu'il n'entre pas dans la boucle
 	else: #SINON , aller a la fonction
 		print("blablabla") #Affiche blablabla et repart la boucle
print("Fin") #Affiche Fin à la fin de la boucle


cba="allo" # Valeur de la Variable
for af in cba: # Ouvrir la boucle af dans la variable cba (allo) lettre par lettre 
	print(af) #Afficher la variable af=cba=allo afficher a reboucler l reboucler l reboucler o 

liste = [1,5,10,15,20] #Valeur de la liste
for i in liste:	# Ouvrir la boucle i dans la liste
	if i > 15: #Si i est plus petit que 15(un indice a la fois) va a la fonction (print i) Si plus grad que 15 Va la fonction (print et Break)
		print("On stoppe la boucle") #Afficher le mot
		break #Break sortir de la boucle
	print(i) #Afficher la valleur i (les nombres plus petits que 15 dans la liste)


------------------------------------------------------------------------------------------------------------- Fonction -----------------
#mettre les fonctions en haut du programme en dessous des import et des variables
def allo(): #Création de la Fonction(def) allo
	print ("Allo tout le monde") #Si la fonction est appeller affiche("allo tout le monde")

allo()#Pour démarré la fonction

print(allo()) # Affiche la fonction ET le return et si pas de return sa va donner none

def calcule (nomb1, nomb2): #Fonction, parametre  de 2 variables
	return nomb1 + nomb2 # Va retourné un calcul de nomb1 et nomb2
print (calcule(4, 7)) #Afficher la fontion, et donner les valeurs au variable														

# Les splat * ou Double ** dans les fonctions
def bar(**kwargs):# Fonction, ** Bibliothèque en dessous de la fonction
    for a in kwargs: # boucle for pour afficher un élément par ligne
        print(a, kwargs[a])  # Affiche les éléments a (premier), qui est la clef et Kwargs[a](2eme) est le rendu de la clef 
bar(name="Ben", age=27)# Varible avec c'est paramètre version (bibliothèque) 

def foo(*args):# Fonction, * pour dire qu il a un nombre infini de paramètre dans une variabl foo (tuple) en dessous de la fonction
    for a in args: # boucle for pour afficher un élément par ligne
        print(a)   # Affiche les éléments des items dans foo     
foo(1,2,3) # Les paramètres dans la variable, on peu en ajouter et en enlever comme on le veux (1,2,3,4,5,6,)

def Inventaire (*listeitems): # Fonction, * pour dire qu il a un nombre infini de paramètre dans une variable Inventaire (tuple)
	for item in listeitems: # boucle for pour afficher un élément par ligne
		print (item) # Affiche les éléments des items dans Inventaire
Inventaire("roche",) # roche est dans l inventaire (mettre aprÈs la fonction)
Inventaire("fenetre", "clavier", 20, 3.4)# item qui sont dans l inventaire
------------------------------------------------------------------------------------------------------------- Global -------------------
#Pour la variable a le global est mis dans la fonction et le print est après à l'extérieur de la fonction. 
a = 2

def test():
    global a
    a = 3
    print("intérieur de test", a)

test()
print("après test", a)


------------------------------------------------------------------------------------------------------------- "lambda" -----------------
fonction = lambda : print ("allo") # Mettre une fonction dans la variable lambda 

add_one = lambda x: x + 1
add_one(2)

"""(lambda x: x + 1)(2) = lambda 2: 2 + 1
                     = 2 + 1
                     = 3
"""

------------------------------------------------------------------------------------------------------------- Décorateur ------------------
#Ajout d'une variable décoratuer  qui relance la fonction  sans toucher au code principal et pour ne pas faire de doublon.

def decorator (func):#Ajout d'une fonction
	print("Rajout de text") # Text a rajouter ou a doubler en affichage
	return func #Renvois la fonction de print

@decorator
def hello(): #Fonction STD pour afficher hello
	print("hello")#Affche hello

hello=decorator(hello) # OU Ajout du décorateur + la fonctione hello dans la variable hello (à la place du @ )

def allo(): #Fonction STD pour afficher allo
	print("Allo")#Affche allo

hello() #Démarre la fonction
allo() #Démarre la fonction


------------------------------------------------------------------------------------------------------------- Asynchrone ---------------
import time 
import threading

def un (): #Fonction pour faire afficher 3x 11111 avec un interval de .5 seconde entre chaque
	i=0
	while i<3:
		print("1111")
		time.sleep(0.5)
		i+=1
def deux (): #Fonction pour faire afficher 3x 22222 avec un interval de .5 seconde entre chaque
	i=0
	while i<3:
		print("2222")
		time.sleep(0.5)
		i+=1

th1=threading.Thread(target=un) # Dire au variable de ce mettre en thread dans la variable th1
th2=threading.Thread(target=deux) # Dire au variable de ce mettre en thread dans la variable th2

th1.start() # Démarré la variable th1
th2.start() # Démarré la variable th2

th1.joint() #Quand la Fonction se termine en premier que ce soit th1 ou th2, elle va attendre l'autre pour continuier par la suite 
th2.joint() #Quand la Fonction se termine en premier que ce soit th1 ou th2, elle va attendre l'autre pour continuier par la suite 


------------------------------------------------------------------------------------------------------------- HTTP Serveur -------------
# Pour faire un serveur fichier ne pas mettre dans le même dossier que celui du web. ou en créé 2 (1 en 8000 et l'autre en 80 pour le Web)
#Ouvrir une page web et inscrire localhost/192.168.1.103 ou seulement localhost si rien inscrie dans l'adresse

#coding:utf-8
import http.server
import socketserver

port=8000
address=("192.168.1.103", port) # L'adresse IP peux être variable ou pas en mettre pour juste appeller le localhost seulement

handler=http.server.SimpleHTTPRequestHandler
httpd=socketserver.TCPServer(address, handler)

print(f"Serveur start sur port {port}")
httpd.serve_forever()
---------------------
#Méthode avec CGI

#coding:utf-8
import http.server

port=80
address=("", port) # L'adresse IP peux être variable ou pas en mettre pour juste appeller le localhost seulement

server=http.server.HTTPServer
handler=http.server.CGIHTTPRequestHandler
handler.cgi_directories=["/"] #Pour un fichier index.py créé dans le même dossier
httpd=server(address, handler)

print(f"Serveur start sur port {port}")
httpd.serve_forever()
----------------------
#Autre fichier.py pour la page html en CGI
#Faire attention pour que le CGI ne fonctionne pas directement avec la version pour faire rouler les Linux (exemple 2.7) "Format error"
----------------------
#! /usr/bin/python3.7 #Ligne pour utiliser la version 3.7 sur un kernel qui roule en 2.7 
#coding:utf-8
import cgi

print("Content-type: text/html; charset=utf-8\n") # Pour lui dire de lire un fichier html avec python avec l'unicode utf-8

html= """<!DOCTYPE html>
<Écrire toute le code html std>
"""
print("html") #Affiche la variable qui a tout le html


------------------------------------------------------------------------------------------------------------- Formulaire ---------------
#Faire fichier pour le Serveur CGI
#Faire un fichier python avec HTML pour le formulaire
#Faire un fichier python de résultat
																-------------JE SUIS RENDU ICI ---------XXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXX


------------------------------------------------------------------------------------------------------------- Cookies ------------------
																-------------JE SUIS RENDU ICI ---------XXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXX


------------------------------------------------------------------------------------------------------------- Socket -------------------
#Pour le socket, c'est pour connecter des machine entre elle. 
#1 fichier serveur pour démarré le serveur et un autre fichier pour faire le client qui se connecte au serveur
import socket

host, port = ('', 5566)#Lui attribu un adresse et un port pour se connecter

socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Création d'un socket
socket.bind((host, port))# On lui donne son adresse et son port de connection
print("Serveur en fonction") #On affiche

while True: # Boucle infini
	socket.listen(5) # 5 possibilité de se connecter en échouant avant d arretter
	conn, adress = socket.accept()# Accepter les connections
	print("Un Client vien de se connecter")#Afficher

	data = conn.recv(1024) #Pour recevoir les donner
	data = data.decode("utf8") # Pour décoder les donner
	print(data)#Pour afficher les donner

conn.close() #Fermer la connection
socket.close() #Fermer le socket

-----------------
import socket

host, port = ('localhost', 5566)#Lui attribu un adresse et un port pour se connecter
socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Création d'un socket
try:
	socket.connect((host, port))#Création d'un socket pour se connecter
	print("Client connecté") # Affiche
	data = input(" Ditte quelque chose : ") # Création d'un input pour mettre l info dans une variable
	data = data.encode("utf8")#Encoder cette variable en utf8
	socket.sendall(data)#Enovyer toute les donner vers lautre socket (serveur)
except:#Si sa marche pas
	print("Connection de Marde") # Affiche
finally: # Fait si oui et même si except
	socket.close()#Fermeture du socket


------------------------------------------------------------------------------------------------------------- Base de données ----------
+TUTO															-------------JE SUIS RENDU ICI ---------XXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXX


------------------------------------------------------------------------------------------------------------- Class --------------------

class Humain(): #Création d'une class Humain
	def __init__(self, Prenom, Age): #La class humain comporte Toujours __inti__ et self on ajout prénom et Age comme parametre de l'objet
		self.Age = Age #Lui même se donne l age
		self.Prenom = Prenom #Lui même se donne le nom

	def afficher():
		print ("Bonjour {} ton {} ans te va très bien.".format(H1.Prenom, H1.Age)) # On affiche
		print("ET")# On affiche
		print ("Bonjour {} ton {} ans te va très bien.".format(H2.Prenom, H2.Age)) # On affiche 

print(" ---- Il a 2 Joueurs ----") # On affiche

VotreNom1=input("Quel est le nom du premier joueur : ")  # On demande et on affiche
AAge1=input(" Et votre âge : ") # On demande et on affiche
H1 = Humain (VotreNom1, AAge1) #Création d'un objet humain avec les 2 parametres son nom et son age

VotreNom2=input("Quel est le nom du deuxième joueur : ") # On demande et on affiche
AAge2=input(" Et votre âge : ") # On demande et on affiche
H2 = Humain (VotreNom2, AAge2) #Création du 2eme objet humain avec les 2 parametres son nom et son age

Humain.afficher() 

#Il a aussi la méthode de parent enfant ()
class Homme(Humain):
	def __init__(self, Prenom, Age, Gabarit):
		Humain.__init__(self, Prenom, Age)
		self.Gabarit=Gabarit

VotreNom1=input("Quel est le nom du premier joueur : ")  # On demande et on affiche
AAge1=input(" Et votre âge : ") # On demande et on affiche
Gab1=input("Gabari?")
H1 = Homme (VotreNom1, AAge1, Gab1) #Création d'un objet humain avec les 2 parametres son nom et son age

print ("Bonjour {} ton {} ans te va très bien par ce que tu es {}.".format(H1.Prenom, H1.Age, H1.Gabarit)) # On affiche

-------------------------------------------------
#Aussi Méthode d'encapsulation (getter et setter)

class Humain(): #Création d'une class Humain
	def __init__(self, Prenom, Age): #La class humain comporte Toujours __inti__ et self on ajout prénom et Age comme parametre de l'objet
		print("Création d'un humain")
		self.Age = Age #Lui même se donne l age
		self._Prenom = Prenom #Lui même se donne le nom Voir le _ avant veux dire Encapsulation

	def _getPrenom(self): #Fonction get de lui même
		if self._Prenom == "Ben": #Si son Prénom est Ben
			return f"{self._Prenom} est vieux de"  #Affiche Est vieux après son prénom
		else: # Sinon 
			return f"{self._Prenom} a l'age de"#Affiche a lage de après son prénom

	Prenom = property(_getPrenom) #On ajoute l'option get (dans la class)

H1 = Humain("Ben", 35)#Création d'un objet humain avec les 2 parametres son nom et son age

print(f"{H1.Prenom} {H1.Age} ans.") # On affiche


------------------------------------------------------------------------------------------------------------- tkinter -----------------
							+TUTO									-------------JE SUIS RENDU ICI ---------XXXXXXXXXXXXXXXXXXXXXXX
Variable controle, menu, positionnement, widjet
XXXXXXXXXXXXXXXXXXXXXXX


import tkinter

def Quit (): #Fonction de fermer programme
	exit()

#Fonction pour bouton ON
def LedBleuOn ():
	print("Buzz ON") #On affiche dans la console

#Fonction pour bouton OFF
def LedBleuOff ():
	print("Buzz OFF")  #On affiche dans la console

Fenetre = tkinter.Tk() #Création de la fenêtre
Fenetre.title("Programme de Buzz") # Titre de la fenetre
Fenetre.geometry("575x220") #Dimention fenetre

 #Bouton pour ON
Ok = tkinter.Button(Fenetre, text="Buzz - ON ", command=LedBleuOn)
Ok.place(x=10,y=30)

#Bouton pour OFF 
Ok = tkinter.Button(Fenetre, text="Buzz - OFF ", command=LedBleuOff)
Ok.place(x=410,y=30)

#Bouton pour Fermer
Ok = tkinter.Button(Fenetre, text="QUITTER", command=Quit)
Ok.place(x=210,y=160)

#Maintient de la fenetre en loop
Fenetre.mainloop()


import tkinter
#module pour message erreur
from tkinter import messagebox
from tkinter import *

def ok():
	messagebox.showinfo("ok", "OKKKK")


#Former une fenetre
Fenetre = tkinter.Tk()
Fenetre.title("Teste Widgets") # titre de la fenetre
Fenetre.geometry("1080x720") # dimention fenetre

# case pour entrer une donner
EnterDonner = tkinter.Entry(Fenetre) #, show="*") pour afficher cacher
EnterDonner.pack() # alligner dans le visuel

#boutton OK  et , relief=RIDGE change le visuel 
Ok = tkinter.Button(Fenetre, text="OK", relief=RIDGE, command=ok)
Ok.pack()

#piton choix d'option
check1 = tkinter.Radiobutton(Fenetre, text=" Homme", value=1)
check2 = tkinter.Radiobutton(Fenetre, text=" Femme", value=0)
check1.pack()
check2.pack()

#piton à cocher pour option
chek3 = tkinter.Checkbutton(Fenetre, text=" Majeur ?", offvalue=0, onvalue=1)
chek3.pack()

#dimmer pour volume etc.
dimmer = tkinter.Scale(Fenetre)
dimmer.pack()

#Liste a sélectioner a vue 
liste = tkinter.Listbox(Fenetre)
liste.insert(1, "Windows")
liste.insert(2, "Linux")
liste.insert(3, "MacOS")
liste.pack()

#afficher message erreur ou voulez vous supprimer?
def erreur():
	messagebox.showerror("ERREUR", "Voila une erreur !")
	# showinfo - showwarning - askquestion (oui non) - askokcancel (ok annuler) - askyesno - askretrycancel

#création d'un piton erreur
Bouton = tkinter.Button(Fenetre, text="Erreur !!!", command=erreur)
Bouton.pack()

#changer le curseur dessu le piton
Button(Fenetre, text ="spider", relief=RAISED, cursor="spider").pack()



# fonction appellée lorsque l'utilisateur presse une touche
def clavier(event):
    global coords

    touche = event.keysym

    if touche == "Up":
        coords = (coords[0], coords[1] - 10)
    elif touche == "Down":
        coords = (coords[0], coords[1] + 10)
    elif touche == "Right":
        coords = (coords[0] + 10, coords[1])
    elif touche == "Left":
        coords = (coords[0] -10, coords[1])
    # changement de coordonnées pour le rectangle
    canvas.coords(rectangle, coords[0], coords[1], coords[0]+25, coords[1]+25)

# création du canvas
canvas = tkinter.Canvas(Fenetre, width=250, height=250, bg="ivory")
# coordonnées initiales
coords = (0, 0)
# création du rectangle
rectangle = canvas.create_rectangle(0,0,25,25,fill="violet")
# ajout du bond sur les touches du clavier
canvas.focus_set()
canvas.bind("<Key>", clavier)
# création du canvas
canvas.pack()



#Tenir la loop fenetre ouverte
Fenetre.mainloop()



from tkinter import *

# - - - - - - - - - - - - - - - - - -

# Déclarations des fonctions utilisées

# - - - - - - - - - - - - - - - - - -

def afficherValeur() :

    valeur = curseur1.get()

    monAffichage.configure(text = valeur)

# - - - - - - - - - - - - - - - - - -

# Création de la fenêtre et des objets associés la fenêtre

# - - - - - - - - - - - - - - - - - -

fen_princ = Tk()

# Création d'un Scale nommé curseur1

curseur1 = Scale(fen_princ, from_ = -20, to = 300)

curseur1.pack()

# Création d'un Label nommé monAffichage

monAffichage = Label(fen_princ, text = "C'est ici qu'on affichera le résultat du Scale", width=70)

monAffichage.pack()

# Création d'un Button lancant la fonction afficherValeur()

monBouton = Button(fen_princ, text = "Récupérer la valeur du curseur", command = afficherValeur)

monBouton.pack()

# - - - - - - - - - - - - - - - - - -

# Bouclage de la fenêtre fen_princ

# - - - - - - - - - - - - - - - - - -

fen_princ.mainloop()


from tkinter import *                                                    #1
                                                                           #2
fen = Tk()                                                                 #3
fen.title("Fenêtre composée à l'aide de frames")                           #4
fen.geometry("300x300")                                                    #5
                                                                           #6
f1 = Frame(fen, bg = '#80c0c0')                                            #7
f1.pack(side =LEFT, padx =5)                                               #8
                                                                           #9
fint = [0]*6                                                               #10
for (n, col, rel, txt) in [(0, 'grey50', RAISED, 'Relief sortant'),        #11
                           (1, 'grey60', SUNKEN, 'Relief rentrant'),       #12
                           (2, 'grey70', FLAT, 'Pas de relief'),           #13
                           (3, 'grey80', RIDGE, 'Crête'),                  #14
                           (4, 'grey90', GROOVE, 'Sillon'),                #15
                           (5, 'grey100', SOLID, 'Bordure')]:              #16
    fint[n] = Frame(f1, bd =2, relief =rel)                                #17
    e = Label(fint[n], text =txt, width =15, bg =col)                      #18
    e.pack(side =LEFT, padx =5, pady =5)                                   #19
    fint[n].pack(side =TOP, padx =10, pady =5)                             #20
                                                                           #21
f2 = Frame(fen, bg ='#d0d0b0', bd =2, relief =GROOVE)                      #22
f2.pack(side =RIGHT, padx =5)                                              #23
                                                                           #24
can = Canvas(f2, width =80, height =80, bg ='white', bd =2, relief =SOLID) #25
can.pack(padx =15, pady =15)                                               #26
bou =Button(f2, text='Bouton')                                             #27
bou.pack()                                                                 #28
                                                                           #29
fen.mainloop()  

------------------------------------------------------------------------------------------------------------- Pygame ------------------
																-------------JE SUIS RENDU ICI ---------XXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXX


------------------------------------------------------------------------------------------------------------- Pack PIP ----------------
#Ouvrir la mode commande administrateur ou sudo.
python3 -m pip install --upgrade pip # Mettre le logiciel pip à jour (pas de 3 si windows)
pip freeze > packtage.txt # Pour connaitre les packtage de pip déja installer et les mettre dans fichier.txt
https://pypi.org/ # Le site pour voir les packtages 
pip search XXX > resultats.txt #Pour faire une recherche directement dans la consol et pour le mettre dans un fichier.txt
pip install -r packtage.txt #Installer toutes les packtages d'une shoot qui sont dans le fichier.txt
pip install XXX # Le nom du pack sans la version pour l'installer
pip uninstall XXX # Le nom du pack sans la version pour le déinstaller
pip show XXX # Pour connaitre l'info du packtage


------------------------------------------------------------------------------------------------------------- Exécutable --------------
# Créé un fichier exécutable dans un dossier
python3 -m pip install cx_Freeze --upgrade # Dans console pour installer et mettre a jour le packtage pour créé des .exe
Créé un fichier setup.py # Ouvrir python et enregistré un fichier seul renommer setup.py

from cx_Freeze import setup, Executable # Dans le programme python la bibliothèque

setup(
	name="Nom De Mon Programme",
	version="0.1",
	descrition="Description du programme",
	executables=[Executable("NOM.py, 2EMENOM.py")]#Nom du programme à mettre en exécutable et un 2eme si il y a. )

python3 setup.py build # Mettre en commande dans console pour démarré le programme et compiler le tout
# Ça créé un Dossier avec les fichiers, dont ceux pour .exe
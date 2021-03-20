#coding:utf-8
import os
import myClassData as ToolsData #pylint: disable=import-error
import messageAfficher as message #pylint: disable=import-error
import fonctionPackage as fonc #pylint: disable=import-error

message.MessageAcceuil()

reponse = True
while reponse == True:
    print("Bonsoir qu'es ce que vous voulez faire ?")
    choix = input("1 --> Ajoutez une tache \t 2 --> Affichez les tache \n3 --> Supprimer une tache \t 4 --> Modifier une tache \n*****Votre Choix : ")
    choix = int(choix)
    try:
        if choix != 1 and choix != 2 and choix != 3 and choix != 4:
            raise ValueError("Choix incombatible")
        if (choix == 1) or (choix == 2) or (choix == 3) or (choix == 4):
            if choix == 1:
                fonc.CreateToDoList()
            elif choix == 2:
                fonc.ReadToDoList()
            elif choix == 3:
                fonc.ReadToDoList()
                a = input("Print entrez le numero de la tache a supprimer : ")
                a = int(a)
                fonc.DeleteTodoList(a)
            else:
                fonc.ReadToDoList()
                a = input("Print entrez le numero de la tache a Modifier")
                a = int(a)
                fonc.UpdateToDOList(a)
    except ValueError:
        print("Erreur : ")

        



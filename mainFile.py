#coding:utf-8
import os
import ToolsData.fonctionPackage as fonc
import ToolsData.myClassData as data
import ToolsData.messageAfficher as message

message.MessageAcceuil()

reponse = False
while reponse:
    print("Bonsoir qu'es ce que vous voulez faire ?")
    choix = input("1 --> Ajoutez une tache \t 2 --> Affichez les tache \t 3 --> Supprimer une tache \t 4 --> Modifier une tache ")
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
                a = input("Print entrez le numero de la tache a supprimer")
                a = int(a)
                fonc.DeleteTodoList(a)
            else:
                fonc.ReadToDoList()
                a = input("Print entrez le numero de la tache a Modifier")
                a = int(a)
                fonc.UpdateToDOList(a)
    except ValueError:
        print("Erreur : ")



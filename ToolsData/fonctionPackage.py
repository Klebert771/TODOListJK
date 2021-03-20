#coding:utf-8
import myClassData as data
import messageAfficher as message
import datetime

toDoListObject = data.ToDoList()

def CreateToDoList():
    message.CreationListToDoList()
    toDoListObject.nomToDo = input("Entrez un titre à votre tâche : ")
    toDoListObject.nomToDo = str(toDoListObject.nomToDo)
    toDoListObject.libelleToDo = input("Entrez un Libellez à votre tâche : ")
    toDoListObject.libelleToDo = str(toDoListObject.libelleToDo)
    toDoListObject.dateCreate = datetime.date.today()
    toDoListObject.dateRunHeure =  GetDateToDoList()
    message.AcceptSave()
    SaveToDoList(toDoListObject)

def SaveToDoList(toDoListObject):
    ToDoListSave = open("toDoListData.txt", "a")
    ListeDonner = str("{} ** {} ** {} ** {} ** {}.".format(toDoListObject.id, toDoListObject.nomToDo, toDoListObject.libelleToDo, toDoListObject.dateCreate, toDoListObject.dateRunHeure))
    try:
        ToDoListSave.write(ListeDonner)
    except:
        print("Enregistrement Echouer")
    ToDoListSave.close()

def ReadToDoList():
    ToDoListSave = open("toDoListData.txt", "r")
    Ligne = ToDoListSave.readlines()
    N_lignes = len(Ligne)
    print("Il y'a {} tâche(s)".format(N_lignes))
    if N_lignes == 0:
        print("Il n'y'a aucune tache disponible")
    else:
        for line in Ligne:
            print(line)

    ToDoListSave.close()

def UpdateToDOList(identifiant):
    ToDoListSave = open("toDoListData.txt", "a")
    Ligne = ToDoListSave.readlines()
    trouver = False
    for line in Ligne:
        if identifiant in line:
            try:
                toDoListObject.nomToDo = input("Entrez un titre à votre tâche")
                toDoListObject.nomToDo = str(toDoListObject.nomToDo)
                toDoListObject.libelleToDo = input("Entrez un Libellez à votre tâche")
                toDoListObject.libelleToDo = str(toDoListObject.libelleToDo)
                toDoListObject.dateCreate = datetime.date.today()
                toDoListObject.dateRunHeure =  GetDateToDoList()
                message.AcceptSave()
                SaveToDoList(toDoListObject)
                trouver = True
            except:
                print("Erreur de lors de la modification")
    if trouver:
        print("Modification effectuer avec succes")
    else:
        print("Aucun tache avec cette indice n'a ete retrouver")

def DeleteTodoList(identifiant):
    ToDoListSave = open("toDoListData.txt", "a")
    Ligne = ToDoListSave.readlines()
    supprimer = False
    for line in Ligne:
        if identifiant in line:
            try:
                ToDoListSave.write("\r\n".join(line))
                supprimer = True
            except:
                print("Erreur de lors de la suppression")
    if supprimer:
        print("Suppression effectuer avec succes")
    else:
        print("Aucun tache avec cette indice n'a ete retrouver")

def SearchToDoList(identifiant):
    ToDoListSave = open("toDoListData.txt", "r")
    Ligne = ToDoListSave.readlines()
    trouver = False
    for line in Ligne:
        if identifiant in Ligne:
            try:
                print(line)
                trouver = True
            except:
                print("Erreur de lors de la recherche")
    if trouver:
        print("recherche effectuer avec succes")
    else:
        print("Aucun tache avec cette indice n'a ete retrouver")

def GetDateToDoList():
    A = input("Entrez l'année : ")
    A = int(A)
    M = input("Entrez le mois : ")
    M = int(M)
    d = input("Entrez le Jour : ")
    d = int(d)
    DateJour = str("{}-{}-{}".format(A, M, d))
    return DateJour
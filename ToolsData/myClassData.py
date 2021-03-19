#coding:utf-8
import datetime

class ToDoList:
    id = 0

    def __init__(self):
        self.id += 1 
        self.nomToDo = "List"
        self.libelleToDo = "Ceci est une tâche"
        self.dateCreate = datetime.date.today()
        self.dateRunHeure = datetime.date.today()


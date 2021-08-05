#!/usr/bin/env python3
import pickle
class Employee: #объявление класса

    def __init__(self, name, emp_id, dept):  #Инициализация объекта
        self.name = name
        self.emp_id = emp_id
        self.dept = dept

    def __str__(self) -> str:
        return "Name: {}\nEmp_id: {}\nDepartment: {}".format( #Оформление объекта
                self.name,
                self.emp_id,
                self.dept
            )

    def __setstate__(self, state: dict): #Данная функция нужна для восстановления класса
        self.name = state["name"]
        self.emp_id = state["emp_id"]
        self.dept = state["dept"]

with open("./ouput.bin","rb") as f:  #Открываем биннарный файл
    emp1=pickle.load(f)
    print(emp1) #Выводим результат в виде карточки сотрудника Mary

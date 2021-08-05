#!/usr/bin/env python3
import pickle
class Employee: #Объявление класса

    def __init__(self, name, emp_id, dept): #Инициализация объекта
        self.name = name
        self.emp_id = emp_id
        self.dept = dept

    def __str__(self) -> str:  #Оформление объекта
        return "Name: {}\nEmp_id: {}\nDepartment: {}".format(
                self.name,
                self.emp_id,
                self.dept
            )

    def __getstate__(self) -> dict: #Данная функция нужна для сохранения класса
        state = {}
        state["name"] = self.name
        state["emp_id"] = self.emp_id
        state["dept"] = self.dept
        return state

emp1 = Employee("Mary", 512, "DBA")
ser=pickle.dumps(emp1)
with open("ouput.bin","wb") as f: #Сохраняем карточку сотрудника Mary класса Employee в биннарный файл
    pickle.dump(emp1,f)

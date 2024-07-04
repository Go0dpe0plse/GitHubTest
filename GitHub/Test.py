print("Вітаю вас в програмі для створення списку студентів")
student = ["Vasya"]
while True:
    choise = int(input("1-Додати студента\n2-Видалити студента\n3-показати студентів\n"))
    if choise == 1:
        newStudent = input("Введіть нового студента")
        student.append(newStudent)
    if choise == 2:
        choiceForRemove = input("Введіть ім'я студента якого хочете видалити")
        student.remove(choiceForRemove)
    if choise == 3:
        for item in student:
            print(item)




import csv
from random import choice


def add_student():
    with open("final_grades.csv","a",encoding="utf-8") as f:
        name = input("Student's name? ")
        grade = input("Grade? ")
        f.write(f"{name},{grade}\n")

def show_all():
    with open("final_grades.csv","r",encoding="utf-8") as f:
        reader = csv.reader(f)
        print("student's list: ")
        for row in reader:
            print(f"{row[0]} - grade: {row[1]}")

def show_avg():
    with open("final_grades.csv","r",encoding="utf-8") as f:
        reader = csv.reader(f)
        grades = [int(row[1]) for row in reader]
        avg = sum(grades) / len(grades)
        print("Grades average: ", avg)

while True:
    print("\n1.Add a student")
    print("2.View list")
    print("3.Calculating the average")
    print("4.Exit")
    choice = input("your choice?")
    if choice == "1":
        add_student()
    elif choice == "2":
        show_all()
    elif choice == "3":
        show_avg()
    elif choice == "4":
        break
    else:
        print("The option is invalid!")
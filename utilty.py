
import pyodbc
import colorama
from colorama import Fore, Style, Back
colorama.init(autoreset=True)

from DB import Database


class Bible(Database):
    def __init__(self):
        super().__init__()

    def bible_questions(self):
        option = 'select Question, A, B, C, D, Answer from Bible'
        self.cursor.execute(option)
        score = 0
        for choice in self.cursor:
            print(choice[0])
            print(choice[1])
            print(choice[2])
            print(choice[3])
            print(choice[4])

            answer = input("choice one of them: ")

            if answer == choice[5]:
                score += 1
            print("you got ", str(score), "/", "6", "correct")


class Maths(Bible):

    def maths_question(self):
        option = 'select Question, A, B, C, D, Answer from Maths'
        self.cursor.execute(option)
        score = 0
        for choice in self.cursor:
            print(choice[0])
            print(choice[1])
            print(choice[2])
            print(choice[3])
            print(choice[4])

            answer = input("choice one of them: ")

            if answer == choice[5]:
                score += 1
            print("you got ", str(score), "/", "6", "correct")


class Football(Bible):

    def football_question(self):
        option = 'select Question, A, B, C, D, Answer from Football'
        self.cursor.execute(option)
        score = 0
        for choice in self.cursor:
            print(choice[0])
            print(choice[1])
            print(choice[2])
            print(choice[3])
            print(choice[4])

            answer = input("choose the correct one: ")

            if answer == choice[5]:
                score += 1
            print("you got ", str(score), "/", "6", "correct")



conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-P5U7S83P;'
                      'Database=Trivial_game;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

def data_entry():
    id_person = int(input(Fore.LIGHTMAGENTA_EX + "Enter your Personal_ID: "))
    last_name = input(Fore.LIGHTMAGENTA_EX + "Enter your last name: ")
    first_name = (input(Fore.LIGHTMAGENTA_EX + "Enter your first name: "))
    score = int(input(Fore.LIGHTMAGENTA_EX + "Enter your score out of 6: "))
    cursor.execute("INSERT INTO Persons (PersonID,LastName,FirstName,Score) VALUES(?, ?, ?, ?)",(id_person, last_name,first_name,score))
    conn.commit()
# data_entry()

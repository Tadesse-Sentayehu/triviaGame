
from app import Catagory


if __name__ == "__main__":
    Catagory


















































# import pyodbc
#
# from DB import Database
#
#
# class Bible(Database):
#     def __init__(self):
#         super().__init__()
#
#     def bible_questions(self):
#         option = 'select Question, A, B, C, D, Answer from Bible'
#         self.cursor.execute(option)
#         score = 0
#         for choice in self.cursor:
#             print(choice[0])
#             print(choice[1])
#             print(choice[2])
#             print(choice[3])
#             print(choice[4])
#
#             answer = input("choice one of them: ")
#
#             if answer == choice[5]:
#                 score += 1
#             print("you got ", str(score), "/", "6", "correct")
#
#
# class Maths(Bible):
#
#     def maths_question(self):
#         option = 'select Question, A, B, C, D, Answer from Maths'
#         self.cursor.execute(option)
#         score = 0
#         for choice in self.cursor:
#             print(choice[0])
#             print(choice[1])
#             print(choice[2])
#             print(choice[3])
#             print(choice[4])
#
#             answer = input("choice one of them: ")
#
#             if answer == choice[5]:
#                 score += 1
#             print("you got ", str(score), "/", "6", "correct")
#
#
# class Football(Bible):
#
#     def football_question(self):
#         option = 'select Question, A, B, C, D, Answer from Football'
#         self.cursor.execute(option)
#         score = 0
#         for choice in self.cursor:
#             print(choice[0])
#             print(choice[1])
#             print(choice[2])
#             print(choice[3])
#             print(choice[4])
#
#             answer = input("choose the correct one: ")
#
#             if answer == choice[5]:
#                 score += 1
#             print("you got ", str(score), "/", "6", "correct")
#
#
#
# class Catagory(Football):
#     list = ['b', 'm', 'f']
#     while True:
#         user_choice = input("Chose the a category you want?\n"
#                       "b = for Bible \n"
#                       "f = for Football\n"
#                       "m = for Maths\n"
#                       "choose here : ")
#         if user_choice == list[0]:
#             u = Bible()
#             u.bible_questions()
#         elif user_choice == list[1]:
#             i = Maths()
#             i.maths_question()
#         elif user_choice == list[2]:
#             a = Football()
#             a.football_question()
#         con = input("Do you want to stop:")
#         if con == "yes":
#             break
#
#
#
#
# Catagory()


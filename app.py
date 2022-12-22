
from utilty import Bible
from utilty import Maths
from utilty import Football
from utilty import data_entry

class Catagory(Football):
    list = ['b', 'm', 'f']
    while True:
        user_choice = input("Chose the a category you want?\n"
                      "b = for Bible \n"
                      "f = for Football\n"
                      "m = for Maths\n"
                      "choose here : ")
        if user_choice == list[0]:
            u = Bible()
            u.bible_questions()
        elif user_choice == list[1]:
            i = Maths()
            i.maths_question()
        elif user_choice == list[2]:
            a = Football()
            a.football_question()
        data_entry()
        con = input("Do you want to stop:")
        if con == "yes":
            break


# Catagory()
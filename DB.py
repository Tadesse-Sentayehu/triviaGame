import pyodbc


class Database():

    def __init__(self):
        connect = pyodbc.connect('Driver={SQL Server};'
                                 'Server=LAPTOP-P5U7S83P;'
                                 'Database=Trivial_game;'
                                 'Trusted_Connection=yes;')

        self.cursor = connect.cursor()
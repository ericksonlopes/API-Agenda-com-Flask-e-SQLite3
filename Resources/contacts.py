from flask_restful import Resource
import sqlite3
import os


class DataBase:
    def __init__(self):
        self.name_file = 'database.db'
        if not os.path.exists(self.name_file):
            try:
                connection = sqlite3.connect(self.name_file)
                cursor = connection.cursor()
                cursor.execute('CREATE TABLE contacts(name TEXT, telephone TEXT)')
                connection.close()
            except Exception as err:
                print(err)
                os.remove(self.name_file)

    def add_data(self, name, telephone):

        connection = sqlite3.connect(self.name_file)
        cursor = connection.cursor()
        cursor.execute(f"insert into contacts values('{name}', '{telephone}')")
        connection.commit()
        connection.close()

    def find_select(self):
        connection = sqlite3.connect(self.name_file)
        cursor = connection.cursor()
        cursor.execute('select rowid, * from contacts')
        dados = cursor.fetchall()
        dicio = []
        for item in dados:
            dicio.append(dict(id=item[0], name=item[1], telephone=item[2]))
        return dicio


class Contacts(Resource):
    def get(self):
        db = DataBase()
        return {'Contacts': db.find_select()}


class Contact(Resource):
    def get(self):
        db = DataBase()
        for item in db.find_select():
            


    def post(self):
        pass

    def put(self):
        pass

    def delete(self, id_contact):
        pass

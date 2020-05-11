from flask import Flask
from flask_restful import Api
from Resources.contacts import Contacts, Contact


app = Flask(__name__)
api = Api(app)

api.add_resource(Contacts, "/contacts")
api.add_resource(Contact, '/contacts/<string:name>')

if __name__ == '__main__':
    from Resources.contacts import DataBase
    app.run()
    # db = DataBase('')
    # db.add_data('Erickson', '11943604897')
    # db.find_select()

from flask import Flask
from flask_restful import Api
from Resources.contacts import Contacts, Contact

# Especificando que o flask irá usar esse arquivo
app = Flask(__name__)
# Especificando que será um API
api = Api(app)

# Adicionando Recursos, e como podem ser chamados
api.add_resource(Contacts, "/contacts")
api.add_resource(Contact, '/contacts/<string:name>')

if __name__ == '__main__':
    # executa a função para funcionamento
    app.run()

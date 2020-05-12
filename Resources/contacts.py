from flask_restful import Resource, reqparse
import sqlite3
import os


class DataBase:
    def __init__(self):
        # nome da base de dados
        self.name_file = 'database.db'
        # verifica se não existe o arquivo
        if not os.path.exists(self.name_file):
            try:
                # tenta criar o arquivo e se conectar a ele
                connection = sqlite3.connect(self.name_file)
                # cria um cursor
                cursor = connection.cursor()
                # executa um script para criar uma tabela com duas colunas
                cursor.execute('CREATE TABLE contacts(name TEXT, telephone TEXT)')
                # fecha a conexão
                connection.close()
            except Exception as err:
                print(err)
                # caso de erro, tenta apagar o documento
                os.remove(self.name_file)

    # função para adicionar contato
    def add_data(self, name, telephone):
        connection = sqlite3.connect(self.name_file)
        cursor = connection.cursor()
        # insere os itens passado pela função
        cursor.execute(f"insert into contacts values('{name}', '{telephone}')")
        # realiza um commit para realizar as alterações
        connection.commit()
        connection.close()

    def find_select(self):
        connection = sqlite3.connect(self.name_file)
        cursor = connection.cursor()
        # realiza uma seleção em todos os itens da tabela, numerado pelo id com rowid
        cursor.execute('select rowid, * from contacts')
        # com os itens encontrados faz uma lista
        data = cursor.fetchall()
        connection.close()
        # cria uma lista vazia
        dicio = []
        # percorre os itens encontrados
        for item in data:
            # com cada item encontrado
            dicio.append(dict(id=item[0], name=item[1], telephone=item[2]))
        # retorna a lista com os dicionários
        return dicio

    def delete(self, name):
        connection = sqlite3.connect(self.name_file)
        cursor = connection.cursor()
        # deleta o item com o nome especificado
        cursor.execute(f"delete from contacts where name = '{name}'")
        connection.commit()
        connection.close()


# classe para retornar todos os itens encontrados
class Contacts(Resource):
    def get(self):
        db = DataBase()
        return {'Contacts': db.find_select()}


# classe para retornar e exibir dados especificos
class Contact(Resource):
    def __init__(self):
        # instancia a classe para ser usada em todo corpo
        self.db = DataBase()
    # recebe os itens enviado pela requisição
    argumentos = reqparse.RequestParser()
    # armazena o item do json com a chave 'telephone'
    argumentos.add_argument('telephone')

    def get(self, name):
        found = []
        # percorre a lista com todos os itens
        for item in self.db.find_select():
            # se a chave 'name' for igual a chave recebida
            if item['name'] == name:
                # adiciona na lista o item inteiro
                found.append(item)
        if found:
            # retorna a lista com os itens encontrados com o nome especificado
            return {'found': found}
        # caso não encontre nada, retorna essa mensagem
        return {'message': 'contac not found'}, 404

    def post(self, name):
        # coloca na variavel os itens enviado pela requisição
        dados = self.argumentos.parse_args()
        # aciona a função que adiciona o banco de dados
        self.db.add_data(name, **dados)

    def delete(self, name):
        # chama a função delete, para deletar o item pedido na requisição
        self.db.delete(name)

import requests


def get_ful():
    req = requests.get("http://127.0.0.1:5000/contacts")

    get = req.json()['Contacts']
    for item in get:
        print(item)


def post(name):
    itens = {'telephone': '1194565488'}
    req = requests.post(f'http://127.0.0.1:5000/contacts/{name}', itens)
    print(req.text)
    print(req.status_code)


def delete(name):
    req = requests.delete(f'http://127.0.0.1:5000/contacts/{name}')
    # print(req.text)
    # print(req.status_code)


if __name__ == '__main__':
    # post('Solaquinho')
    # delete('Juliano')
    get_ful()

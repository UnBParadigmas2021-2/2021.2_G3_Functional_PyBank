from file_functions import read_from_file, append_on_file, write_on_file
from utils import split

DATABASE_FILE = "src/database/accounts.txt"
CLIENT_FIELDS_MAP = {
    'account_number': 0,
    'name': 1,
    'cpf': 2,
    'phone': 3,
    'type': 4,
    'balance': 5
}


def create_account(type):
    print("############################")
    print("Informe os dados do cliente: ")
    print("############################")
    name = input("Nome: ")
    cpf = input("CPF: ")
    phone = input("Telefone: ")
    account_number = input("Numero da Conta: ")  # Para manter a função pura
    account = {"account_number": account_number, "name": name,
               "cpf": cpf, "phone": phone, "type": type, "balance": 0}
    append_on_file(account, DATABASE_FILE)


def edit_client():
    client = identify_client()
    print("############################")
    print("Qual dado você gostaria de alterar?")
    print("############################")
    print("1 - Nome")
    print("2 - Telefone")

    option = int(input("Escolha uma opção: "))

    if option == 1:
        new_name = input("Digite o novo nome: ")
        new_data = [client[0], new_name, *client[2:6]]
    elif option == 2:
        new_phone = input("Digite o novo telefone: ")
        new_data = [*client[0:3], new_phone, client[4:6]]
    else:
        print("Opção Inválida!")
        exit()

    update_clients_file(client[0], new_data)


def identify_client():
    client_id = input("Digite o CPF do Cliente: ")
    client = read_account_data(client_id)
    name, cpf = get_client_data(client, ['name', 'cpf'])
    print(f"\tCliente {name}, CPF: {cpf}")
    return client


def read_account_data(id_client):
    clients = read_from_file(DATABASE_FILE)
    index = search_client(clients, id_client)
    if index == -1:
        print('Cliente não cadastrado!')
        exit()
    return split(clients[index])


def search_client(clients, id_client, index=0):
    if index >= len(clients):
        return -1
    if id_client in split(clients[index]):
        return index
    return search_client(clients, id_client, index+1)


def update_client(clients, index, new_data):
    return clients[:index] + [f"{new_data[0]},{new_data[1]},{new_data[2]},{new_data[3]},{new_data[4]},{new_data[5]}\n"] + clients[index+1:]


def update_clients_file(id_client, new_data):
    clients = read_from_file(DATABASE_FILE)
    index = search_client(clients, id_client)
    list_string = update_client(clients, index, new_data)
    write_on_file(list_string, DATABASE_FILE)


def get_client_data(client, fields: list[str]):
    client_fields = map(lambda x: client[CLIENT_FIELDS_MAP[x]], fields)
    return client_fields

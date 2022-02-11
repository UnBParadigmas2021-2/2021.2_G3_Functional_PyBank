from file_functions import read_from_file, write_on_file
from utils import join, split

DATABASE_FILE = "src/database/accounts.txt"

def create_account(type):
    print("############################")
    print("Informe os dados do cliente: ")
    print("############################")
    name = input("Nome: ")
    cpf = input("CPF: ")
    phone = input("Telefone: ")
    number_account = input("Numero da Conta: ") # Para manter a função pura
    account = {"number_account": number_account, "name": name, "cpf": cpf, "phone": phone, "type": type, "balance": 0}
    write_on_file(account, DATABASE_FILE)

def edit_client():
    cpf_client = identify_client()
    print("############################")
    print("Qual dado você gostaria de alterar?")
    print("############################")
    print("1 - Nome:")
    print("2 - Telefone")

    option = int(input("Escolha uma opção: "))

    account_data = read_account_data(cpf_client)

    if option == 1:
        new_data = [account_data[0], input("Digite o novo nome: "), account_data[2], account_data[3], account_data[4], account_data[5]]
    else:
        new_data = [account_data[0], account_data[1], account_data[2], input("Digite o novo telefone: "), account_data[4], account_data[5]]
        
    update_clients_file(account_data[0], new_data)

def identify_client():
    return input("Digite o CPF do Cliente: ")

def read_account_data(id_client):
    clients = read_from_file(DATABASE_FILE)   
    index = search_client(clients, id_client)
    if index == -1:
        print('Cliente não cadastrado!')
        exit()         
    return split(clients[index])

def search_client(clients, id_client, index = 0):
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
    file = open(DATABASE_FILE, "w")
    list_string = update_client(clients, index, new_data)
    file.write(join(list_string))
    file.close()


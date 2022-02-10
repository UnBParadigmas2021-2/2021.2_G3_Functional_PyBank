
def main():
    id_client = identify_client()
    # init, final = search_client(file, id_client)
    client = read_client_file(id_client)
    presentation_data(client)
    option = edit_client_menu()
    edit_client(option, client)

# Funções que substituem métodos python
def split(line, char=",", i=0):
    if i >= len(line):
        return [line[:-1]]
    if line[i] == char:
        return [line[:i]] + split(line[i+1:], char, 0) 
    else:
        return split(line, char, i+1)
    
def join(string_list, i=0):
    if i >= len(string_list):
        return ""
    
    txt_join = string_list[i]
    return txt_join + join(string_list, i+1)

## Funções de arquivo

def read_clients_file():
    file = open("./tmp/clients.txt", "r")
    lines = file.readlines()
    file.close()

    return lines

def read_client_file(id_client):
    clients = read_clients_file()   
    index = search_client(clients, id_client)
    if index == -1:
        print('Cliente não cadastrado!')
        exit()         
    return split(clients[index])

def update_client(clients, index, new_data, i=0, text=""):
    return clients[:index] + [f"{new_data[0]},{new_data[1]},{new_data[2]}\n"] + clients[index+1:]



def update_clients_file(id_client, new_data): 
    clients = read_clients_file()   
    index = search_client(clients, id_client)
    file = open("./tmp/clients.txt", "w")
    list_string = update_client(clients, index, new_data)
    file.write(join(list_string))
    file.close()


# Edição do cliente 

def edit_client_menu():
    print("Qual dado você gostaria de alterar?")
    print("1 - Nome:")
    print("2 - Telefone")
    return int(input("Escolha uma opção: "))
 

def presentation_data(client):
    print(f"CPF: {client[0]}\nNome: {client[1]}\nTelefone: {client[2]}")


# def search_client(file, id_client, index = 0):
#     # print(index)
#     init = file.tell()
#     line = split(file.readline())
    
#     if '' in line:
#         return
    
#     if id_client in line:
#         return init, index
    
#     return search_client(file, id_client, index+1)

# 0000,lll
# 0001,lll
# 0002,lll


def search_client(clients, id_client, index = 0):
    if index >= len(clients):
        return -1
    
    if id_client in split(clients[index]):
        return index
    
    return search_client(clients, id_client, index+1)



def edit_client(option, client):
    if option == 1:
        new_data = [client[0], input("Digite o novo nome: "), client[2]]
    else:
        new_data = [client[0], client[1], input("Digite o novo telefone: ")]
        
    update_clients_file(client[0], new_data)

def identify_client():
    return input("Digite o CPF do Cliente: ")

main()
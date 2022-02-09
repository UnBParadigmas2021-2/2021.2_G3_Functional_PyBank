def main():
    id_client = identify_client()
    presentation_data(id_client)
    option = edit_client_menu()
    edit_client(option, id_client)

def edit_client_menu():
    print("Qual dado você gostaria de alterar?")
    print("1 - Nome:")
    print("2 - Telefone")
    return input("Escolha uma opção: ")
 

def presentation_data(id_client):
    # Uso de Programação OO
    file = open("./tmp/clients.txt", "r")
    client = search_client(file, id_client)
    file.close()
    #
    # print(f"CPF: {client['cpf']}\nNome: {client['name']}\nTelefone: {client['phone']}")


def split(line, char=",", i=0):
    if i >= len(line):
        return [line[:-1]]
    if line[i] == char:
        return [line[:i]] + split(line[i+1:], char, 0) 
    else:
        return split(line, char, i+1)
    

def search_client(file, client):
    init = file.tell()
    line = split(file.readline())
    final = file.tell()

    if client in line:
        return init, final
    
    return search_client(file, client)
    
def edit_client(option, client):
    if option == 1:
        edit_name(client)
    else:
        edit_phone(client)

def edit_name(client):
    ...
def update_client_data(client):
    ...

def edit_phone(id_client):
    ...

def identify_client():
    ...
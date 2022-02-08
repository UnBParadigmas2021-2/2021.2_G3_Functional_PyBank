# def main():
#     user = getUserData()
#     register_user(user)

def write_on_file(user):
    file = open(f"./temp/clients.txt", "a")
    file.write(f"{user['cpf']}\n{user['name']}\n{user['phone']}\n\n")
    file.close()
    

def get_user_data():
    print("Enter yours datas!\n")
    name = input('Nome: ')
    cpf = input('CPF: ')
    phone = input ('Telefone: ')
    return {"name": name, "cpf": cpf, "phone": phone}


# main()
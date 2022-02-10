def write_on_file(user):
    # Uso de Programação OO
    file = open(f"./temp/clients.txt", "a")
    file.write(f"{user['cpf']}, {user['name']}, {user['phone']}\n")
    file.close()
    # 

def get_user_data():
    print("Enter yours datas!\n")
    name = input('Nome: ')
    cpf = input('CPF: ')
    phone = input ('Telefone: ')
    return {"name": name, "cpf": cpf, "phone": phone}


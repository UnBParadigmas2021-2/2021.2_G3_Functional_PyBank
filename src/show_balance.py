from edit_data import identify_client, get_client_data

def show_user_balance():
    client_data = identify_client(input("Digite o número da conta: "))
    client_balance, type_account = get_client_data(client_data,["balance", "type"])
    print(f'\nO seu saldo atual é de: R$ {client_balance}\n')
    if(type_account == 'poupanca'):
        print(f'O seu rendimento atualmente é de: R$ {int(client_balance)*0.01}\n')
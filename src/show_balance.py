from edit_data import identify_client, get_client_data
from operations import increase_balance, update_balance

def show_user_balance():
    client_data = identify_client(input("Digite o número da conta: "))
    client_balance, type_account= get_client_data(client_data,["balance", "type"])
    
    if(type_account == 'poupanca'):
        print(f'\nO seu saldo atual é de: R$ {float(client_balance)*1.01:.2f}\n')
        print(f'O seu rendimento atualmente é de: R$ {float(client_balance)*0.01:.2f}\n')
        update_balance(client_data, float(client_balance) * 0.01, increase_balance)
    else:
        print(f'\nO seu saldo atual é de: R$ {client_balance}\n')

from edit_data import identify_client, read_account_data

def show_user_balance():
  client_id = identify_client()
  client_data = read_account_data(client_id)
  print(f'\nO seu saldo atual é de: R$ {client_data[5]}\n')
  if(client_data[4] == 'poupanca'):
    print(f'O seu rendimento atualmente é de: R$ {int(client_data[5])*0.01}\n')
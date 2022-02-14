from edit_data import identify_client, read_account_data, update_clients_file

def get_withdraw_amount(current_balance):
  amount = int(input('Por favor, digite o valor que deseja sacar: '))
  if(amount > current_balance):
    print('Saldo insuficiente! Saque cancelado!')
    exit()
  return amount

def withdraw_from_account():
  client_id = identify_client()
  client_data = read_account_data(client_id)
  withdraw_amount = get_withdraw_amount(int(client_data[5]))
  updated_client_balance = int(client_data[5]) - withdraw_amount
  updated_client = [client_data[0], client_data[1], client_data[2], client_data[3], client_data[4], updated_client_balance]
  update_clients_file(client_id, updated_client)
  print("\nSeu saque foi efetuado com sucesso!\n")
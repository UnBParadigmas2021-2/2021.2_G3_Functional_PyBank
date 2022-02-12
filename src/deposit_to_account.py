from edit_data import identify_client, read_account_data, update_clients_file


def get_deposit_amount():
  amount = int(input('Por favor, digite o valor que deseja depositar: '))
  if(amount <=0 ):
    print('Valor Inválido, transação cancelada!')
    exit()
  return amount

def deposit_to_account():
  client_id = identify_client()
  client_data = read_account_data(client_id)
  deposit_amount = get_deposit_amount()
  updated_client_balance = int(client_data[5]) + deposit_amount
  updated_client = [client_data[0], client_data[1], client_data[2], client_data[3], client_data[4], updated_client_balance]
  update_clients_file(client_id, updated_client)
  print("\nSeu deposito foi efetuado com sucesso!\n")
# PyBank

**Disciplina**: FGA0210 - PARADIGMAS DE PROGRAMAÇÃO - T01 <br>
**Nro do Grupo**: 03<br>
**Paradigma**: Funcional<br>

## Alunos

| Matrícula  | Aluno                           |
| ---------- | ------------------------------- |
| 19/0063441 | Ana Carolina Carvalho da Silva  |
| 18/0113151 | Eduardo Nunes Picolo            |
| 18/0113861 | Kleidson Alves Corrêa           |
| 18/0125770 | Lucas Gabriel Bezerra           |
| 18/0114077 | Lucas Rodrigues Fonseca         |
| 18/0106970 | Matheus Gabriel Alves Rodrigues |
| 18/0129058 | Paulo Victor da Silva           |
| 18/0129287 | Pedro Henrique Vieira Lima      |
| 18/0130722 | Samuel Nogueira                 |

## Sobre

Após sofrer muito tempo com planilhas e anotações de caderno tentando manter a ordem de todas as contas no banco, o gerente do PyBank solicitou ao time de desenvolvimento que criasse uma solução que permitisse que ele tivesse todo o controle necessário para que conseguisse ajudar os clientes sem ter o risco de perder algum detalhe ou de cometer algum erro. Achando que isso não seria desafio suficiente para o time de desenvolvimento do PyBank, ele decidiu exigir que o time usasse o Paradigma Funcional na solução, após ter visto no jornal que isso era a nova tendência em soluções de organizações financeiras.

## Requisitos

Nossa integrante Ana Carolina decidiu prontamente organizar esse pedido do gerente e elaborou a seguinte lista de requisitos para guiar o time de desenvolvimento durante esse desafio.

| ID    | Requisito           | Descrição                                                                                                                                                                   |
| ----- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RF001 | Cadastro de usuário | Cadastro simples de usuário                                                                                                                                                 |
| RF002 | Criação de conta    | A conta deve ter um código identificador e estar associado a um usuário. Um mesmo código não pode estar associado a 2 usuários                                              |
| RF003 | Conta corrente      | Tipo de conta padrão do usuário                                                                                                                                             |
| RF004 | Conta poupança      | Neste tipo de conta, toda vez que o usuário optar por consultar o saldo, o valor deve ser multiplicado por 0,01 (fazendo uma referencia fictícia do rendimento da poupança) |
| RF005 | Depositar saldo     | Fazer acrescimo de valor no saldo atual                                                                                                                                     |
| RF006 | Sacar saldo         | Fazer retirada do saldo sem transferir para outra conta. Caso não exista saldo suficiente, retornar mensagem de erro                                                        |
| RF007 | Transferir saldo    | Validar se conta destino existe e realizar a transferência, senão retornar aviso                                                                                            |
| RF008 | Editar Usuário      | Alterar dados do cadastro. Não sendo possível alterar o código da conta                                                                                                     |
| RF009 | Consultar saldo     | Exibir saldo atual do usuário, se for poupança deve seguir a regra já definida                                                                                              |


Planilha de referência usada para organizar os requisitos <iframe width="200%" height="600" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQiLF5V4S0vZTmM2tC9cFMyr8XI6C7crnm6RMU2CyWswSRvGi-k531DtA6IqH5d0YiZ_Z6cxooXpOjy/pubhtml?gid=0&amp;single=true&amp;widget=true&amp;headers=false"></iframe> 


## Screenshots 

Menu principal da aplicação 

![Menu principal](/Media/img1.jpeg) 

Funcionalidade de alterar dados do usuário 

![Alterar dados do usuário](/Media/img2.jpeg) 

Lista das informações do usuário salvas em um arquivo .txt 

![Forma como os dados são guardados](/Media/img3.jpeg)

## Instalação

**Linguagens**: Python<br>
**Tecnologias**: -<br>
**Passo a Passo da instalação**:

1. Acesse o [site oficial do Python](https://www.python.org/downloads/) e baixe o instalador para seu sistema operacional.
2. Caso esteja no Windows, não se esqueça de marcar a opção para adicionar o Python ao PATH.
3. Após instalar o Python, acesse a pasta src deste repositório através do terminal.
4. Execute a aplicação através do comando:

```python
  python3 main.py
```

## Uso

Basta utilizar seu teclado para interagir com a aplicação e seguir as instruções apresentadas em tela.

## Vídeo

[![PyBank](https://img.youtube.com/vi/7xEJkpA0iyo/0.jpg)](https://www.youtube.com/watch?v=7xEJkpA0iyo)
[Link](https://www.youtube.com/watch?v=7xEJkpA0iyo)

<!-- ## Outros
Quaisquer outras informações sobre seu projeto podem ser descritas a seguir. -->

<!-- ## Fontes
Caso utilize materiais de terceiros, referencie-os adequadamente. -->

'''desafio 1
    - limite de 3 saques por dia, 
    - valor de saque limitado a R$500,00 por saque
    - não permitir deposito de valores negativos
'''

'''desafio 2
    - Estabelecer limite de 10 transações diárias
    - Exibir msg ao usuario se exceder o limite diario
    - Adicionar no extrato a data e hora das transações
'''

'''desafio 3
    - separar funções existentes: saque, deposito e extrato em funçoes - ok
    - criar novas funções: cadastrar usuario (cliente) e cadastrar cta bancária
    - a conta corrente deve estar vinculada ao usuario
    - saque: deve receber argumentos apenas por nome (keyword only). Saldo (saldo = vlr_saldo, limite_saque = 3, num_saque = qtd_saque_dia) - ok
    - deposito: recebe os argumentos apenas por posição (positional only) - ok
    - extrato: deve receber os argumentos por posição e por nome (position only e keyword only) - ok
    - Criar usuário: - ok
        - armazenar em uma lista contendo: nome, data de nascimenteo, cpf e endereço.
        - o endereço é uma string com: logradouro, no. - bairro - cidade/estado
        - cpf deve conter apenas numeros
        - não permitir cadastrar 2x o msm CPF
    - Conta Corrente:
        - armazenar em lista
        - cta é composta por: agencia, numero da cta e usuario
        - no. da conta é sequencial
        - no. da agencia é fixo : 0001
        - o usuario pode ter mais de uma cta, mas uma cta pertence a apenas 1 usuario
    - para vincular um usuario a uma cta, filtre a lista de usuarios
    buscando o no. do CPF informado para cada usuairo da lista
    '''



import textwrap
from datetime import datetime, timedelta,timezone


def menu():
    menu = """\n
    ================ MENU ================ 
    [d] \tDepositar
    [s] \tSacar
    [e] \tExtrato
    [c] \tCadastrar Cliente
    [n] \tAbrir nova conta-corrente
    [l] \tListar Clientes
    [lc] \tListar Contas
    [q] \tSair

    => """
    return input(textwrap.dedent(menu))

def depositar(vlr_deposito,extrato,saldo,numero_transacao_dia,data, /):
    if vlr_deposito> 0: 
        saldo += vlr_deposito
        numero_transacao_dia += 1
        data = datetime.now().strftime("%d/%m%Y %H:%M:%S")
        extrato += f"{data}              Depósito: \tR$ {vlr_deposito:.2f}\n"       
        print("Deposito realizado com sucesso!")        
    else:
       print ("Falha ao realizar o depósito! Verifique o valor informado.")
   
        
    return saldo, extrato, numero_transacao_dia

def sacar(*,valor_saque, extrato, saldo, num_saque,numero_transacao_dia,data,valor_max_saque,limite_saque):
    if valor_saque > valor_max_saque:
        print ("Valor superior ao limite permitido para saque. Favor inserir outro valor.")
    elif saldo < valor_saque:
        print ("Saldo insufiente.")
    elif num_saque >= limite_saque:
        print ("Limite de Saque excedido.")
    elif valor_saque > 0:
        num_saque += 1
        numero_transacao_dia += 1
        saldo -= valor_saque
        data = datetime.now().strftime("%d/%m%Y %H:%M:%S")
        extrato += f"{data}              Saque:        \tR$ {valor_saque:.2f}\n"
        print("Saque realizado com sucesso!")        
    else: 
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato,num_saque,numero_transacao_dia
     
def exibir_extrato(extrato, /, *, saldo):
    print("\n============================ EXTRATO ============================")  

    if not extrato: 
        print("Não foram realizadas movimentações." )
    else: 
        print (extrato)
        print(f"\n                                  Saldo: \tR$ {saldo:.2f}")
    
    print("==================================================================")


def validar_cpf(cpf):
    # Verifica se o CPF contém apenas números e tem 11 dígitos
    return cpf.isdigit() and len(cpf) == 11
            
def validar_endereco(endereco):
    # Verifica se o endereço está no formato correto 
    partes = endereco.split(" - ")
    if len(partes) != 3:
        return False
    logradouro, bairro, cidade_uf = partes
    return logradouro and bairro and cidade_uf
   

def validar_data(data_str):

    while True:
        
        if len(data_str) == 10 and data_str[2] == data_str[5] == "/":
            try:
                dia, mes, ano = map(int, data_str.split("/"))
                data = datetime.strptime(data_str, "%d/%m/%Y")
                # Verifica se o ano é maior ou igual a 1920 e não é superior ao ano atual
                ano_atual = datetime.now().year
                if 1920 <= data.year <= ano_atual:
                    return data
                else:return False
            except ValueError:
                return False
        else:
            return False
        
def obter_dados_cliente():

    print ("*********** INFORME OS DADOS PARA CADASTRO ***********")
    nome = input("Nome: ")
    data_str = input("Digite sua data de nascimento dd/mm/aaaa: ")
    cpf = input("CPF: ")
    endereco = (input("Endereço: "))
    
    return (nome,data_str,cpf,endereco)


def cadastrar_cliente(clientes, nome, data_nascimento, cpf, endereco):

    if validar_cpf(cpf) and validar_endereco(endereco) and validar_data(data_nascimento):
        for cliente in clientes:
            if cliente['cpf'] == cpf:
                print("CPF já cadastrado. Cliente não adicionado.")
                return
            
        novo_cliente = {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'cpf': cpf,
            'endereco': endereco
        }
        clientes.append(novo_cliente)
        print("Cliente cadastrado com sucesso!")
    else:
        print("\n******Cliente não adicionado****** ")
        if validar_cpf(cpf) == False: print("\nCPF deve conter 11 caracteres numéricos.")
        if validar_endereco(endereco) == False: print("\nEndereço deve obedecer o padrão: \nLogradouro,no. - Bairro - Cidade/UF")
        if validar_data(data_nascimento) == False : print("\nData de Nascimento precisa ser uma data válida \nEstar no formato dd/mm/aaaa \ne ano deve ser maior 1920 e menor que ou igual ano atual")
     


def listar_clientes(clientes):

    print("\n*****************CLIENTES CADASTRADOS******************")

    for cliente in clientes:
        print(f"CPF: {cliente['cpf']} | Nome: {cliente['nome']} | Data de Nasc.: {cliente['data_nascimento']} | Endereço: {cliente['endereco']}")



def cadastrar_conta(clientes,contas,agencia):

    print ("********Cadastrar Nova Conta********* \n\nPara abrir uma nova conta o cliente precisa estar cadastrado.")
    cpf = input("\nInforme o CPF: ")

   # Verifica se o CPF do cliente já está cadastrado
    cliente_encontrado = None
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            cliente_encontrado = cliente
            break

    if not cliente_encontrado:
        print("Cliente não encontrado. Cadastre o cliente primeiro.")
        return

    # Incrementa o número da conta
    if contas:
        max_numero_conta = max(contas, key=lambda c: c["numero"])["numero"]
        novo_numero_conta = max_numero_conta + 1
    else:
        novo_numero_conta = 1

    # Cadastra a nova conta 
    nova_conta = {
        "agencia": agencia,
        "numero": novo_numero_conta,
        "cpf_cliente": cpf
    }
    contas.append(nova_conta)

    print(f"\n**********Conta cadastrada com sucesso!**********\n\nAgência: {agencia} \nNúmero da conta: {novo_numero_conta:06}")   


def listar_contas(contas):

    print("\n*****************CONTAS CADASTRADAS******************\n")

    for conta in contas:
        print(f"agencia: {conta['agencia']}  | conta: {conta['numero']}| CPF_cliente: {conta['cpf_cliente']}")

def main():
    LIMITE_SAQUE = 3
    LIMITE_DIARIO_TRANSACAO = 10
    AGENCIA = "0001"
    
    
    valor_max_por_saque = 500
    saldo = 0
    saque = 0
    deposito = 0
    extrato =""
    num_saque = 0
    opcao = ""
    numero_transacao_dia = 0
    data = datetime.now()
    clientes_cadastrados = []
    lista_conta_corrente = []
    
    

    while True:   

        opcao = menu()
        
        if opcao == "e":
            exibir_extrato(extrato,saldo=saldo)   

        elif numero_transacao_dia >= LIMITE_DIARIO_TRANSACAO:  
            print ("Você excedeu o limite de transações diárias.")

        elif opcao == "c":    
            nome, data_nascimento, cpf, endereco= obter_dados_cliente()
            cadastrar_cliente(clientes_cadastrados, nome, data_nascimento, cpf, endereco)

        elif opcao == "l":
            listar_clientes(clientes_cadastrados)
        
        elif opcao == "lc":
            listar_contas(lista_conta_corrente)

        elif opcao == "n" :
            cadastrar_conta(clientes_cadastrados,lista_conta_corrente, AGENCIA)

        elif opcao == "d":
            try:
                vlr_deposito = float(input("Informe o valor do depósito: "))
                saldo, extrato, numero_transacao_dia = depositar(vlr_deposito,extrato,saldo, numero_transacao_dia,data) 
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
              

        elif opcao == "s":
            try:
                valor_saque = float(input("Informe o valor do saque: "))
                saldo, extrato, num_saque,numero_transacao_dia = sacar(
                                                valor_saque = valor_saque, 
                                                extrato = extrato,
                                                saldo = saldo,
                                                num_saque = num_saque,
                                                numero_transacao_dia = numero_transacao_dia,
                                                data = data,
                                                valor_max_saque = valor_max_por_saque,
                                                limite_saque = LIMITE_SAQUE) 

            except ValueError:
                print("Entrada inválida. Digite um número válido.")
                
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
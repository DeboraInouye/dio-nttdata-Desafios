'''
desafio
herança, polimorfismo, 

'''


import textwrap
from datetime import datetime, timedelta,timezone
from abc import ABC

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        self.indice_conta = 0

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def __str__(self):
        return f"""\
            CPF:{self.cpf} \tNome:{self.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {  
                "data" : datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                
            }
        )

class Transacao(ABC):
    @property
    def valor(self):
        pass

    @classmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao == True:
            conta.historico.adicionar_transacao(self)


class Conta(Cliente):

    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print ("Valor superior ao limite permitido para saque. Favor inserir outro valor.")
        
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")      
            return True  
        else: 
            print("Operação falhou! O valor informado é inválido.")
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Deposito realizado com sucesso!")
        else:
            print("Falha ao realizar o depósito! Verifique o valor informado.")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print ("Valor superior ao limite permitido para saque. Favor inserir outro valor.")

        elif excedeu_saques:
            print ("Limite de Saque excedido.")
        else:
            return super().sacar(valor)
        return False

    def __str__(self):
        return f"""\
            CPF:{self.cliente.cpf} \tAgência:{self.agencia} \t\tC/C:{self.numero} \tTitular:{self.cliente.nome}
        """


def busca_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def validar_cpf(cpf):
    # Verifica se o CPF contém apenas números e tem 11 dígitos
    return cpf.isdigit() and len(cpf) == 11
            
def validar_endereco(endereco):
    # Verifica se o endereço está no formato correto 
    partes = endereco.split(" - ")
    if len(partes) != 3:
        return False
    
    return True
    

def validar_data(data_str):

    while True:
        
        if len(data_str) == 10 and data_str[2] == data_str[5] == "/":
            try:
                dia, mes, ano = map(int, data_str.split("/"))
                data = datetime.strptime(data_str, "%d/%m/%Y")
                # Verifica se o ano é maior ou igual a 1920 e não é superior ao ano atual
                ano_atual = datetime.now().year
                if 1920 <= data.year <= ano_atual:
                    return True
                else:return False
            except ValueError:
                return False
        else:
            return False
        

def cadastrar_cliente(clientes):
    
    print ("*********** INFORME OS DADOS PARA CADASTRO ***********")
    cpf = input("CPF: ")
    cliente = busca_cliente(cpf, clientes)

    nome = input("Nome Completo: ")
    data_nascimento = input("Digite sua data de nascimento dd/mm/aaaa: ")
    

    endereco = (input("Endereço: "))
    

    if cliente:
        print("\n******Cliente não adicionado****** ")
        print("CPF já cadastrado. Cliente não adicionado.")
        return 
    
    elif validar_cpf(cpf)== False or validar_data(data_nascimento)== False or validar_endereco(endereco)== False:
        
        print("\n******Cliente não adicionado****** ")
        if validar_cpf(cpf) == False: print("\nCPF deve conter 11 caracteres numéricos.")
        if validar_data(data_nascimento) == False : print("\nData de Nascimento precisa ser uma data válida \nEstar no formato dd/mm/aaaa \ne ano deve ser maior 1920 e menor que ou igual ano atual")
        if validar_endereco(endereco) == False: print("\nEndereço deve obedecer o padrão: \nLogradouro,no. - Bairro - Cidade/UF")
        return
    
    else:
        cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf= cpf, endereco = endereco)
        clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")
 
       

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = busca_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado. Cadastre o cliente primeiro.")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print(f"\n**********Conta cadastrada com sucesso!**********")  
    print (f"\nNúmero da conta: {numero_conta}")


def buscar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nCliente não possui conta!")
        return
    

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

    print(f"A conta com o número {numero_conta} não pertence a esse cliente.")
    return None
   


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = busca_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!")
        return

    

    conta = buscar_conta_cliente(cliente )

    if not conta:
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor) 
    cliente.realizar_transacao(conta, transacao)

   
    

def sacar(clientes):
    cpf = input("Informe o CPF:: ")
    cliente = busca_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!")
        return
    
   
    conta = buscar_conta_cliente(cliente)
    if not conta:
        return

 
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    cliente.realizar_transacao(conta, transacao)
    
def formatar_valor(valor):
    largura=12
    return f"R$ {valor:{largura}.2f}"


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = busca_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado! ")
        return

  
    conta = buscar_conta_cliente(cliente)
    if not conta:
        return

    print("\nE X T R A T O ")
    print  ("=" *100)
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        print("Data\t\t\tTipo\t\t\tValor")
        print("=" * 100)
        for transacao in transacoes:
            tipo_formatado = transacao['tipo'].ljust(15)  # Largura fixa para o tipo
            valor_formatado = formatar_valor(transacao['valor'])
            print(f"{transacao['data']}\t{tipo_formatado}\t{valor_formatado}")

    saldo_formatado = formatar_valor(conta.saldo)
    print("=" * 100)
    print(f"\t\t\tSaldo:\t\t{saldo_formatado}")
    
    print  ("=" *100)



def listar_clientes(clientes):

    print("\nC L I E N T E S    C A D A S T R A D O S\n")
    print("=" * 100)
    for cliente in clientes:
        
        print(textwrap.dedent(str(cliente)))

    print("=" * 100)


def listar_contas(contas):

    print("\nC O N T A S    C A D A S T R A D A S\n")
    print("=" * 100)
    for conta in contas:
        
        print(textwrap.dedent(str(conta)))
    print("=" * 100)


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


def main():
    
    clientes = []
    contas = []
    
    
    while True:   

        opcao = menu()
        
        if opcao == "e":
            exibir_extrato(clientes)   

        elif opcao == "c":    
            cadastrar_cliente(clientes)

        elif opcao == "l":
            listar_clientes(clientes)
        
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "n" :
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
            
        elif opcao == "d":
            depositar(clientes)
              

        elif opcao == "s":
            sacar(clientes)
                
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
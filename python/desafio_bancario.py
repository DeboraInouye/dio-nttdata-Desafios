# limite de 3 saques por dia, 
# valor de saque limitado a R$500,00 por saque
# não permitir deposito de valores negativos


saque = 0
deposito = 0
extrato =""
num_saque = 0
valor_limite_saque = 500
LIMITE_SAQUE = 3
saldo = 0
opcao = ""

#================ MENU ================ 

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
    


def depositar(vlr_deposito,extrato,saldo):
   
    if vlr_deposito> 0: 
        saldo += vlr_deposito
        extrato += f"Deposito: R$ {vlr_deposito:.2f}\n"
        
        print("Deposito realizado com sucesso!")
        

    else:
        print ("Falha ao realizar o depósito! Verifique o valor informado.")
 
    return saldo, extrato

def sacar(valor_saque, extrato, saldo, num_saque):

    if num_saque >= LIMITE_SAQUE:
        print ("Você já excedeu a quantidade de saques permitidas no dia.")

    elif valor_saque > valor_limite_saque:
        print ("Valor superior ao limite permitido para saque. Favor inserir outro valor.")

    elif saldo < valor_saque:
        print ("Saldo insufiente.")

    elif valor_saque > 0:
        num_saque += 1
        saldo -= valor_saque
        extrato += f"Saque: R$ {valor_saque:.2f}\n"
        print("Saque realizado com sucesso!")

    else: 
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato,num_saque
  
def exibir_extrato(extrato,saldo):
    print("\n================ EXTRATO ================")  

    if not extrato: 
        print("Não foram realizadas movimentações." )
    else: 
        print (extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
    
    print("==========================================")
     
while True:
    
    opcao = input(menu)

    if opcao == "d":
        vlr_deposito = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(vlr_deposito,extrato,saldo)
        

    elif opcao == "s":
        valor_saque = float(input("Informe o valor do saque: "))
        saldo, extrato, num_saque = sacar(valor_saque, extrato, saldo,num_saque)

    elif opcao == "e":
        exibir_extrato(extrato,saldo)
    
    
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
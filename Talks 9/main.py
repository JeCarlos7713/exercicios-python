
class Account:
    #atributos:
    __account_number = None
    __agency = None
    __account_holder = None
    __account_balance = 0.00

    #definindo constructor
    def __init__(self, agency: str, account_number: str, account_holder: str, account_balance: float) -> None: #self busca o escopo do contexto Account
        self.__agency = agency
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__account_balance = account_balance

    #métodos:
    def get_account_balance(self): #busca o account (getter)
        return self.__account_balance
    
    def get_agency(self):
        return self.__agency
    
    def get_account_number(self):
        return self.__account_number
    
    def get_account_holder(self):
        return self.__account_holder
    
    
    def set_account_balance(self, balance): #adiciona valor no atributo account_balance um novo valor (setter)
        self.__account_balance = balance
    
    def set_agency(self, agency):
        self.__agency = agency
    
    def set_account_number(self, number):
        self.__account_number = number

    def set_account_holder(self, holder):
        self.__account_holder = holder

    def __has_balance(self, amount):
        if self.__account_balance <= 0 or self.__account_balance < amount :
            return False
        else:
            return True

    def cash_in(self, amount: float):
        print("Olá ", self.__account_holder, "! Seja bem-vindo(a)")
        if amount > 0.0:
            self.__account_balance += amount
            print("Depósito de R$", amount, " realizado com sucesso! Saldo atual: R$", self.__account_balance)
        else:
           print('Não houve depósito. Valor atual: R$', self.__account_balance)
        

    def cash_out(self, amount: float):
        print("Olá ", self.__account_holder, "! Seja bem-vindo(a)")
        is_balance = self.__has_balance(amount=amount)
        if is_balance:
            if amount > 0.0:
                self.__account_balance -= amount
                print("Saque de R$", amount, " realizado com sucesso! Saldo atual: R$", self.__account_balance)
            else:
                print('Não houve saque. Valor atual: R$', self.__account_balance)
        else:
            print("Você não tem saldo suficiente")    


def main():
    print("#" * 60)
    print("MFX Banking")
    print("#" * 60)

    print("Informe sua agência:")
    agency = input()

    print("Informe o número da conta:")
    account = input()

    print("Informe o nome do cliente:")
    holder = input()

    print("Informe o saldo da conta")
    balance = input()

    account_01 = Account(
        agency=agency, 
        account_number=account, 
        account_holder=holder, 
        account_balance=float(balance)
    )

    print("#" * 60)
    print("Selecione a operação:")
    print("#1 - Cash-In \n #2 - Cash-Out")
    operation = input()
    
    if operation in '1':
        print("Digite o valor a ser depositado: ")
        amount_cash_in = input()
        account_01.cash_in(float(amount_cash_in))
    elif operation in '2':
        print("Digite o valor a ser sacado: ")
        amount_cash_out = input()
        account_01.cash_out(float(amount_cash_out))


if __name__ == "__main__":
    main()


"""
    Modo errado de setar valor no meu atributo
    account_01.__account_holder='erikola'

    Modo errado de buscar uma informação do meu atributo
    print(account_01.account_balance)
    modo certo
    account_01.set_account_balance(20000.00)
    print(account_01.__account_holder)
"""
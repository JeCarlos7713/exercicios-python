

class Account:
    #atributos:
    __account_number = None
    __agency = None
    __account_holder = None
    __account_balance = None

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




def main():
    account_01 = Account(agency="001", account_number="12345678-9", account_holder="Jean Carlos", account_balance=10000.00)
    
    
    """
    Modo errado de setar valor no meu atributo
    account_01.__account_holder='erikola'

    Modo errado de buscar uma informação do meu atributo
    print(account_01.account_balance)
    """

    #modo certo
    account_01.set_account_balance(20000.00)
    print(account_01.__account_holder)


if __name__ == "__main__":
    main()
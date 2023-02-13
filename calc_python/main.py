def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def sum(x, y):
    return x + y

def divisor(x, y):
    return x / y

def calc():

    while True:
            
        print("#" * 30)
        print("Take my pocket")
        print("#" * 30)
        print("Operação aritmética:")
        
        print("Digite o primeiro numero: ")
        x = int(input())
        
        print("Digite o segundo numero: ")
        y = int(input())

        print("Digite o operador ( + | - | * ): ")
        op = input()
        result = None

        if op == "+" :
            result = sum(x, y)

        elif op == "-":
            result = sub(x, y)
        
        elif op == '*':
            result = mult(x, y)
        
        elif op == '/':
            result = divisor(x, y)

        else :
            if result == None:
                print("O Resultado é 0")
            result = 'valores não enviados'
        
        print("O resultado da operação é: ", result)
        #print(f"O resultado da operação é: {result}") #f é um template string
        yes = 'yes'
        no = 'no'
        print(f"Deseja continuar? ({yes.upper()} | {no.upper()})")
        conditional = input()
        print('Conditional: ', conditional)

        if conditional in "No":
            break

if __name__ == "__main__": #chama a classe inicializadora
    calc()


#in traz se é verdadeiro ou falso
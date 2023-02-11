import random
import os
from time import time

##############################DICT##############################
def calc(op: dict):
    if "sum" in op:
        #return print(op.items()) pega os ittens e adiciona em tuplas
        #return print(op.keys()) pega as chaves (valores) e add em uma tupla
        return print(op.values())

def talks():
    #print("CALCULADORA: ")
    #print("#" * 10)
    
    json = {"sum": "+", "sub" : "-", "multi": "*", "div" : "/"}
    
    #for key, value in json.items():
        #print(key, ':', value)

    #calc(json)
    cube = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    for item in range(1):
        x = random.choice(cube)
        print(x)

    #arquivo()

    print(Car(wheels="17", horse="77cv", brand="volks").horse)
################################################################

class Car:
    #atributos
    whells = None
    brand = None
    horse = None

    # métodos

    def __init__(self, wheels: str, horse:str, brand: str) -> None:
        self.whells = wheels
        self.brand = horse
        self.horse = brand

    def run(self): #self consegue referenciar-se aos atributos dentro da classe 
        
        pass

    def stop(self):
        pass

    def ligths(self):
        pass

    def run_fast(self):
        pass

#############################TUPLE##############################

def tupla():
    t = ("a", "n")
    todayDate = ("12")

    return (t)
################################################################

#############################ARQUIVOS##############################

def arquivo():
    file = open("teste.txt", "w")
    file.write("Take my pocket \n Zoka is real")
    file.close()

    #cwd = os.getcwd() pegando caminho
    file_path = os.path.abspath("teste.txt") #pegando caminho com nome do docs
    print(file_path)

    with open("teste.txt") as f:
        lines = f.readlines()
        print(lines)

################################################################

if __name__ == '__main__':
    talks()
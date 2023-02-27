import functools

class Retangle:

    def __init__(self, x, y) -> None:
        self.__y = y
        self.__x = x
        self.__area = None
    
    @staticmethod #diz que o método não precisa de um self, pois ele é estático
    def calc_area(func):
        @functools.wraps(func) #preservo a estrutura da função
        def execute(self): #usa o self através da wraps
            self.__area = self.__x * self.__y
            return func(self)
        
        return execute

    @property
    def get_area(self):
        return self.__area
    
    @get_area.setter
    def get_area(self, x):
        self.__area = x

    @calc_area #property customizada
    def area(self): #o self me diz que é um método, não uma função
        print("="*40)
        print(f"A área é {self.__area}")
        print("="*40)
    
def main():
    instance = Retangle(x=20, y=9)
    instance.area()

if __name__ == "__main__":
    main()
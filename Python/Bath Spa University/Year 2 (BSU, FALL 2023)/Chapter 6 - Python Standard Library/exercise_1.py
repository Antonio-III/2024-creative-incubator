import math

# Default settings
FIND_CEIL_OF=2.3
FIND_FLOOR_OF=2.3
FIND_FACTORIAL_OF=5
FIND_CUBE_OF=2
FIND_SQ_ROOT_OF=16

class App:
    def __init__(self,**kwargs: int | float):
        # round up if non-zero decimal
        self.ceil=kwargs.get('ceil', 0)
        # round down to the nearest whole number. 2.99 rounds to 2
        self.floor=kwargs.get('floor', 0)
        self.factorial=kwargs.get('factorial', 0)
        self.pow=kwargs.get('base', 0)

        self.sqrt=kwargs.get('sqrt', 0)

        self.operations_names=['ceil','floor','factorial','pow','sqrt']
        self.operations_result=[math.ceil(self.ceil),math.floor(self.floor),math.factorial(self.factorial),math.pow(self.pow,3),math.sqrt(self.sqrt)] # type: ignore
        
    def output(self)->None:
        for operation,result in zip(self.operations_names,self.operations_result):
            print(f'The {operation} of {getattr(self,operation)} is {result}')
            if operation=='pow':
                print(f'{getattr(self,operation)} raised to 3 is {result}')

def main()->None:
    App(ceil=FIND_CEIL_OF,floor=FIND_FLOOR_OF,factorial=FIND_FACTORIAL_OF,base=FIND_CUBE_OF,sqrt=FIND_SQ_ROOT_OF).output()

if __name__ == "__main__":
	main()
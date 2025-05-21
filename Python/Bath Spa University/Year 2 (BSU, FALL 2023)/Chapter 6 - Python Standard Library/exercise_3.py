import operator

QUIT_BUTTON='q'
QUIT_PROMPT='Would you like to quit? Press q if so\n'

class App:
    def __init__(self):
        self.quit=False
        self.operations_name=('Addition','Subraction','Multiplication','Division','Modulus Division','Greater Number')
        self.operations_name_len=len(self.operations_name)

        self.foreverloop()
        
    def foreverloop(self)->None:
        
        while self.quit!=True:
            self.operation_end=False
            self.user_input=int(input('Enter a number 1-6:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus\n6. Check greater number\n'))
            
            if self.user_input in range(1,self.operations_name_len+1): #inclusive
                self.operation(self.user_input)
            else:
                print('Wrong input\n')
                
            if self.operation_end!=False:
                self.q=input(QUIT_PROMPT)
                
                if self.q.lower().startswith(QUIT_BUTTON):
                    self.quit=True
                
    def operation(self,chosen_num)->None:
        self.selected_operation=chosen_num-1 # offset so the index can fit into the list (which has 5 elements, whereas the user can enter the number 6)
        
    
        self.num_one=int(input('Enter first num: '))
        self.num_two=int(input('Enter second num: '))

        self.operations=(operator.add(self.num_one,self.num_two),operator.sub(self.num_one,self.num_two),operator.mul(self.num_one,self.num_two),operator.truediv(self.num_one,self.num_two),
                         operator.mod(self.num_one,self.num_two),operator.gt(self.num_one,self.num_two))

        if chosen_num==6:
            print(f'The first number {self.num_one} being greater than {self.num_two} is: {self.operations[self.selected_operation]}\n')
        else:
            print(f'The {self.operations_name[self.selected_operation]} between {self.num_one} and {self.num_two} is {self.operations[self.selected_operation]}\n')
        
        self.operation_end=True

def main()->None:
    App()

if __name__ == "__main__":
	main()
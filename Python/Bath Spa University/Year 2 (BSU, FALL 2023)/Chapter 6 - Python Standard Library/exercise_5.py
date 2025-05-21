import json

FILE_DIR='Text Files/StudentJson.json'

class App:
    def __init__(self):
        self.name=input('Enter name: ')
        self.id=input('Enter ID: ')
        self.course=input('Enter Course: ')
        
        self.dict={"Details of the Student are":{"Name":self.name.title(),"ID":self.id,"Course":self.course}}
 
        self.output_one()
        self.output_two()

    def write_to_file(self,directory,content):
        with open(directory,'w') as file_handler:
            json.dump(content,file_handler,indent=4)
            
    def output_dict(self):
        for key in self.dict.keys():
            print(f'\n{key}')
            
        for key,value in self.dict['Details of the Student are'].items():
            print(f'\t{key}: {value}')
            
    def output_one(self):
        # you can create a new variable and have it point to the .load() return value of json lib, but I'm skipping that because it returns the same dict object
        self.write_to_file(FILE_DIR,self.dict)

        # output file
        self.output_dict()
        
            
    def output_two(self):
        # introduce new dict
        self.course_details={"Course Details":{"Group":"A","Year":2}}
        # update student dictionary with new dict values
        self.dict["Details of the Student are"].update(self.course_details["Course Details"])
        # update file
        self.write_to_file(FILE_DIR,self.dict)

        # output file
        self.output_dict()
            
def main()->None:
    response=input(f'Running this app will create a directory "{FILE_DIR}" at the current directory. Proceed? (y/n)')
    if response.lower().startswith('y'):
        App()   

if __name__ == "__main__":
	main()
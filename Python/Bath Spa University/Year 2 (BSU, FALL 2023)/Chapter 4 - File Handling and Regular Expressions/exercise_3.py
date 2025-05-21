
# DEfault settings
FILE_DIR='Text Files/numbers.txt'

def main() -> None:
    file=FILE_DIR

    try:
        with open(file) as file_handler:
            file_list=file_handler.readlines()

        int_file=[int(i) for i in file_list]
    except FileNotFoundError:
         print(f'A directory "{FILE_DIR}" must exist in the current directory for the app to work.')
    else:
        print(int_file)
        
if __name__ == "__main__":
	main()
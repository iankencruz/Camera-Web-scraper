import os


class ReName:
    print("Class Rename")
    def __init__(self, state='') -> None:
        self.path = os.getcwd()
        self.state = state
    


    def get_info(self):
        print(f'CWD: {self.path}') 


    def get_changes(self, name , path=None, state=''):
        ''' 
        Walk Directory of Path. 
             Params:  
                path ( str ) : Target path you want to search(Default is cwd)
        '''
        if path is None:
            path = self.path            

        iter_amnt = 1
        old_name = ''
        new_name = ''

        for root, folders, files in os.walk(path):
            for file in files:
                file_name, file_ext = os.path.splitext(file)
                file_list = []
                file_list.append(file)
                old_name = file_list[0]
                file_list.clear()
                changed_name = f'{name}_0{iter_amnt}{file_ext}'
                file_list.append(changed_name)
                new_name = file_list[0]

        print('\n')
        print(f"Old: {old_name}")        
        print(f"New: {new_name}")        
        print('\n')
        # return old_name, new_name
        # return file_list


    def batch_rename(self, name, path=None, ):
        
        ''' 
        Walk Directory of Path. 
             Params:  
                name ( str ) : Target name to replace old name
                path ( str ) : Target path you want to search(Default is cwd)
        '''
        
        # Function operation checks
        if path is None:
            path = self.path   



        iter_amnt = 1
                

        for root, folders, files in os.walk(path):
            for file in files:
                file_name, file_ext = os.path.splitext(file)

                try:
                    old_name = f'{path}\{file_name}{file_ext}'
                    # print(f"Old Name: {old_name}\n")
                    new_name = f'{path}\{name}_0{iter_amnt}{file_ext}'
                    # print(f"New Name: {new_name}\n")
                    # os.rename(old_name, new_name)

                    

                    iter_amnt += 1
                except IndexError:
                    print("Index out of range")
                            
    def batch_replace(self, src_name='', target_name='', path=None):



        # Function operation checks
        if path is None:
            path = self.path   

                

        for root, folders, files in os.walk(path):
            for file in files:
                if(src_name in file):
                    file_name, file_ext = os.path.splitext(file)
                    f_tag, f_title = file_name.split(src_name, 1)

                    try:
                        old_name = f'{path}\{file_name}{file_ext}'
                        new_name = f'{path}\{target_name}{f_title}{file_ext}'
                        print(f'Old Name = {old_name}')
                        print(f'New Name = {new_name}')
                        # os.rename(old_name, new_name)
                        

                        
                    except IndexError:
                        print("Index out of range")

    #!
    #TODO: Single file target rename 



#TODO Options to 1. simple rename 2. Remove specific tags


class ui_menu:
    def __init__(self) -> None:
        pass

    #* Menu for selecting which function to use
    def main_menu(self):
        print('*********************************')
        print('Please select an option:')
        print('\n')
        print('1. Batch rename | SIMPLE')
        print('2. Batch selective rename | ADVANCED')
        print('\n')
        print('x. Exit Program')
        print('\n')
    

    #* Options for batch replacing 
    def replace_menu(self):
        print('*********************************')
        print('Please select an option:')
        print('\n')
        print('1. Batch rename | SIMPLE')
        print('2. Batch selective rename | ADVANCED')
        print('\n')


def main():

    # Setup files and dirs

    rn = ReName()
    rn.get_info()

    
    
    ui = ui_menu()
    isRunning = True


    location = str(input("Enter Target Directory: "))
    location = f'"{location}"'
    
    print('\n')
    print('Current Directory :')
    print (location)
    print('\n')
    
    # Select type of renaming process
    #TODO Menu 

    ui.main_menu()
    
    selection = input("Input: ")   
    
    if selection == '1':
        
        # ui.rename_menu()
        print('\n')
        sel = input("Rename to: ")
        rn.get_changes(name=sel, path=location)
        
        confirm = input("Confirm Selection: Y/N: ").lower()

        if confirm == 'y':            
            rn.batch_rename(confirm, location)
            print("RENAME FUNC")
        elif confirm == 'n':
            print("Operation Cancelled.")
            main()
        else:
            print("Please input valid type. ")
            main()
            

    elif selection == '2':
        print("Replace Function")
        rm_text = input("Enter text that you wish to remove: ")
        new_text = input("Replace with : ")
        rn.get_changes(name=new_text, path=location)

        confirm = input("Confirm Selection: Y/N: ").lower()

        if confirm == 'y':
            rn.batch_replace(src_name=rm_text, target_name=new_text, path=location)
        elif confirm == 'n':
            print("Operation Cancelled.")
            main()
        else:
            print("Please input valid type. ")
            main()

    elif selection == 'x':
        os._exit(1)
    # ERROR AND DATATYPE HANDLING    2
    else:
        print("ValueError: Please Input valid type. ")
        main()






if __name__ == "__main__":
    main()


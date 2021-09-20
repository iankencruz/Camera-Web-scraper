import os


class ReName:
    print("Class Rename")
    def __init__(self) -> None:
        self.path = os.getcwd()
    


    def get_info(self):
        print(f'CWD: {self.path}') 


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
                    print(f"Old Name: {old_name}\n")
                    new_name = f'{path}\{name}({iter_amnt}){file_ext}'
                    print(f"New Name: {new_name}\n")
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



# Options to 1. simple rename 2. Remove specific tags


# 


def main():

    # Setup files and dirs
    location =r"E:\Anime\Bleach\dev"

    rn = ReName()
    rn.get_info()
    


    # Select type of renaming process


    #*  Confirm inputs

    
    # rn.batch_rename("kenny", location)
    # rn.batch_replace("-" , 'Bleach -',path=location)

if __name__ == "__main__":
    main()


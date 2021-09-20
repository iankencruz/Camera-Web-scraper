import os


class ReName:
    print("Class Rename")
    def __init__(self) -> None:
        self.path = os.getcwd()
    


    def get_info(self):
        print(f'CWD: {self.path}') 


    def walk_dir(self, path=None):
        ''' 
        Walk Directory of Path. 
             Params:  
                path ( str ) : Target path you want to search(Default is cwd)
        '''
        if path is None:
            path = self.path            

        file_list = []

        for root, folders, files in os.walk(path):
            for file in files:
                # file_name, file_ext = os.path.splitext(file)
                # print(f"Files: {file}")
                file_list.append(file)

        return file_list
        

    def batch_rename(self, name, path=None, ):
        
        ''' 
        Walk Directory of Path. 
             Params:  
                path ( str ) : Target path you want to search(Default is cwd)
        '''
        
        iter_amnt = 1

        if path is None:
            path = self.path            


        for root, folders, files in os.walk(path):

            
            for file in files:
                


                file_name, file_ext = os.path.splitext(file)
                # print(f"Files: {file}")

                try:
                    old_name = f'{path}\{file_name}{file_ext}'
                    print(f"Old Name: {old_name}\n")
                    new_name = f'{path}\{name}({iter_amnt}){file_ext}'
                    print(f"New Name: {new_name}\n")

                    # os.rename(old_name, new_name)

                    iter_amnt += 1
                except FileNotFoundError:
                    print("Error: Cannot find files")
                    
            print(len(files))

        # print(f_list)
        print ("batch rename")
        

    def batch_replace():
        pass



# Options to 1. simple rename 2. Remove specific tags


# 


def main():

    rn = ReName()
    rn.get_info()
    rn.batch_rename("kenny", path=r"E:\Anime\Bleach\[Judas] Bleach 001-055 [BD 1080p][HEVC x265 10bit]")

    # location = f'C:\\Users\\PC\AppData\Local\CaptureOne\Styles50\IKM'

    # for root, folder, files in os.walk(location):
    #     for name in files:
    #         file_name, file_ext = os.path.splitext(name)
    #         f_title = file_name.split("_", 1)

    #         try:
    #             old_name =  f'{location}\{file_name}{file_ext}'
    #             new_name = f'{location}\{f_title[1]}{file_ext}'
    #             os.rename(old_name, new_name)
    #             print(f'old name :{old_name}')
    #             print(f'new name :{new_name}')
        
    #         except IndexError:
    #             print("Index out of range")




if __name__ == "__main__":
    main()


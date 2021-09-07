import pyperclip
import os


location = r"C:\Users\PC\Downloads\Slime dev - Copy"


blacklist = 'Tensura'

series_name = pyperclip.paste()
vol_num = 13

for root, folder, files in os.walk(location):
    for name in files:
        if(blacklist in name):
            file_name, file_ext = os.path.splitext(name)
            f_title, f_num = file_name.split(" ", 1)

            try:
                old_name =  f'{location}\{file_name}{file_ext}'
                # Change to suit needs
                new_name = f'{location}\{series_name}- LN {vol_num}{file_ext}'

                vol_num += 1

                print (new_name)
                os.rename(old_name, new_name)
                

            except FileExistsError:
                print("Error: Cannot Find File!")
            
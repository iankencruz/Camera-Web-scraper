import random


D = {'Camera1': {'name': 'Sony', 'job': 'Mirrorless'},
     'Camera2': {'name': 'Fujifilm', 'job': 'APS-C'},
     'Camera3': {'name': 'Canon', 'job': 'DSLR'}}




for item, brand in D.items():
    print ( item)
    D[item]['rating'] = str(random.randrange(1,6)) + " stars"
    for key in brand:
        print (key + ':', brand[key])
    print ('\n')


print ("\n")
print (D)
my_dict = {'first_name': ['Jeremy', 'Joe', 'Tom'], 'last_name': ['Hefner', 'Dimagio', 'Brady']}
my_dict2 = {'Jan' : 1, 'Feb': 2, 'Mar': 4}



print('Adding a new name to the list, please wait........')
my_dict['first_name'].append('Cosmo')
my_dict['last_name'].append('Kramer')
for first_name, last_name in zip(my_dict['first_name'], my_dict['last_name']):
    print(first_name, last_name)

my_keys = my_dict2.keys()

print('Showing my keys', my_keys)
for a_item in my_dict2.items():
    print(a_item)

def scream():
    print('ahhhhh!')


user = {
    'age': 27,
    'name': 'Meredith',
    'magic': True,
    'scream': scream,
    'test': lambda num: num*2,
    scream(): 'lol',
    15: 'teenager'
}


print(user['age'])
user['scream']()
user['spell'] = 'abra kadabra'

print(user['spell'])

# how to call a lambda function defined inside a dictionary
print(user['test'](2))

print(user[scream()])


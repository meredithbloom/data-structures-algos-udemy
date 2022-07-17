# LINKED LISTS
# singly vs doubly

basket = ['apples', 'grapes', 'baguette', 'pears']


# linked list: apples 
#                   --> grapes 
#                            --> baguette 
#                                       --> pears
#                                                --> null

# 10 --> 5 --> 16

my_linked_list = {
    'head': {
        'value': 10,
        'next': {
            'value': 5,
            'next': {
                'value': 16,
                'next': None
            }
        }
    }
}
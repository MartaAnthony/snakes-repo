order = {
  'appetizers' : {
    'wings': 0,
    'cookies': 0,
    'spring rolls': 0,
  },

  'entrees' : {
    'salmon': 0,
    'steak': 0,
    'meat tornado': 0,
    'a literal Garden': 0,
  },

  'desserts' : {
    'ice cream': 0,
    'cake': 0,
    'pie': 0,
  },

  'drinks' : {
    'coffee': 0,
    'tea': 0,
    'unicorn tears': 0,
  }
}     

def main():
  print_menu()
  user_input = ''
  while user_input != 'quit':
    user_input = input('> ')
    
    for key in order['appetizers']:
      if user_input == key:
        order['appetizers'][key] += 1
        print('** ' + str(order['appetizers'][key]) + ' order of ' + user_input + ' has been added to your meal **')
    for key in order['entrees']:
      if user_input == key:
        order['entrees'][key] += 1
        print('** ' + str(order['entrees'][key]) + ' order of ' + user_input + ' has been added to your meal **')
    for key in order['desserts']:
      if user_input == key:
        order['desserts'][key] += 1
        print('** ' + str(order['desserts'][key]) + ' order of ' + user_input + ' has been added to your meal **')
    for key in order['drinks']:
      if user_input == key:
        order['drinks'][key] += 1
        print('** ' + str(order['drinks'][key]) + ' order of ' + user_input + ' has been added to your meal **')


def print_menu():
  print('''
  **************************************
  **    Welcome to the Snakes Cafe!   **
  **    Please see our menu below.    **
  **
  ** To quit at any time, type "quit" **
  **************************************
  ''')

  print('''
  \tAppetizers
  \t----------
  ''')
  for key in order['appetizers']:
    print('\t'+key.capitalize())

  print('''
  \tEntrees
  \t-------
  ''')
  for key in order['entrees']:
    print('\t'+ key.capitalize())
  
  print('''
  \tDesserts
  \t--------
  ''')
  for key in order['desserts']:
    print('\t' + key.capitalize())

  print('''
  \tDrinks
  \t------
  ''')
  for key in order['drinks']:
    print('\t'+ key.capitalize())

  print('''
  ***********************************
  ** What would you like to order? **
  ***********************************
  ''')

main()

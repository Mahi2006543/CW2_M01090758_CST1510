from log_hash import register_user, log_in_user

def menu():
   print('*'* 30)
   print('*** welcome to my system ***')
   print('choose from the following options:')
   print('1. register')
   print('2. log in')
   print('3. exit')
   print('*'* 30)
   
   
def main():
   while True:
      menu()
      choice = input('> ')
      if choice == '1':
         register_user()
      elif choice == '2':
         if log_in_user():
            print('you loged in !!')
         else:
            print('incorect log in')
      elif choice == '3':
        print('good bye!!')
      break
   

if __name__ == '__main__':
   main()

         





    
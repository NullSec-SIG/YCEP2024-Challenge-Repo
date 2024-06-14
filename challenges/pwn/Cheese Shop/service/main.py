def greetings(balance, cheese):
  print(r"""
          )         (         (       )    )  (     
   (   ( /(         )\ )      )\ ) ( /( ( /(  )\ )  
   )\  )\())(   (  (()/((    (()/( )\()))\())(()/(  
 (((_)((_)\ )\  )\  /(_))\    /(_)|(_)\((_)\/(_)) 
 )\___ _((_)(_) ((_)_))((_)  (_))  _((_)(_))(_))   
((/ __| || | __| __/ __| __| / __|| || |/ _ \| _ \  
 | (__| __ | _|| _|\__ \ _|  \__ \| __ | (_) |  _/  
  \___|_||_|___|___|___/___| |___/|_||_|\___/|_|    
""")
  print("🧀 WELCOME! 🧀\nYour balance: {} coins\nCheese: {}".format(balance, cheese))

def menu(cost):
  opns = ["Buy Cheese", "Buy fake flag", "Buy flag", "Check Balance", "Exit"]
  while True:
    try:
      print()
      print("-" * 35)
      for i in range(0, 3):
        print("{}. {:<13} : {} coins".format(i+1, opns[i], cost[i]))
      for i in range(3, 5):
        print("{}. {:<13}".format(i+1, opns[i]))
      print("-" * 35)

      opn = int(input("Enter option: "))
      
      return opn  
        
    except ValueError:
      print("Invalid.")
    except:
      exit()


def player(cost, balance, cheese):
  try:
    with open("flag.txt", "r") as file:
      flag = file.read()

    with open("fake.txt", "r") as fake:
      fake_flag = fake.read()
  except FileNotFoundError:
    print("File not found.")
    exit()
    
  while True:
    opn = menu(cost)

    match opn:
        case 1:
            try:
              num_cheese = int(input("Enter number of cheese to buy: "))
              if balance >= cost[0] * num_cheese:
                cheese += num_cheese
                balance -= cost[0] * num_cheese
                print("Sold!")
              else:
                print("Not enough coins :(")
            except ValueError:
              print("Invalid.")
        case 2:
            if balance >= cost[1]:
                balance -= cost[1]
                print("Here's your fake flag: {}".format(fake_flag))
            else:
                print("Not enough coins :(")
        case 3:
            if balance >= cost[2]:
                balance -= cost[2]
                print("VIP!🧀 Here's your flag: {}".format(flag))
            else:
                print("Not enough coins :(")
        case 4:
            print("Your balance: {} coins\nCheese: {}".format(balance, cheese))
        case 5:
            print("Bye!")
            break
        case _:
            print("Invalid.")

def main():
  balance = 150
  cheese = 0
  cost = [15, 100, 10000]
  
  greetings(balance, cheese)
  player(cost, balance, cheese)


if __name__ == "__main__":
  main()
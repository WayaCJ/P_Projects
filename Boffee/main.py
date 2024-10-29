# Define your functions
def print_message():
  print("I'm sorry, i did not understand your selection. Please enter the corresponding letter for your response.")

def order_latte():
  res = input('What kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n')
  if res == 'a':
    return '2% latte'
  elif res == 'b':
    return 'Non-fat latte'
  elif res == 'c':
    return 'Soy latte'
  else:
    print_message()
    return order_latte()

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n')
  if res == 'a':
    return 'Brewed Coffee'
  elif res == 'b':
    return 'Mocha'
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

def get_size():
  res = input('What drink size can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n')
  if res == 'a':
    return 'Small'
  elif res == 'b':
    return 'Medium'
  elif res == 'c':
    return 'Large'
  else:
    print_message()
    return get_size()

def get_name():
  name = input('Can I get your name please? ')
  print(f'Thanks, {name}! Your drink will be ready shortly.')

def cup_type():
  res = input('What would you like to use? \n[a] Plastic cup \n[b] Own reusable cup \n')
  if res == 'a':
    return 'Plastic cup'
  elif res == 'b':
    return 'Reusable cup'
  else:
    print_message()
    return cup_type()
def drink_temp():
  res = input('How would you like your drink? \n[a] Hot \n[b] Cold \n')
  if res == 'a':
    return 'Hot'
  elif res == 'b':
    return 'Cold'
  else:
    print_message()
    return drink_temp()

def anothr_drink():
  res = input('Would you like to order an additional drink? \n[a] Yes \n[b] No \n')
  if res == 'a':
    return coffee_add()
  elif res == 'b':
    return 'with no additional drink'
  else:
    print_message()
    return anothr_drink()

def coffee_add():
  print("What would be your other drink?")
  size = get_size()
  drink_type = get_drink_type()
  cup = cup_type()
  temp = drink_temp()
  return(f"And a {size} {temp} {drink_type}! In a {cup}.")

def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  cup = cup_type()
  temp = drink_temp()
  add = anothr_drink()
  print(f"Alright, that's a {size} {temp} {drink_type}! In a {cup}.")
  print(add)
  get_name()



# Call coffee_bot()!
coffee_bot()



def ask_currency(country_currency):
  country_length = len(country_currency)
  while 1:
    try:
      inp = int(input("#: "))
      if inp > country_length or inp< 1:
        print("Choose a number from the list.")
      else:
        print(country_currency[inp-1]['country'])
        break
    except ValueError:
      print("That wasn's a number.")
  return country_currency[inp-1]['currency']

def ask_amount():
  while 1:
    try:
      inp = int(input("#: "))
      if inp<0:
        print("Unvalid input. Please try again")
      else:
        break
    except ValueError:
      print("\nThat wasn's a number.")
  return inp

def get_input(country_currency):
  print("\nWhere are you from? Choose a country by number. \n")
  from_currency = ask_currency(country_currency)
  print("\nNow choose another country.\n")
  to_currency = ask_currency(country_currency)
  print(f"\nHow many {from_currency} do you want to convert to {to_currency}?\n")
  amount = ask_amount()
  return {'from_cur' : from_currency, 'to_cur': to_currency, 'amount' : amount}
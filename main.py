import os
from babel.numbers import format_currency
from extract_currency import get_country_currency
from get_input import get_input
from convert_currency import convert_currency

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""


def show_interface(country_currency):
  country_length = len(country_currency)
  for i in range(country_length):
    print(f"# {i+1} {country_currency[i]['country']}")

def main():

  country_currency = get_country_currency()
  show_interface(country_currency)
  inputs = get_input(country_currency)
  amounts = convert_currency(inputs)
  if amounts is not None:
    print(f"{format_currency(amounts['from_amount'], amounts['from_cur'], locale='ko_KR')} is {format_currency(amounts['to_amount'], amounts['to_cur'], locale='ko_KR')}")

main()
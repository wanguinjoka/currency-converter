import argparse
import csv
import requests
import json

# Using Argparse module to add Currency and language list flags to app

parser = argparse.ArgumentParser(description="Cheap Stocks App", epilog="Enjoy the program! :)")
parser.add_argument('-c', '--currency', help ='display list the Supported currency')
parser.add_argument('-l','--language', help= 'Displays List of supported Languages')

args = parser.parse_args()

# reading and displaying the currency csv file
curr_file = csv.reader(open('Currencies.csv', "r"), delimiter=",")
for row in curr_file:
    if args.currency:
        print(row)  
        
# reading and displaying the language csv file
lang_file = csv.reader(open('Languages.csv', "r"), delimiter=",")
for cols in lang_file:
    if args.language:
        print (cols)
        
def main():
    api_url_end='http://data.fixer.io/api/latest?access_key=0722e5bf94e83d392f37e7bb90ee6056' 

# fetching json data from fixer.io api
    response=requests.get(api_url_end)
 
# checking user input on prefered language
    language=input('Enter your Prefered language : ') or 'English'
    print(language)
    for row in lang_file:
        if language == row[1]:
            print(row)
        else:
            print('language not supported')

# checking whether users input is in csv supported currencies
    while True:
        try:
            base_currency=input('Enter your Prefered currency : ').upper()
            for row in curr_file:
                if base_currency ==row[2] :
                    print(row)
                else:
                    print('Currency not found')
            break
        except ValueError:
            print('Currency is not supported:')

# curreny set to default usd
    convert_to='USD'

#error handling of amount input
    while True:
        try:
            amount_to_convert=int(input("Enter the amount to buy stock:"))
            break
        except ValueError:
            print('Invalid number. Try again')   
    
 # function to convert currenies  
    def currency_convertor(base_currency,currency_to,amount):
#  Exchange rates delivered by the Fixer API are by default relative to EUR. Therefore, i first convert to eur then to USD
        rate=response.json()['rates'][base_currency]
        amount_in_EUR=amount/rate
        result=round(amount_in_EUR*(response.json()['rates'][currency_to]), 2)
        
        print('The current price for AAPL is', result,'USD')

     
    currency_convertor(base_currency,convert_to,amount_to_convert)

if __name__=='__main__':
    main()

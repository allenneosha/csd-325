# Neosha Allen
# 7/19/2026
# Module 8.2 assignment
# This programs includes a dictonary
# of stocks, asking the user to enter a stocks ticker
# symbol displaying the price of the stocks

# this handles all validating and lookup in dictonary
def lookup_stock(stocks):
    
    while True:
        input_ticker = input("Enter the ticker symbol you would like to lookup: ").strip()
        
        # this part of the program validates user input, checks to see if the input is empty
        if not input_ticker:
            print("Input cannot be empty. Please try again.\n")
            continue
         # this part checks for numbers in user input   
        if any(char.isdigit() for char in input_ticker):
            print("Invalid Input! Ticker symbols cannot contain numbers. Please try again.\n")
            continue
            
        # converts to uppercase to match dictionary keys securely
        input_ticker = input_ticker.upper()
        
        # this part of the program searches the dictionary
        if input_ticker in stocks:
            print("\n----------Stock Ticker And Price Lookup--------")
            print(f"Stock Ticker: {input_ticker} | Price: ${stocks[input_ticker]:.2f}\n")
            break  
        else:
            print(f"The stock ticker symbol '{input_ticker}' was not found. Please try again.\n")
            break

def main():
    # dictionary of 10 ticker symbols and stock prices
    stocks = {
        "AAL": 14.98, "ALIT": 21.74, "BTC": 28.38, "CI": 281.45, "EBAY": 112.06,
        "NKE": 43.76, "FIG": 23.95, "FIVE": 202.35, "GAP": 20.35, "HPQ": 24.84
    }
    
    while True:
        lookup_stock(stocks)
        
        # asking the user if they want to look up another ticker symbol
        repeat = input("Would you like to look up another ticker symbol? (type Y to continue or"
        " anything else exits the program): ").strip().upper()
        
        if repeat != 'Y':
            print("Exiting this program now. Goodbye!")
            break

main()
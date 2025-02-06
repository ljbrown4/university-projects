#
# ps6pr4.py (Problem Set 6, Problem 4)
#
# TT Securities    
#
# Computer Science 111
#

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.
    print('(3) Find the average price')
    print('(4) Find the min price and its day')
    print('(5) Find the max single-day change and its day')
    print('(6) Test a threshold')
    print("(7) Your investment plan")

    print('(8) Quit')

#prompt 0
def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

#prompt 1
def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

#prompt 2
def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.

#prompt 3
def avg_price(prices):
    '''returns price of a list of prices
        input: prices is a list of 1 or more numbers'''
    total = 0
    for i in range(len(prices)):
        total += prices[i]
    avg = total/len(prices)
    return avg


#prompt 4
def min_day(prices):
    '''returns the day, as a number, of the lowest price from a list of prices
        input: prices is a list of 1 or more numbers'''
    min = prices[0]
    minday = 0
    for i in range(len(prices)):
        if prices[i] < min:
            min = prices[i]
            minday = i
    return minday

#prompt 5
def max_change_day(prices):
    '''returns the day of the greatest price change
        input: prices is a list of 2 or more numbers'''
    maxchange = 0
    day = 0
    for i in range(len(prices)-1):
        change = (prices[i+1]-prices[i])
        if change > maxchange:
            maxchange = change
            day = i + 1
    return day


#prompt 6
def any_above(prices, threshold):
    '''returns True if a number in the list is greater than the threshold, and False otherwise
        inputs: prices is a list of 1 or more numbers, threshold is a number'''
    for x in prices:
        if x > threshold:
            return True
    return False
    

#prompt 7
def find_tts(prices):
    '''finds the best day to buy, sell, and gives you the profit made as a list
        input: prices is a list of 2 or more numbers'''
    buyday = 0
    sellday = 1
    length = len(prices)
    prof = prices[1] - prices[0]
    
    for d1 in range(length):
        for d2 in range(d1, length):
            new_prof = prices[d2] - prices[d1]
            if new_prof > prof:
                buyday = d1
                prof = new_prof
                sellday = d2
    returnlist = [buyday, sellday, prof]
    return returnlist
            
                
            
    
    
    
    
        




def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            avg = avg_price(prices)
            print('The average price is', avg)
        elif choice == 4:
            minday = min_day(prices)
            minprice = prices[minday]
            print("The min price is", minprice, "on day", minday)
        elif choice == 5:
            day = max_change_day(prices)
            price1 = prices[day - 1]
            price2 = prices[day]
            print('The max single-day change occurs on day', day, 
                  'when the price goes from', price1, 'to', price2)  
        elif choice == 6:
            threshold = int(input("Enter the threshold: "))
            finder = any_above(prices, threshold)
            if finder == True:
                print("There is at least one price above", threshold)
            else:
                print("There are no prices above", threshold)
        elif choice == 7:
            tts_f = find_tts(prices)
            buy = tts_f[0]
            sell = tts_f[1]
            prof = tts_f[2]
            print(" Buy on day", buy, "at price", prices[buy])
            print('Sell on day', sell, 'at price', prices[sell])
            print('Total profit:', prof)
            
            
            
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')

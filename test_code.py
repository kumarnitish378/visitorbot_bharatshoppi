import numbers
import requests
import time



url = "https://bharatshoppi.com/"

def increase_visitor(num=50, interval=1):
    for itre in range(num):
        try:
            response = requests.get(url)
            print("Response Code: {}".format(response.status_code))
            if response.status_code == 200:
                print("Success: {}".format(itre+1))
            time.sleep(interval)
        except KeyboardInterrupt:
            print("program interrupted")
            break
        except:
            print("Error")
            pass
        
if __name__ == "__main__":
    print('''
___________
Welcome to the visitor increase program
Author: Nitish Kumar
License: copyright 2022 bharatshoppi.com
Note: This program will increase the visitor of the website and will be used for testing purpose

(press ctrl+c to stop)
___________
          ''')
    for _ in range(3):
        try:
            number_of_itres = int(input("number of iterations/visitor: "))
            intervals = float(input("interval between each iteration (in second): "))
            if number_of_itres > 500:
                print("max number of iterations is 500")
                number_of_itres = 500
            if number_of_itres == 0:
                print("Please enter a valid number")
            else:
                increase_visitor(number_of_itres)
                print("Done")
                print("Now you can close this window and open the website in your browser and check the visitor in the footer section")
                break
        except:
            print("Please enter a valid number")
    
import os
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates

def plot_graph():
    """ Plot time-price graph of a product """
    path = os.getcwd()
    data = pd.read_csv('{0}/cache/products.csv'.format(path))
    item_name = data['ItemName']
    item_id = data['ItemId']

    while(True):
        j = 1
        for i in item_name:
            print(j, "Product : ", i)
            j += 1

        print(j, " to exit..")
        op = int(input("Choose product : "))

        if op == j:
            exit(0)

        elif op > j or op < 1:
            print("Invalid option!!")
            ch = input("Try again?? [Y/n] : ")
            if ch == 'n' or ch == 'N':
                break

        else:
            product_file = item_id[op-1]
            data = pd.read_csv('{0}/cache/{1}'.format(path, product_file))
            price_data = data['Date-time']
            price = data['Price']
            product_name = data['Name']

            data['Date-time'] = pd.to_datetime(data['Date-time'].astype(str), format="%Y-%m-%d %H:%M")

            plt.plot_date(price_data, price, linestyle="solid", label=product_name[0])
            plt.gcf().autofmt_xdate()
            plt.ylabel("Price")
            plt.xlabel("Date")
            plt.title(product_name[0])
            plt.show()


def main():
    plot_graph()

if __name__ == "__main__":
    main()

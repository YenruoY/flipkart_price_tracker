#!/usr/bin/python

import re
import os
import csv
import datetime
import requests
from bs4 import BeautifulSoup

def scrape_price(link):
    """ Scrape price from the webpage data object """
    soup = BeautifulSoup(link.text, 'html.parser')
    tmp_price = soup.find('div', {'class': '_30jeq3 _16Jk6d'})
    price = tmp_price.text
    price = price.replace('₹','') 
    price = price.replace(',','') 
    return int(price)


def get_item_id(link):
    """ Extract itemId from the link of the product """
    item_id = re.search(r"(?<!\w)itm\w+", link)
    return item_id

def get_item_name(link):
    """ Scrape product name form the webpage """
    soup = BeautifulSoup(link.text, 'html.parser')
    name = soup.find('span', {'class': 'B_NuCI'})
    return name.text

def check_links():
    """ Checks for links.txt file """
    path = ""   # Paste the path here
    if os.path.exists('{0}/links.txt'.format(path)):
        fo = open("{0}/links.txt".format(path), "r")
        lines = fo.readlines()
        fo.close()
        return lines
    else:
        #print("File doesn't exist. Create a file with the name 'links.txt'")
        return -1


def main():
    """ Main function """

    file_ob = check_links()
    if file_ob == -1:
        exit(-1)
    else:
        rows = []
        for i in file_ob:
            #print("Fetching page data.. Please wait..")
            line = i.strip()
            data = requests.get(line)
            price = scrape_price(data)

            item_id = get_item_id(line)
            item_id = item_id.group()
            item_name = get_item_name(data)

            # Current time
            current_time = datetime.datetime.now()

            path = ""   # Past the path here
            #print("Checking cache files...")
            if os.path.exists('{0}/cache/{1}'.format(path,item_id)):
                row = [item_id, price, current_time, item_name]
                with open('{0}/cache/{1}'.format(path,item_id), 'a') as f:
                    write = csv.writer(f)
                    write.writerow(row)

            else:
                fields = ['ItemId', 'Price', 'Date-time', 'Name']
                row = [item_id, price, current_time, item_name]
                with open('{0}/cache/{1}'.format(path,item_id), 'a+') as f:
                    write = csv.writer(f)
                    write.writerow(fields)
                    write.writerow(row)

                #print("Updating item prices...")
                if not os.path.exists('{0}/cache/products.csv'.format(path)):
                    #print("File 'products.csv' does not exist, hence creating..")
                    product_fields = ['ItemId', 'ItemName']
                    product_row = [item_id, item_name]
                    
                    with open('{0}/cache/products.csv'.format(path), 'a+') as f:
                        write = csv.writer(f)
                        write.writerow(product_fields)
                        write.writerow(product_row)
                else:
                    product_row = [item_id, item_name]
                    with open('{0}/cache/products.csv'.format(path), 'a') as f:
                        write = csv.writer(f)
                        write.writerow(product_row)
                    

if __name__ == "__main__":
    main()
    


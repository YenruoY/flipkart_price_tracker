# Flipkart price tracker using Python
Tracks the price of your flipkart items. 
This tool runs in the background using crontab and scrapes the price of a flipkart products time to time and saves the data to local files which can be used to plot a graph for each of your products.
This tool is <b>only for linux</b>(for now). 

# Workings
The links of the products must be saves in the file named <b>links.txt</b> to start to track their price. Then a cronjob must be added to let the script run in the background.

# Instructions 

1. First run the `set_path.py` file. And copy just the path.

1. Open `flipkart_track.py` file and paste the path at line 34 and 70 in between the double quotes.

1. Copy your product links in the file `links.txt` one link in each line.

1. Run `flipkart_track.py` file manually to check if everything is working without an error.

1. In terminal, run the command `crontab -e` then edit the file and save.
	- My cronjob which runs at the start of every hour :

	```
	0 * * * * /usr/bin/python /path/to/flipkart_track.py
	```
	- You can also use [https://cron.help](https://cron.help) to generate cronjob easily.

1. Sit back and relax or do someting else. 

1. After some hour the program may have collected product price data automatically.

1. Now run the `plot_graph.py` file to view the time-price graph of your product.

**Note :** Run the `flipkart_track.py` manually first to check if everything is working properly. If everything works, you will see some files in the cache folder.

# Requirments
```
1. re 
2. requests
3. BeautifulSoup
4. Matplotlib
5. Pandas
```

# Note 
<b>This tool is still in development.</b>

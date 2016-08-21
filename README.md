# Gitam Result Scraper

Python script to scrape Gitam Result 

* Here the [cse1.py](https://github.com/shubhamc183/GitamResultScrapper/blob/master/cse1.py) and [cse2.py](https://github.com/shubhamc183/GitamResultScrapper/blob/master/cse2.py) are to files which scrape the result of CSE batch 2014-2018 of semester 1st,2nd,3rd and 4th sem ,total 21780 rows will be saved,divided into two files because of maximum post requests ,2500+ requests, will be exceeded.

* Use [result.py](https://github.com/shubhamc183/GitamResultScrapper/blob/master/cse2.py) just to see results of a particular semester and id and not need MySql database.


Requiremnts
* Python 3.4

```sh
$ sudo apt-get python3
```
* [MySql Database](http://www.tutorialspoint.com/mysql/mysql-installation.htm)

Python Packages
 * Install pip

 ```sh
$ sudo apt-get install python3-pip
```

 * Requests
  
 ```sh
 $ sudo pip3 install requests
 ```
 * BeautifulSoup
 
 ```sh
 $ sudo pip install beautifulsoup4
 ```
 * MySQLdb
  
 [From here](http://www.tutorialspoint.com/python/python_database_access.htm), it seems mysql module is not supported by python3 anymore


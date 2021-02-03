import requests
from bs4 import BeautifulSoup
import sys

def github(name):
    url=f"https://api.github.com/users/{name}/repos"
    print("working")
    page=requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')

    sys.stdout= open('output.txt','w')
    print(soup.text)

def clean_data():
    """""
    changing some words to correct form
    """""
    f1 = open('output.txt', 'r')
    f2 = open('file2.txt', 'w')
    checkWords = ("true", "false", "null")
    repWords = ("True", "False", '""' )

    for line in f1:
        for check, rep in zip(checkWords, repWords):
            line = line.replace(check, rep)
        f2.write(line)
    f1.close()
    f2.close()


github(name='UVvirus')
clean_data()
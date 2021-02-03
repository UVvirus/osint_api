from bs4 import BeautifulSoup
import requests
import sys
from github import Github
import validators
from svn.remote import RemoteClient
import csv
import numpy as np
import pandas as pd

def acces_repo():
    print("befr acc tok")
    ACCESS_TOKEN="YOUR GITHUB ACCESS TOKEN HERE"
    print("after acc tok")
    github_obj= Github(ACCESS_TOKEN)
    word=input("ENter the keywords to search:")
    word=[key.strip() for key in word.split(',')]
    print(word)

def github(name):
    url=f"https://api.github.com/users/{name}/repos"
    print("working")
    page=requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')

    sys.stdout= open('output.csv','w')
    print(soup.text)
    #sys.stdout.close()
    print("comp")

def filter(name):
    data = pd.read_csv(f'https://api.github.com/users/{name}/repos')
    data_col = data.columns
    matching = [s for s in data_col if "html_url" in s]
    print(matching)
    download(matching)


def download(matching):
    if 'master' in matching:
        matching = matching.replace('master', 'test')
    remote = RemoteClient(matching)
    remote.export('fileout')
def main():
    name=input("Enter the name:")
    filter(name)
    github(name)
    acces_repo()



if __name__ == '__main__':
    main()

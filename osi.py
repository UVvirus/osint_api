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

def check_acl():
    print("inside acl")
    PREDEFINED_URI=["http://acs.amazonaws.com/groups/global/AllUsers",
    "http://acs.amazonaws.com/groups/global/AuthenticatedUsers"]
    bucket='wordlist.txt'
    list_of_buckets=[]
    s3=boto3.resource('s3')

    bucket_acl = s3.BucketAcl(bucket)
    bucket_acl.load()


    for granted in bucket_acl.grants:
        if 'URI' in granted['Grantee']:

            if granted["Grantee"]["URI"] == PREDEFINED_URI:
                list_of_buckets.append(granted["Permission"])
    return list_of_buckets

def check_without_creds(bucket_url):
    request=requests.head(bucket_url)
    if request.status_code==200:
        soup = BeautifulSoup(request.content, 'html.parser')
        print(soup.prettify())
   
    
    
github(name='UVvirus')
clean_data()
check_acl()
check_without_creds(bucket_url)

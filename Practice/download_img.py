# driver = webdriver.Chrome('C:\Users\DELL\Downloads\Programs\chromedriver.exe')

#Importing stuff
import os
import urllib.request as ulib
from bs4 import BeautifulSoup as Soup
#The library that will turn a weird string library that we'll scrap from Google into one that we can read
import ast

from selenium import webdriver

# chromePath=r'C:\Windows.old\Users\Ivan\MyPythonScripts\Drivers\chromedriver.exe'
chromePath=r'C:\Users\DELL\Downloads\Programs\chromedriver.exe'


driver = webdriver.Chrome(chromePath)

search = input("Search for: ")
num = input("Number of images: ")

URL = 'https://www.google.ru/search?q='+ search +'&num=1000&newwindow=1&safe=off&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiGueO-uN7eAhXCFiwKHTiYDlUQ_AUIDigB&biw=1440&bih=789'
directory = 'dataset'


def getURLs(URL):
    driver.get(URL)
    a=input("Press Enter to download image")
    page = driver.page_source
    print(page)
    soup = Soup(page, 'lxml')
    desiredURLs = soup.findAll('div', {'class':'rg_meta notranslate'})
    ourURLs = []
    for url in desiredURLs:
        theURL = url.text
        theURL = ast.literal_eval(theURL)['ou']

        ourURLs.append(theURL)
    return ourURLs[:int(num)]



def save_images(URLs, directory):

    if not os.path.isdir(directory):
        os.mkdir(directory)

    for i, url in enumerate(URLs):
        savePath = os.path.join(directory, '{:06}.jpg'.format(i))
        print("Downloading... {}/{} ========================== {}%".format(URLs.index(url)+1, len(URLs), (URLs.index(url)+1)*100/len(URLs)))

        try:
            ulib.urlretrieve(url, savePath)

        except:
            print('I failed with', url)


URLs = getURLs(URL)

save_images(URLs, directory)

# for url in URLs:
    # print(url)


print("\nDownload Finish")
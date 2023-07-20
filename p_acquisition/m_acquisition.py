#Imports
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from dotenv import dotenv_values

#Install Chromevriver selenium
path = '../requirements/chromedriver'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

#Configurate dotenv to hide password
config = dotenv_values("../.env")
mar_password = config["PASSWORD"]

#Log into Goodreads with Selenium
url = 'https://www.goodreads.com/ap/signin?language=en_US&openid.assoc_handle=amzn_goodreads_web_na&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.goodreads.com%2Fap-handler%2Fsign-in&siteState=5343dd7ffb96ad0340e3a83b80aba5dc'
driver.get(url)
driver.maximize_window()
username = driver.find_element(By.XPATH, "//input[@type='email']")
username.send_keys("margamontv@gmail.com")
password = driver.find_element(By.XPATH, "//input[@type='password']")
password.send_keys(mar_password)
sign_in = driver.find_element(By.XPATH, "//input[@id='signInSubmit']")
sign_in.click()

#Get the genres urls containing 50 books per page per genre
#Create a genre list with the gernes and a page list with the pages
genre_list = ['adult-fiction', 'biography', 'business', 'chick-lit', 'childrens', 
              'comics', 'contemporary', 'crime', 'fantasy', 'fiction', 
              'graphic-novels', 'historical-fiction', 'history', 'horror', 'humor', 
              'lgbt', 'literary-fiction', 'memoir', 'mystery', 'new-adult', 
              'non-fiction', 'paranormal', 'poetry', 'romance', 'science', 
              'science-fiction', 'self-help', 'suspense', 'thriller', 'travel', 'young-adult']

genre_pages = ['1', '2', '3', '4', '5',
              '6', '7', '8', '9', '10',
              '11', '12', '13', '14', '15',
              '16', '17', '18', '19', '20']

#Create a for loop and dictionaries containing the main urls. This urls contain 50 books each
list_url_genres = []

for g in genre_list:
    for p in genre_pages:
        base_url = 'https://www.goodreads.com/shelf/show/'
        pages_url = f'?page={p}'
        full_url = base_url + g + pages_url
        dict_url = {}
        dict_url['genre'] = g
        dict_url['url'] = full_url
        list_url_genres.append(dict_url)  

# Convert my list of dictionaries (JSON) into a Pandas dataframe
genres_urls = pd.DataFrame(list_url_genres)

#Obtain the books urls form the genres urls
#Create an empty list for my dictionaries
list_url_books = []

#create a for loop to iterate along the genres urls
for i in range(len(genres_urls['url'])):   # [0,1,2,...,620]
    driver_content = driver.get(genres_urls['url'][i])
    genre = genres_urls['genre'][i]
    try:
        books_elements = driver.find_elements(By.XPATH, "//a[@class='bookTitle']")
    except:
        continue
    
    for element in books_elements:
        dict_url_books = {}
        try:
            books_url = element.get_attribute("href")
            #print(books_url)
            dict_url_books['book_url'] = books_url
            dict_url_books['genre'] = genre
        except:
            continue

        list_url_books.append(dict_url_books)

# Convert my list of urls (JSON) into a Pandas dataframe
books_urls = pd.DataFrame(list_url_books)

#Extract the relevant info from my books_urls and append to dictionary
#create an empty list to store my dictionaries
goodreads_books_list = []

#Iterate the urls through a for loop
for i in range(len(books_urls_2['book_url'])):   # [0,1,2,...,620]
    genre = books_urls_2['genre'][i]
    url = books_urls_2['book_url'][i]

#Create a new dictionary to store the info extracted
    goodreads_books = {}

#Iterate through the urls
    new_driver_content = driver.get(url)

#Extract the relevant info from each book and append to dictionary
    #Title info
    try:
        titles = driver.find_element(By.XPATH, "//h1[@class='Text Text__title1']").text
        goodreads_books['Title'] = titles
    except:
        goodreads_books['Title'] = 'error' 
    #Author info
    try:
        authors = driver.find_element(By.XPATH, "//span[@class='ContributorLink__name']").text
        goodreads_books['Author'] = authors
    except:
        goodreads_books['Author'] = 'error'
    #Rating info
    try:
        ratings = driver.find_element(By.XPATH, "//div[@class='RatingStatistics__rating']").text
        goodreads_books['Rating'] = ratings
    except:
        goodreads_books['Rating'] = 'error' 
    #Ratings count info
    try:
        ratings_count = driver.find_element(By.XPATH, "//span[@data-testid='ratingsCount']").text
        goodreads_books['Ratings count'] = ratings_count
    except: 
        goodreads_books['Ratings count'] = 'error'
    #Reviews count info
    try:
        reviews_count = driver.find_element(By.XPATH, "//span[@data-testid='reviewsCount']").text
        goodreads_books['Reviews count'] = reviews_count
    except: 
        goodreads_books['Reviews count'] = 'error'
    #Pages info
    try:
        pages = driver.find_element(By.XPATH, "//p[@data-testid='pagesFormat']").text
        goodreads_books['Pages'] = pages
    except:
        goodreads_books['Pages'] = 'error'
    #First published info
    try:
        first_published = driver.find_element(By.XPATH, "//p[@data-testid='publicationInfo']").text
        goodreads_books['First published'] = first_published
    except:
        goodreads_books['First published'] = 'error'
    #Cover image info
    try:
        cover_image = driver.find_element(By.XPATH, "//img[@class='ResponsiveImage']")
        image_url = cover_image.get_attribute("src")
        goodreads_books['Cover image'] = image_url
    except:
        goodreads_books['Cover image'] = 'error' 
    
    goodreads_books['Genre'] = genre
    goodreads_books['Book url'] = url
    
    goodreads_books_list.append(goodreads_books)

# Convert my list of urls (JSON) into a Pandas dataframe
goodreads_books_df = pd.DataFrame(goodreads_books_list)

#Convert my df to csv
goodreads_books_df.to_csv('../data/goodreads_books.csv', index=False)
# Book Recommending App - Data Analytics Final Project
![image](https://github.com/MargaMontV/Final-Project-Book-Recommendation/assets/122310638/a4799096-e440-405c-a60e-9b1619a19c9c)
 https://final-project-book-recommendationgi-goodreads.streamlit.app/


## Introduction
Welcome to the Book Recommending App, the final project for the Data Analytics Bootcamp. This app is designed to help users discover their next great read by providing personalized book recommendations based on their preferences. The app utilizes web scraping, data cleaning, and Streamlit for the user interface.

## Project Overview
### Data Collection
To create a diverse and extensive collection of books, I performed web scraping using Selenium from Goodreads. The scraping process covered 31 genres, gathering data on 1,000 books per genre, resulting in a total of 31,000 books.

### Data Cleaning
The collected data underwent a thorough cleaning process to ensure its quality and usability. Steps taken during the data cleaning phase include:

Handling numerical data: Ensuring all numerical data were correctly represented as integers or floats instead of objects.
Error elimination: Removing rows with data errors or missing values to maintain data integrity.
### App Development
The main app was developed using Streamlit, which provides an interactive and user-friendly interface. I initially tested the app's functionality in Jupyter Notebook before implementing it in the main.py file.

### App Features
The Book Recommending App offers the following features:

- Genre Filtering: Users can select their preferred genre from a list of 31 options, narrowing down the book recommendations to their favorite literary category.

- Length Preference: Users can choose between long or short books, filtering the recommendations based on their desired page count (e.g., less than 300 pages or more).

- Popularity Preference: Users can decide whether they want to explore popular books or hidden gems. The app filters books based on review counts (e.g., less than 100,000 reviews or more).

- Recency Preference: Users can opt for recent or classical books. The app filters books based on their publication year, with the option to view books from the last five years.

- Book Selection: After applying the desired filters, the app presents the user with three book choices. Each book is accompanied by its cover image, title, and author. Users can click on a cover to be redirected to the book's Goodreads page for more information.

- Shuffle Option: If the user isn't satisfied with the initial recommendations, they can shuffle the book options to receive a new set of choices.

## How to Use the App
- Access the Book Recommending App through the provided Streamlit link: https://final-project-book-recommendationgi-goodreads.streamlit.app/

- On the app's interface, you will find a series of dropdown menus and options for selecting your preferences.

- Start by choosing your favorite genre from the list of 31 genres available.

- Next, specify your preferred book length (short or long).

- Select your reading preference based on popularity (popular or hidden gem).

- Finally, choose whether you want to explore recent books or classical literature (last five years or older).

- Once all preferences are set, click on the "Get Recommendations" button.

- The app will display three book recommendations matching your selected criteria, each with its cover, title, and author.

- If none of the initial recommendations catch your interest, you can click on the "Shuffle" button to get a new set of book options.

- Click on any book cover to be redirected to the respective book's page on Goodreads for additional details and user reviews.

## Conclusion
The Book Recommending App aims to make the book selection process more enjoyable and personalized for readers. By combining web scraping, data cleaning, and Streamlit, this project offers an interactive platform for discovering new and exciting reads. Feel free to explore the app, discover new books, and embark on captivating literary journeys!

#Import
from p_wrangling import m_wrangling as mwr

#Read the csv that I obtained from the web scraping
books_wrangling = pd.read_csv('../data/goodreads_books.csv')

#Drop errors applying the function
books_wrangling = mwr.drop_error(books_wrangling, 'Title', 'error')
books_wrangling = mwr.drop_error(books_wrangling, 'Author', 'error')
books_wrangling = mwr.drop_error(books_wrangling, 'Rating', 'error')
books_wrangling = mwr.drop_error(books_wrangling, 'Ratings count', 'error')
books_wrangling = mwr.drop_error(books_wrangling, 'Reviews count', 'error')
books_wrangling = mwr.drop_error(books_wrangling, 'Pages', 'error')
books_wrangling = mwr.drop_error(books_wrangling, 'First published', 'error')
books_wrangling = mwr.drop_error(books_wrangling, 'Cover image', 'error')
books_wrangling = mwr.drop_error(books_wrangling, 'Genre', 'error')
books_wrangling = mwr.drop_error(books_wrangling, 'Book url', 'error')

#Apply the spliting function
book_filter_rating_pages_df = mwr.wrangling_split(books_wrangling, ['Ratings count', 'Reviews count', 'Pages'], " ", 0)
book_filter_year_df = mwr.wrangling_split(book_filter_rating_pages_df, ['First published'], ",", 1)

#Use again the drop_error function for books that have no pages
book_filter_rating_pages_df = mwr.drop_error(book_filter_rating_pages_df, 'Pages', 'Unknown')
book_filter_rating_pages_df = mwr.drop_error(book_filter_rating_pages_df, 'Pages', 'Paperback')
book_filter_rating_pages_df = mwr.drop_error(book_filter_rating_pages_df, 'Pages', 'Hardcover')
book_filter_rating_pages_df = mwr.drop_error(book_filter_rating_pages_df, 'Pages', 'Audible')
book_filter_rating_pages_df = mwr.drop_error(book_filter_rating_pages_df, 'Pages', 'Audiobook')
book_filter_rating_pages_df = mwr.drop_error(book_filter_rating_pages_df, 'Pages', 'ebook')
book_filter_rating_pages_df = mwr.drop_error(book_filter_rating_pages_df, 'Pages', 'Audio')
book_filter_rating_pages_df = mwr.drop_error(book_filter_rating_pages_df, 'Pages', 'Kindle')

#Apply the replace function
book_filter_replace_df = mwr.wrangling_replace(book_filter_year_df, ['Ratings count', 'Reviews count'], ",", "")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "adult-fiction", "Adult Fiction")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "biography", "Biography")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "business", "Business")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "chick-lit", "Chick-Lit")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "childrens", "Childrens")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "comics", "Comics")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "contemporary", "Contemporary")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "crime", "Crime")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "fantasy", "Fantasy")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "fiction", "Fiction")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "graphic-novels", "Graphic Novels")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "historical-Fiction", "Historical Fiction")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "history", "History")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "horror", "Horror")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "humor", "Humor")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "lgbt", "LGBT")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "literary-Fiction", "Literary Fiction")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "memoir", "Memoir")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "mystery", "Mystery")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "new-adult", "New Adult")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "non-Fiction", "Nonfiction")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "paranormal", "Paranormal")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "poetry", "Poetry")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "romance", "Romance")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "science", "Science")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "Science-Fiction", "Science Fiction")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "self-help", "Self-Help")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "suspense", "Suspense")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "thriller", "Thriller")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "travel", "Travel")
genre_filter_replace_df = mwr.wrangling_replace(book_filter_replace_df, ['Genre'], "young-adult", "Young Adult")

#Apply the casting function
book_filter_to_int_df = mwr.wrangling_to_type(genre_filter_replace_df, ['Ratings count', 'Reviews count', 'Pages', 'First published'], int)
book_filter_to_int_df = mwr.wrangling_to_type(genre_filter_replace_df, ['Rating'], float)

#Get my df into a csv
book_filter_to_int_df.to_csv('../data/books_clean.csv', index=False)
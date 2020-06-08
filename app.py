
from selenium import webdriver

from pages.quotes_page import QuotePage, InvalidTagForAuthorError

try:
    author = input("Enter the author you want quotes from: ")
    tag = input('Enter your tag: ')

    chrome = webdriver.Chrome(executable_path="/Users/kyleortega/Downloads/chromedriver")
    chrome.get("http://quotes.toscrape.com/search.aspx")
    page = QuotePage(chrome)

    print(page.search_for_quotes(author.title(), tag.lower()))

except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("An unknown error occurred. Please try again.")


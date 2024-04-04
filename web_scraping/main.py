import re
import requests

from bs4 import BeautifulSoup

URL = "https://habr.com/ru/articles/"
BASE_URL = "https://habr.com"
COUNT_PAGE = 3
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'ntws', 'ntw3']


def make_soup(url):
    # raw data
    response = requests.get(url)

    # html data
    htmlData = response.content

    return BeautifulSoup(htmlData, "html.parser")


def get_text(url):
    raw_text = ""

    # make borsch
    borsch = make_soup(url)
    data = borsch.find_all(
        'div',
        class_='article-formatted-body article-formatted-body article-formatted-body_version-2')

    # get paragraphs
    if data:
        paragraphs = data[0].find_all('p')
        raw_text = [t.text for t in paragraphs]

    return "".join(raw_text)


def find_text(text):
    find_words = []

    for word in KEYWORDS:
        result = re.findall(word, text, re.IGNORECASE)
        if result:
            find_words.append(word)

    return find_words


def scraping_page(url):
    count_articles = 0

    # make soup
    soup = make_soup(url)

    # parsing data
    articles = soup.find_all('div', class_='tm-article-snippet tm-article-snippet')

    for article in articles:
        # get link
        link_title = article.find(class_='tm-title__link')

        # find keywords in text
        article_text = get_text(f"{BASE_URL}{link_title['href']}")
        match_keywords = find_text(article_text)

        if match_keywords:
            count_articles += 1

            article_title = article.find('h2', class_='tm-title tm-title_h2').text
            author_title = article.find(class_='tm-user-info__username')
            datatime_title = article.find('time')

            print(f"Title: {article_title}")
            print(f"Link: {BASE_URL}{link_title['href']}")
            print(f"Author: {author_title.text.strip()}")
            print(f"Author URL: {BASE_URL}{author_title['href']}")
            print(f"Data published: {datatime_title['title']}")
            print("Found word(s):",  *match_keywords)
            print()

    return count_articles


def main():
    found_pages = 0

    if COUNT_PAGE > 1:
        for p in range(1, COUNT_PAGE + 1):
            print(f"=== Scraping page: {p} ===")
            print()
            found_pages += scraping_page(f"{URL}page{p}/")
    else:
        found_pages = scraping_page(URL)

    print(f"Total found page(s): {found_pages}")


if __name__ == '__main__':
    main()

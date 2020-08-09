import requests
from bs4 import BeautifulSoup
import sys


def percent_encoding(encoding=None):
    url_escape = {'<': '%3C', '>': '%3E', '#': '%23', '%': '%25',
                  '{': '%7B', '}': '%7D', '|': '%7C', '\\': '%5C',
                  '^': '%5E', '~': '%7E', '[': '%5B', ']': '%5D',
                  '`': '%60', ';': '%3B', '/': '%2F', '?': '%3F',
                  ':': '%3A', '@': '%40', '=': '%3D', '&': '%26',
                  '$': '%24'}
    encode = []
    for symbol in encoding:
        if symbol in url_escape:
            encode.append(url_escape[symbol])
        else:
            encode.append(symbol)
    return ''.join(encode)


def get_questions(tagged=None, total=0):
    page = 1
    count = 0
    while True:
        r = requests.get("https://api.stackexchange.com/2.2/questions?page={}"
                         "&pagesize=50&order=desc&sort=votes&tagged={}"
                         "&site=stackoverflow".format(page, tagged))
        data = r.json()
        for question in data['items']:
            print("Title: {}\nLink: {}\n".format(
                  question['title'], question['link']))
            count += 1
            if count == total:
                break
        if count == total:
            break
        elif data['has_more'] is True:
            page += 1
        elif data['has_more'] is False:
            break


def main():
    tagged = percent_encoding(' '.join(sys.argv[2:]))
    get_questions(tagged, total=int(sys.argv[1]))


if __name__ == '__main__':
    main()

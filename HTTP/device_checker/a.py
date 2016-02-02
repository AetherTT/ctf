import requests
from html.parser import HTMLParser
import sys

req = requests.get("http://useragentstring.com/pages/All/")

last_tag = []

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        last_tag.append(tag)
    def handle_endtag(self, tag):
        if len(last_tag) != 0:
            last_tag.pop()
    def handle_data(self, data):
        if len(last_tag) != 0 and last_tag[-1] == "a":
            print("trying string: '", data, "'")
            headers = {"User-Agent": data}
            res = requests.get("http://devicechecker.training.hackerdom.ru/", headers=headers)
            if not "неправильного" in res.text:
                print("The answer is here:\n", res.text)
                sys.exit("Answer was found")

parser = MyHTMLParser()
parser.feed(req.text)

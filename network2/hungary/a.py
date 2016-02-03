import requests
from html.parser import HTMLParser
import sys

#Did not found better site. It would be greate if some site with a huge list on one page existed.
#Using this site I have to write two parser for two pages
req = requests.get("http://www.gatherproxy.com/proxylistbycountry")

all_proxies_for_country = []

#I always take only first proxy from a list for this country
class SpecificCountryHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        if "PROXY_COUNTRY" in data:
            start_index = data.index("{")
            end_index = data.index("}")
            null = ""
            str_dict = data[start_index:end_index + 1]
            proxy_info_dict = eval(str_dict)
            if proxy_info_dict["PROXY_STATUS"] == "OK" and not proxy_info_dict["PROXY_TYPE"] == "Elite":
                global all_proxies_for_country
                all_proxies_for_country.append(proxy_info_dict)


def some_function_name(d):
    return int(d["PROXY_TIME"])

def get_proxy(link):
    global ip
    ip = "127.0.0.1"
    global port
    port = "80"
    global all_proxies_for_country
    all_proxies_for_country = []

    parser = SpecificCountryHTMLParser()
    country_proxies_page = requests.get(link)
    parser.feed(country_proxies_page.text)

    if len(all_proxies_for_country) > 0:
        print(len(all_proxies_for_country), "got. sorting")
        sorted(all_proxies_for_country, key=some_function_name)
        best_proxy = all_proxies_for_country[0]
        ip = best_proxy["PROXY_IP"]
        port = str(int(best_proxy["PROXY_PORT"], 16))
    else:
        print("no proxies for this country")

    return ip + ":" + port


class MainPageHTMLParser(HTMLParser):
    def __init__(self):
        self.last_tag = []
        self.link = ""
        self.is_list = False
        super(MainPageHTMLParser, self).__init__()

    def handle_starttag(self, tag, attrs):
        self.last_tag.append(tag)
        if tag == "a":
            self.link = attrs[0][1]
        if tag == "ul" and len(attrs) > 0:
            self.is_list = attrs[0][1] == "pc-list"

    def handle_endtag(self, tag):
        if len(self.last_tag) != 0:
            self.last_tag.pop()
        if tag == "ul":
            self.is_list = False

    def handle_data(self, data):
        if self.is_list and len(self.last_tag) > 1 and self.last_tag[-2] == "li" and self.last_tag[-1] == "a":
            print("Now country:", data)
            proxies = {"http": "http://" + get_proxy("http://www.gatherproxy.com" + self.link)}
            global ip
            global port
            print("Trying with proxy: " + ip + ":" + port)
            try:
                res = requests.get("http://hungary.training.hackerdom.ru/", proxies=proxies, timeout=40)
                if "Этот сайт доступен только из определенной страны." in res.text:
                    print("This is not right country")
                else:
                    print("The answer is here:\n", res.text)
            except Exception:
                print("this connection is refused")
            print("\n")

parser = MainPageHTMLParser()
parser.feed(req.text)

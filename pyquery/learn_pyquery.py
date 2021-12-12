# encoding=utf-8
import requests
from pyquery import PyQuery as pq

class PyQueryUtil(object):

    def __init__(self) -> None:
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
        pass

    def get_html(self, url: str):
        response = requests.get(url=url, headers=self.headers)
        # with open("测试网页.html", "wt", encoding='utf-8') as fout:
        #     fout.write(response.text)
        doc = pq(response.text)
        properties_name = doc.css('dd.basicInfo-block basicInfo-left .dt.basicInfo-item name')
        print(properties_name)
        


def main():
    util = PyQueryUtil()
    util.get_html("https://baike.baidu.com/item/%E6%88%90%E9%83%BD/128473")
    pass


if __name__ == "__main__":
    main()
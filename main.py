from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import requests
import time

if __name__ == '__main__':
    url = 'https://www.86cfm.com/tupian/174499.html'
    # 发起请求前，可以让url表示的页面动态加载出更多的数据
    path = r'E:\projects\Study_scrapy\webdriver\chromedriver.exe'
    # 创建无界面的浏览器对象
    bro = webdriver.Chrome(path)
    # 发起url请求
    bro.get(url)
    # 执行js代码（让滚动条向下偏移n个像素（作用：动态加载了更多的电影信息））
    js = 'document.body.scrollTop=1000'
      # 该函数可以执行一组字符串形式的js代码
    for i in range(0, 5):
        time.sleep(5)
        # 截图
        bro.execute_script(js)
    # 使用爬虫程序爬去当前url中的内容
    html_source = bro.page_source  # 该属性可以获取当前浏览器的当前页的源码（html）
    bro.quit()
    soup = BeautifulSoup(html_source)
    picture_labels = soup.find_all("img",class_="videopic lazy")
    for plabel in picture_labels:
        picture_name = plabel.attrs['data-original'][-10: -4]
        src_url = plabel.attrs['src']
        if src_url.endswith(".jpg"):
            break
        response = requests.get(src_url)
        with open("images\{}".format(picture_name), "wb") as fout:
            fout.write(response.content)


# -*- coding: utf-8 -*-
# @Time    : 2019/12/30 16:03
# @Author  : Jesse
# @Email   : jianxiangzhouemail@163.com
# @File    : Setup.py
# @Software: PyCharm

from html_downloader import HtmlDownloader
from html_paraser import HtmlParser

if __name__ == '__main__':
    hd = HtmlDownloader()
    hp = HtmlParser()

    url = r'https://gongshang.mingluji.com/zhejiang/riqi/2019-12-16?page=2'
    html_content = hd.download(url)
    hp.cityparase(html_content)





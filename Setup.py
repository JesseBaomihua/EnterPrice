# -*- coding: utf-8 -*-
# @Time    : 2019/12/30 16:03
# @Author  : Jesse
# @Email   : jianxiangzhouemail@163.com
# @File    : Setup.py
# @Software: PyCharm

from html_downloader import HtmlDownloader
from html_paraser import HtmlParser
import pymysql

conn = pymysql.connect(host='192.168.64.135', port=3306, user='root', passwd='123456', db='comp')
cursor = conn.cursor()


if __name__ == '__main__':
    hd = HtmlDownloader()
    hp = HtmlParser()

    province = 'be'
    comregdate = '2019-12-30'

    url = r'https://gongshang.mingluji.com/jiangsu/riqi/2019-12-23'
    html_content = hd.download(url)
    hp.cityparase(html_content, cursor, province, comregdate)

    conn.commit()  # 提交数据到数据库
    cursor.close()
    conn.close()





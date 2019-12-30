# -*- coding: utf-8 -*-
# @Time    : 2019/12/30 16:03
# @Author  : Jesse
# @Email   : jianxiangzhouemail@163.com
# @File    : Setup.py
# @Software: PyCharm

from html_downloader import HtmlDownloader
from html_paraser import HtmlParser
import pymysql
from date_provider import getAllDayPerYear
import time

conn = pymysql.connect(host='192.168.64.135', port=3306, user='root', passwd='123456', db='comp')
cursor = conn.cursor()


if __name__ == '__main__':
    hd = HtmlDownloader()
    hp = HtmlParser()

    province = 'zhejiang'
    for year in range(2019,1949,-1):
        print(year)
        year_date_list = getAllDayPerYear(year)
        # print(year_date_list)
        for comregdate in year_date_list:
            print(comregdate)
            errcnt = 0
            pagecnt_tmp = 0
            for pagecnt in range(0,1000):

                url = r'https://gongshang.mingluji.com/' + province + r'/riqi/' + comregdate + r'?page=' + str(pagecnt)
                # print(url)
                time.sleep(1)
                pagecnt_tmp = pagecnt
                try:
                    html_content = hd.download(url)
                    hp.cityparase(html_content, cursor, province, comregdate)
                    conn.commit()
                    print(province, comregdate, pagecnt)
                except Exception as e:
                    # print(e)
                    if(pagecnt - pagecnt_tmp == 0):
                        errcnt += 1
                    # print(pagecnt)
                    # print(pagecnt_tmp)
                    # print(errcnt)
                    if(errcnt > 10):
                        break

    conn.commit()  # 提交数据到数据库
    cursor.close()
    conn.close()





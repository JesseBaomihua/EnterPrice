# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from mysql_handler import insert_CompaneyTitle

class HtmlParser(object):

    def cityparase(self, html_content, cursor, province, comregdate):
        # 将html代码从gb2312转码到utf-8
        # html_content = html_content.decode('gb2312', 'ignore').encode('utf-8')
        # soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        # print(html_content)
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        # print(soup)
        # outer_list = []
        soup_citylist1 = soup.find_all('table', 'views-table cols-2')
        # print(soup_citylist[0].tbody)
        soup2 = soup_citylist1[0].tbody
        soup_citylist2 = soup2.find_all('tr')
        # print(soup_citylist2)
        for i in range(0,len(soup_citylist2)):
            soup3 = soup_citylist2[i]
            soup4 = soup3.find_all('td')
            # print(soup4[0].a.attrs['href'])
            # print(soup4[0].a.getText())
            # print(soup4[1].a.getText())

            try:
                companyurl = soup4[0].a.attrs['href']
            except Exception as e:
                companyurl = 'unfound'


            try:
                comname = soup4[0].a.getText()
            except Exception as e:
                comname = 'unfound'


            try:
                comarea = soup4[1].a.getText()
            except Exception as e:
                comarea = 'unfound'

            # print(companyurl)
            # print(comname)
            # print(comarea)

            insert_CompaneyTitle(cursor, province, companyurl, comname, comarea, comregdate)

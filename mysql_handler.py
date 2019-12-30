# -*- coding: utf-8 -*-
# @Time    : 2019/12/30 16:39
# @Author  : Jesse
# @Email   : jianxiangzhouemail@163.com
# @File    : mysql_handler.py
# @Software: PyCharm

def insert_CompaneyTitle(cursor, province, comurl, comname, comarea, comregdate):
    cursor.execute(
        '''insert into `%s`(province, comurl, comname, comarea, comregdate) values("%s","%s","%s","%s","%s")''' %
        ('CompaneyTitle',province, comurl, comname, comarea, comregdate))
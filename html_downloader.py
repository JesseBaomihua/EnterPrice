# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import urllib.error
import time


class HtmlDownloader(object):
    def download(self, url):
        cnt = 0
        if url is None:
            raise Exception('url is None')
        # 输出当前进行下载的url
        # print(url)
        # 伪装浏览器
        req = urllib.request.Request(url, None, {'Cookie': 'AD_RS_COOKIE=20083363',
                                                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                                                     AppleWeb\Kit/537.36 (KHTML, like Gecko)\
                                                      Chrome/58.0.3029.110 Safari/537.36'})

        use_proxy = urllib.request.ProxyHandler({'http': '222.189.190.128:9999'})
        # null_proxy = urllib.request.ProxyHandler()
        if True:
            opener = urllib.request.build_opener(use_proxy)
        else:
            opener = urllib.request.build_opener(null_proxy)
        # 根据上面的开关，安装的opener对象是否带有代理地址
        urllib.request.install_opener(opener)
        html = urllib.request.urlopen(req).read()
        return html



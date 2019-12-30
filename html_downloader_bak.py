# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import urllib.error
import time


class HtmlDownloader(object):
    def download(self, url, errcnt):
        if(errcnt > 5):
            break

        if url is None:
            raise Exception('url is None')
        # 输出当前进行下载的url
        print(url)
        # 伪装浏览器
        request = urllib.request.Request(url, None, {'Cookie': 'AD_RS_COOKIE=20083363',
                                                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                                                     AppleWeb\Kit/537.36 (KHTML, like Gecko)\
                                                      Chrome/58.0.3029.110 Safari/537.36'})
        try:
            with urllib.request.urlopen(request,timeout=1) as response:
                if response.getcode() != 200:
                    # 递归调用
                    return self.download(url,errcnt+1)
                else:
                    return response.read()
        except urllib.error.HTTPError as e:
            print(e)
            time.sleep(5)
            if(errcnt > 5):
                with open('download.err', 'a') as f:
                    f.write(url)
                pass
            else:
                return self.download(url)


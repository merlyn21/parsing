#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import codecs
import openpyxl
import docx
from bs4 import BeautifulSoup
import re
import locale

# from urllib2 import urlopen
# from pprint import pprint

from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font, Side
# from datetime import  *

def get_text(url, re_text):

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            'Sec-Fetch-Mode': 'cors'
          }

    try:
        r = requests.get(url, headers = headers, verify=False, timeout=5)
    except requests.ConnectionError as e:
        print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
        print(str(e))
        return str(e)+' '+url
    except requests.Timeout as e:
        print("OOPS!! Timeout Error")
        print(str(e))
        return str(e) + ' ' + url
    except requests.RequestException as e:
        print("OOPS!! General Error")
        print(str(e))
        return str(e) + ' ' + url

    #pattern = re.compile(re_text)
    reg = re.compile('[^а-яА-ЯЁё .,!?\-\0-9\s]')
    regt = re.compile('[|\n]')
    reel = re.compile('[«»()\n\r\s]')
    reclear = re.compile('[^а-яА-ЯЁё]')

#    print(locale.getpreferredencoding())

    if r.status_code == 200:
        print('Все в норме search!')
        #print (r.encoding)
        if (r.encoding.lower() == "windows-1251"):
            r.encoding = 'cp1251'
            print("1251")
        elif (r.encoding.lower() == "utf-8"):
            r.encoding = 'utf-8'
            print("utf8")
        # else:
        #     print("else")
        #     r.encoding = 'utf-8'


        #'utf-8'

        soup = BeautifulSoup(r.text, 'html.parser')

        #if (r.encoding == "ISO-8859-1"):
            #print(url)
            #print(r.text)

        for tag in soup.find_all('script'):
            tag.clear()

        for tag in soup.find_all('style'):
            tag.clear()

        for tag in soup.find_all(style=True):
            del tag['style']

        #print(soup.get_text())
        #res = soup.findAll('div')
        if re.search("znak.com", url):
            print("nj znak!!!!! -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            res = soup.find('article')
        else:
            res = soup.findAll('div')

#        print(res)
        i = 0
        ch = 100000
        ch_i = 0
        for div in res:
            ##print(re.sub("^\s+|\n|\r|\s+$",'',div.text))
            #print("-=-=-=-=-=-=-=-=-=-")
#            print(div)
            #print(i)
            div_clear = reclear.sub('',div.text)
            re_text_clear = reclear.sub('',re_text)
            if len(div.text) > len(re_text):

                if re.search(re_text_clear, div_clear):
                    #print("000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
                    #print(len(div.text))
                    if len(div.text) < ch:
                        ch = len(div.text)
                        ch_i = i
                        res_text = div.text

            i+=1
        print("ch_i = "+str(ch_i))
        if (ch_i > 0):
            #f_t = res[ch_i]    #.get_text()
            #cl_t = f_t#regt.sub('', f_t)
            # print(res[ch_i].get_text())
            print("===================")
            print(res_text)
            print("===================")
            return res_text
        else:
            return url




url1 = 'https://www.znak.com/2019-10-21/meriya_kurgana_vvodit_dopolnitelnyy_avtobusnyy_marshrut_v_rayone_mosta_zhbi'
re_text1 = 'Мост ЖБИ протяженностью 462 метра был построен в 1973 году, и на сегодня он изношен. Мост соединяет центральную часть города с другими микрорайонами, от которых она отделена путями ЮУЖД.'
#re_text1 = ' ... Магнитогорского Линейного отдела полиции во время рейдовых мероприятий на железнодорожных перегонах'

#print(get_text(url1,re_text1))



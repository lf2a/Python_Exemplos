#!/usr/bin/python3
# -*- coding: utf-8 -*-

try:
    import requests
    import bs4
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    import urllib.request
except ImportError as e:
    print(e)


class Stock(object):
    def __init__(self):
        pass

    def get_stock(self, stock):
        info = {}

        r = requests.get(stock)
        soup = bs4.BeautifulSoup(r.text, 'xml')

        for span in soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}):
            sp = span.find_all('span')

            price = sp[0].text
            price_det = sp[1].text

            info.update({'price': price})
            info.update({'based-previous-price': price_det})
            
            page = urlopen(stock).read()
            soup2 = BeautifulSoup(page, 'lxml')
            
            for tr in soup2.find_all('table', {'class':'W(100%)'})[0:1]:
                tds = tr.find_all('td')
            
            value = ''
            key = ''
            
            for i in range(0, len(tds)):
                if i % 2 == 0:
                    value = tds[i].text
                else:
                    key = tds[i].text
                info.update({value : key})
            
            for tr in soup2.find_all('table', {'class':'W(100%)'})[0:]:
                tds = tr.find_all('td')
            
            value = ''
            key = ''
            
            for i in range(0, len(tds)):
                if i % 2 == 0:
                    value = tds[i].text
                else:
                    key = tds[i].text
                info.update({value : key})

        return info

    def get_cryptocoin(self, coin):
        info = {}

        r = requests.get(coin)
        soup = bs4.BeautifulSoup(r.text, 'xml')

        for span in soup.find_all('div', {'class': 'D(ib) smartphone_Mb(10px) W(70%) W(100%)--mobp smartphone_Mt(6px)'}):
            sp = span.find_all('span')

            price = sp[0].text
            price_det = sp[1].text

            info.update({'price': price})
            info.update({'based-previous-price': price_det})
        
        page = urlopen(coin).read()
        soup2 = BeautifulSoup(page, 'lxml')  
            
        for tr in soup2.find_all('table', {'class':'W(100%)'})[0:1]:
            tds = tr.find_all('td')
            
        value = ''
        key = ''
            
        for i in range(0, len(tds)):
            if i % 2 == 0:
                value = tds[i].text
            else:
                key = tds[i].text
            info.update({value : key})
        
        for tr in soup2.find_all('table', {'class':'W(100%)'})[0:]:
            tds = tr.find_all('td')
            
        value = ''
        key = ''
            
        for i in range(0, len(tds)):
            if i % 2 == 0:
                value = tds[i].text
            else:
                key = tds[i].text
            info.update({value : key})

        return info

    def search(self, valor):
        f = urllib.request.urlopen(
            "https://query2.finance.yahoo.com/v1/finance/search?q=" + valor + "&quotesCount=6&newsCount=4&quotesQueryId=tss_match_phrase_query&multiQuoteQueryId=multi_quote_single_token_query&newsQueryId=news_ss_symbols&enableCb=true&enableNavLinks=true")

        return f.read()
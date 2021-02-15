#!/usr/bin/python3
# -*- coding: utf-8 -*-

#import requests
#from newspaper import Article
import newspaper


from_url = newspaper.build('https://ural-meridian.ru/news/148312/')

# article.download()
# article = Article(url)
# article.parse()

first_article = from_url.articles
first_article.download()
first_article.parse()
#
# print(len(url.articles))
print(first_article.text)
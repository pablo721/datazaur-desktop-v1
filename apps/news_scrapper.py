from bs4 import BeautifulSoup
import requests
import yaml
import os
import sys


class NewsScrapper:
    def __init__(self):
        self.websites = None
        self.load_websites()


    def load_websites(self):
        try:
            with open('scrapper_selectors.yaml', 'r') as file:
                self.websites = yaml.safe_load(file)
        except:
            return


    def scrap_news(self, website, pages=None):
        req = requests.get(website).text
        soup = BeautifulSoup(req, features='lxml')
        articles = soup.select(self.websites[website])
        return [[article.a.text, article.a.get('href')] for article in articles]


    def add_website(self, url, selectors):
        if url in self.websites.keys():
            return False
        self.websites[url] = selectors
        with open('scrapper_selectors.yaml', 'a') as file:
            yaml.dump({url: selectors}, file)
        print('git')








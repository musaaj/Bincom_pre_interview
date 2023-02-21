#!/usr/bin/python3
"""color module"""
import requests
from bs4 import BeautifulSoup
import statistics as stat
from model.storage.engine import Engine


class Colors(BeautifulSoup):
    """color class"""

    def __init__(self, filename):
        try:
            with open(filename, 'r') as fp:
                super().__init__(fp, 'html.parser')
        except FileNotFoundError:
            pass

    def get_list(self):
        """returns single list od all colors"""
        colors_list = []
        for tr in self.find_all('tr'):
            colors_list.extend(tr.find_all('td')[1]
                      .text.split(','))
        colors_list = [val.strip() for val in colors_list]
        return sorted(colors_list)

    def get_set(self):
        """get unique colors"""
        return set(self.get_list())

    def get_dict(self):
        """returns dictionary of colors and
        and their frequencies
        """
        return {key: self.get_list().count(key)
                  for key in self.get_set()}

    def get_mode_color(self):
        """return mode of colors"""
        try:
            return stat.mode(self.get_list())
        except stat.StatisticsError:
            pass

    def get_mean_color(self):
        """return mean of colors"""
        mean = stat.mean([val for key, val in 
                self.get_dict().items()])
        for key, val in self.get_dict().items():
            if val == round(mean + 1):
                return key

    def get_median_color(self):
        """return median of colors"""
        median = stat.median([val for key, val in
                self.get_dict().items()])
        for key, val in self.get_dict().items():
            if val == round(median):
                return key

    def get_variance(self):
        """get variance of colors"""
        return stat.variance([val for key, val in
                self.get_dict().items()])

    def get_prob(self, color):
        """get probability of picking a color
        at random
        """
        if not isinstance(color, str):
            raise TypeError('color must be a string')
        colors = self.get_list()
        if color not in colors:
            raise KeyError('{} not found'.format(color))
        return colors.count(color) / len(colors)

    def save(self):
        engine = Engine(host='localhost',
                user='fakeuser',
                password='fakepass',
                port='5432',
                dbname='fakedata')
        engine.save(self)

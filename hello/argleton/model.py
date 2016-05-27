# Hello
# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
from pyquery.pyquery import JQueryTranslator
from selenium import webdriver

from hello._config import static_root

def __get_webdriver__():
  try:
    return __get_webdriver__.driver
  except AttributeError:
    __get_webdriver__.driver = webdriver.PhantomJS()
    return __get_webdriver__()


class MapShots(object):
  _css_to_xpath_ = JQueryTranslator(xhtml=True).css_to_xpath
  url = 'file://{0}/index.html'.format(static_root)

  def __init__(self):
    self._wd = __get_webdriver__()
    self._wd.get(self.url)

  @property
  def traffic(self):
    pass

  @property
  def road(self):
    pass

  @property
  def map(self):
    pass


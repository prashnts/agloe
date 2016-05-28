# Hello
# -*- coding: utf-8 -*-
import io
import skimage.io

from pyquery.pyquery import JQueryTranslator
from selenium import webdriver
from retrying import retry

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
  _opt_ = 'select[name="map-type"] option[value="{0}"]'

  def __init__(self):
    self._wd = __get_webdriver__()
    self._wd.set_window_size(1920, 1080)
    self._wd.get(self.url)
    self._p_epoch_ = 0
    self._p_state_ = None

  def _get_elements_(self, selector):
    xpath = self._css_to_xpath_(selector)
    return self._wd.find_elements_by_xpath(xpath)

  def _apply_click_(self, selector):
    for element in self._get_elements_(selector):
      element.click()

  @retry(wait_exponential_multiplier=100, wait_exponential_max=10000)
  def _validate_loaded_(self):
    try:
      c_epoch = int(self._get_elements_('#epoch')[0].get_attribute('innerText'))
    except ValueError:
      c_epoch = 0

    if not c_epoch > self._p_epoch_:
      raise ValueError

    self._p_epoch_ = c_epoch
    return True

  def _get_dom_shot_(self):
    stream = io.BytesIO(self._wd.get_screenshot_as_png())
    return skimage.io.imread(stream)

  def _get_map_(self, maptype):
    if not self._p_state_ == maptype:
      self._apply_click_(self._opt_.format(maptype))
      self._validate_loaded_()
      self._p_state_ = maptype
    return self._get_dom_shot_()

  @property
  def traffic(self):
    return self._get_map_('traffic')

  @property
  def road(self):
    return self._get_map_('road')

  @property
  def map(self):
    return self._get_map_('default')


class GrowNetwork(object):
  pass

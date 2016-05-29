# Hello
# -*- coding: utf-8 -*-
import io
import skimage.io
import random
import networkx as nx
import random

from pyquery.pyquery import JQueryTranslator
from selenium import webdriver
from retrying import retry

from hello._config import static_root
from hello.argleton.flooding import route
from hello.argleton.graph_nodes import traffic_mask


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

	def __init__(self):

		agloe = MapShots()
		self.image = agloe._get_dom_shot_()
		self.G = nx.Graph()
  

	# return all graph_nodes of different traffic densities separately
	def candidate_nodes(self):

		# using traffic_masked image for finding nodes 
		green_candidates = self.valid_nodes(traffic_mask(self.image,'green'))
		orange_candidates = self.valid_nodes(traffic_mask(self.image,'orange'))
		red_candidates = self.valid_nodes(traffic_mask(self.image,'red'))
		maroon_candidates = self.valid_nodes(traffic_mask(self.image,'maroon'))

		return green_candidates,orange_candidates,red_candidates,maroon_candidates


	# calculate road_nodes from any boolean masked image
	def valid_nodes(self,masked_image):

	  q=[]
	  # checks for true values(ie.road pixels) and append
	  for i in range(len(masked_image)):
		k=[]
		for j in range(len(masked_image[i])):

		  if masked_image[i][j]==True:
			k.append((i,j))

		if len(k)>0:
			q.append(k)

	  # to get rid of nested array
	  q = [item for sublist in q for item in sublist]

	  return q

	# agent positions for the map
	def agent_coordinates(self):

		# randomly choose agent nodes according to traffic densities
		return random.sample(self.candidate_nodes()[0],50) + random.sample(self.candidate_nodes()[1],100) + random.sample(self.candidate_nodes()[2],150) + random.sample(self.candidate_nodes()[3],200)


	# calculates within-range nodes and add corresponding edge to the graph
	def valid_graph_edges(self):

		a = self.agent_coordinates()
		
		p = [[i,j,((i[1]-j[1])**2 + (i[0]-j[0])**2)**0.5] for i in a for j in a if i != j]
		d = [[i,j] for x in p if x[3]<200]

		self.G.add_edges_from(d)


	# overlays agent images on the map
	def draw_agent(self):

		for i in self.agent_coordinates():
			x,y = i[0],i[1]
			
			steps = [(100, [100, 20, 255, 50]),
					 (50,  [100, 20, 255, 150]),
					 (20,  [50,  20, 150, 255])]

			for step in steps:
				rr, cc = skimage.draw.circle(x, y, step[0])
				self.image[rr, cc] = step[1]

		return self.image

	# resultant route path (only for flooding algo for now)
	def draw_route_edges(self,source,destination):

		for i in route(source,destination,self.G):

			rr, cc = skimage.draw.line(i[0][1],i[0][0],i[1][1],i[1][0])
				self.image[rr, cc] = [40,60,80]

		return self.image











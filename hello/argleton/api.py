# Hello
# -*- coding: utf-8 -*-
import hug

@hug.get('/')
def get_root():
  return "Test API"


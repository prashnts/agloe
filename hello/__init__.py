# Hello
# -*- coding: utf-8 -*-
import hug
import pecan_mount
import static

from hello import _config as config

@hug.get('/')
def index():
  """API Homepage"""
  return "Hello API Server. Go to /v1 for docs."


from hello.argleton import api as argleton_api

@hug.extend_api('/argleton')
def attach_argleton_api():
  return [argleton_api]

# Get WSGI friendly environment for *both* Static Files and API
pecan_mount.tree.graft(__hug_wsgi__, '/api')
pecan_mount.tree.graft(static.Cling(config.static_root), '/')

api = pecan_mount.tree

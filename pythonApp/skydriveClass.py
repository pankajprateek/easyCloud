#!/usr/bin/python

import cmd
import locale
import os
import pprint
import shlex
import sys
import httplib2
from __future__ import unicode_literals, print_function
import itertools as it, operator as op, functools as ft
from os.path import dirname, basename, exists, isdir, join, abspath
from collections import defaultdict
import io, re, types, json

try:
	import chardet
except ImportError: # optional
	chardet = None
	
import api_v5, conf

class skydriveClass:
	def __init__(self):
		self.TOKEN_FILE = "~/.lcrc"
		self.api_client = api_v5.PersistentSkyDriveAPI.from_conf(optz.config)
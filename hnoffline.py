# -*- coding: utf-8 -*-
import os
import sys

from hackernews import HackerNews
from jinja2 import FileSystemLoader, Environment

# http://stackoverflow.com/a/19105436/4905313
sys.version = '2.7.3 (default, Apr 12 2012, 14:30:37) [MSC v.1500 32 bit (Intel)]'

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
templateLoader = FileSystemLoader(THIS_DIR)
templateEnv = Environment(loader=templateLoader, trim_blocks=True)
TEMPLATE_FILE = "index.jinja2"
template = templateEnv.get_template( TEMPLATE_FILE )

hn = HackerNews()

# Get the top 10 stories
top_stories = [hn.get_item(story_id) for story_id in hn.top_stories(limit=5)]
outputText = (template.render( top_stories = top_stories )).encode('utf-8')

# Make an output html file
output = open("index.html", "w")
output.write(outputText)
output.close()
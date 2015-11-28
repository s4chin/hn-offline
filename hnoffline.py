# -*- coding: utf-8 -*-
import os
import sys

from hackernews import HackerNews
from jinja2 import FileSystemLoader, Environment

# http://stackoverflow.com/a/19105436/4905313
sys.version = '2.7.3 (default, Apr 12 2012, 14:30:37) [MSC v.1500 32 bit (Intel)]'

def set_up_jinja2():
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    templateLoader = FileSystemLoader(THIS_DIR)
    templateEnv = Environment(loader=templateLoader, trim_blocks=True)
    TEMPLATE_FILE = "./templates/index.jinja2"
    template = templateEnv.get_template( TEMPLATE_FILE )
    return template

def get_top_stories(hn, limit=2):
    """
        Get the top 10 stories
    """
    top_stories = [hn.get_item(story_id) for story_id in hn.top_stories(limit=limit)]
    return top_stories

def get_ask_stories(hn, limit=2):
    ask_stories = [hn.get_item(story_id) for story_id in hn.top_stories(limit=limit)]
    return ask_stories

def make_output_page(outputText, directory="", page_name="index"):
    # Make an output html file
    output = open(directory + page_name + ".html", "w")
    output.write(outputText)
    output.close()

def render_template(stories, template):
    """
        Return the rendered template with the stories
    """
    return (template.render(stories=stories)).encode('utf-8')

def main():
    template = set_up_jinja2()
    hn = HackerNews()
    top_stories = get_top_stories(hn)
    outputText = render_template(stories=top_stories, template=template)
    make_output_page(outputText=outputText)

if __name__ == '__main__':
    main()
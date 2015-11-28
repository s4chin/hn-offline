# -*- coding: utf-8 -*-
import os
import errno
import shutil
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
        Get the top stories
    """
    top_stories = [hn.get_item(story_id) for story_id in hn.top_stories(limit=limit)]
    sys.stdout.write("Got the top stories\n")
    return top_stories

def get_ask_stories(hn, limit=2):
    """
        Get the Ask HN posts
    """
    ask_stories = [hn.get_item(story_id) for story_id in hn.ask_stories(limit=limit)]
    sys.stdout.write("Got the ask stories\n")
    return ask_stories

def make_output_page(outputText, directory="./output/", page_name="index"): # There's something wrong here :(
    # Make an output html file
    output = open(directory + page_name + ".html", "w")
    output.write(outputText)
    output.close()

def render_template(templateVars, template):
    """
        Return the rendered template with the stories
    """
    return (template.render(templateVars)).encode('utf-8')

# http://stackoverflow.com/a/5032238/4905313
def make_folder(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def main():
    template = set_up_jinja2()
    hn = HackerNews()
    top_stories = get_top_stories(hn)
    ask_stories = get_ask_stories(hn)
    templateVars = {
        "top_stories": top_stories,
        "ask_stories": ask_stories
    }
    outputText = render_template(templateVars=templateVars, template=template)
    make_folder("./output") # Make it take its value from a config file
    shutil.copytree(src="./templates/js", dst="./output/js") # Error if folder already exists, need to workaround this
    make_output_page(outputText=outputText)

if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bowtie.visual import Markdown
from bowtie.control import Textbox


mark = Markdown('''
# Text you write
## goes here

link to [bowtie](https://github.com/jwkvam/bowtie)

''')
text = Textbox(area=True, autosize=True, placeholder='Enter markdown')
sidemark = Markdown('# Live Markdown Editor')


def write(txt):
    mark.do_text(txt)


from bowtie import command, Layout
@command
def build():
    layout = Layout(debug=False)
    layout.add(mark)
    layout.add_sidebar(sidemark)
    layout.add_sidebar(text)

    layout.subscribe(write, text.on_change)

    layout.build()

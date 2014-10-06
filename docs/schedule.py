#!/usr/bin/env python
# schedule.py

import re
import collections
RE_TIME = re.compile(r'([^(]*)\(\s*(\d+)\s*(?:min)?\s*\)([^(]*)', re.IGNORECASE)

def schedule(path='outline.md'):
    """Process an outline in Markdown format, extracting the time estimates for each line"""

    sections, parent, i = collections.OrderedDict(), 0, 1
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            matches = RE_TIME.match(line)
            if matches:
                groups = [g.strip().strip('.').strip() for g in matches.groups()]
                try:
                    sections[i] = dict(zip(['number', 'time', 'name', 'line'], groups + [line.strip()]))
                    sections[i]['parent'] = None
                except IndexError:
                    sections[i] = {'time': matches.group(2), 'line': line.strip()}
                    sections[i]['parent'] = None
                parent = i
            else:
                sections[i] = {'parent': parent, 'line': line.strip()}
    return sections


def generate_markdown(sections):
    for i, section in sections.iteritems():
        if section.get('name', None):
            slide = '---\n'
            slide += 'title: {0}'.format(section['name'])


def print_markdown(path='outline.md'):
    for slide in generate_markdown(schedule(path)):
        print slide


if __name__ == '__main__':
    print_markdown()

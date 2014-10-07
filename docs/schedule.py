#!/usr/bin/env python
# schedule.py

import os.path
import re
import collections
import math

from pug.nlp import util


RE_TIME = re.compile(r'([^(]*)\(\s*(\d+)\s*(?:min)?\s*\)([^(]*)', re.IGNORECASE)

def schedule(path=None):
    """Process an outline in Markdown format, extracting the time estimates for each line"""

    if not path:
        path = 'outline.md'

    sections, parent, i, section_num = collections.OrderedDict(), 0, 1, 1
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            matches = RE_TIME.match(line)
            if matches:
                groups = [g.strip().strip('.').strip() for g in matches.groups()]
                try:
                    section_num = float(matches.group(1))
                except ValueError:
                    section_num = section_num + 1
                try:
                    sections[i] = dict(zip(['bullet', 'time', 'name', 'line', 'section'], groups + [line.strip(), section_num]))
                    sections[i]['parent'] = None
                    try:
                        sections[i]['time'] = float(sections[i]['time'].strip())
                    except ValueError:
                        pass
                except IndexError:
                    sections[i] = {'time': matches.group(2), 'line': line.strip()}
                    sections[i]['parent'] = None
                if 'coffee' in line.lower() or line.strip('-').strip().startswith('Break'):
                    sections[i]['name'] = 'Break'
                    sections[i]['time'] = '10'
                    sections[i]['bullet'] = ''
                    sections[i]['section'] = section_num

                parent = i
            else:
                sections[i] = {'parent': parent, 'line': line.strip()}
            i += 1
    return sections


def generate_markdown(sections):
    for i, section in sections.iteritems():
        if section.get('name', None):
            section['name'] = section['name'][0].upper() + section['name'][1:]
            slide = '\n---\n'
            slide += 'title: {0}\n'.format(section['name'])
            if section.get('time', None):
                slide += 'footer: ({0} min)\n'.format(section['time'])
        else:
            slide = '* ' + section['line'].strip()
        yield slide



def print_markdown(sections):
    if not sections or (isinstance(sections, basestring) and os.path.isfile(sections)):
        sections = schedule(sections)
    for slide in generate_markdown(sections):
        print slide


def total_time(sections):
    total = 0
    for i, s in sections.iteritems():
        try:
            total += float(s['time'])
        except:
            pass
    return total


if __name__ == '__main__':
    sections = schedule()
    num_bullets = len(sections)
    md = ''
    for slide in generate_markdown(sections):
        md += slide

    stats = util.markdown_stats(md)
    stats['time'] = '{0:d}:{1:02d}'.format(int(math.floor(total_time(sections) / 60.)), int(total_time(sections) % 60))
    print md
    print '---\ntitle: Metadata\n\n'
    for k, v in stats.iteritems():
        print '* {0}: {1}'.format(k.capitalize(), v)

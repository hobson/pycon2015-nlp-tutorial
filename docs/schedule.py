# calc_schedule.py

import re
RE_TIME = re.compile(r'([^(]*)\(\s*(\d+)\s*(?:min)?\s*\)([^(]*)', re.IGNORECASE)

times = []
with open('outline.md', 'r') as f:
    for line in f:
        txt = f.read()
        matches = RE_TIME.match('1. (10 min) What is natural language ')
        groups = [g.strip().strip('.').strip() for g in matches.groups()]
        if matches:
            try:
                times += [dict(zip(['number', 'time', 'name', 'line'], groups + [matches.group(0)]))]
            except IndexError:
                times += [{'time': matches.group(2), 'line': matches.group(0)}]






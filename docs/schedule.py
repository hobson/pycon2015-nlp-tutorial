# calc_schedule.py

def schedule(path='outline.md'):
    """Process an outline in Markdown format, extracting the time estimates for each line"""
    import re
    RE_TIME = re.compile(r'([^(]*)\(\s*(\d+)\s*(?:min)?\s*\)([^(]*)', re.IGNORECASE)

    sections, parent, i = [], 0, 1
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            matches = RE_TIME.match()
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



#!/usr/bin/env sh

python schedule.py > slides/middle.md && cat slides/front.md middle.md slides/back.md > slides/slides.md && cd slides && slidedeck render && cd ..

#!/bin/bash
find /src/timetravel_radio/ -name *.mp3 -exec lame --decode -m m {} \; -exec rm {} \;

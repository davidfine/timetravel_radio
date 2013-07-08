#!/bin/bash
find /Users/dfine/Documents/projects/radio/wavs -name *.mp3 -exec lame --decode -m m {} \; -exec rm {} \;

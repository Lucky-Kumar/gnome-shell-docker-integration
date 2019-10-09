#!/usr/bin/python

# Check that a valid UUID is used for the extension
# according to the https://wiki.gnome.org/Projects/GnomeShell/Extensions/UUIDGuidelines

import sys
import re


def validate(value):
    print('Value passed:', value)
    result = re.match('[-a-zA-Z0-9@._]+$', value)
    if result == None:
        print('NO Valid UUID Provided 😭')
    else:
        print('You are good to go 😁')


# use stdin
if not sys.stdin.isatty():
    input_stream = sys.stdin
    for line in input_stream:
        validate(line.strip())
# use arguments
elif len(sys.argv) > 1:
    for value in sys.argv[1:]:
        validate(sys.argv[1])
else:
    print('No argument/s passed 😩')

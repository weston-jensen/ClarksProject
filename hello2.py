#!/usr/bin/env python

import os


print "content-type: text/html\n"

qs = os.environ['QUERY_STRING']

if 'firstname' in qs:
	name = qs.split('=')[1]
else:
	name = 'No name provided'

print "<html>"
print "<body> <h1> Hello %s </h1>" % name
print "</pre>"
print "</body>"
print "</html>"

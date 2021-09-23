#!/usr/bin/env python3

import os
import json

# Q1
print("Content-Type:text/html\r\n\r\n")
print()
print("<title> Test </title>")

# print the env. var.
#print(os.environ)

# serve the env back as Json
json_environ = json.dumps(dict(os.environ), indent=4)
#print(json_environ)

# Q2
print("<b>Query string</b> = {" + os.environ.get("QUERY_STRING") + "}<br>")

# Q3
print("<b>User's borwser in the HTML</b> = {" + os.environ.get("HTTP_USER_AGENT") + "}<br>")

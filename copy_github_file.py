#!/usr/bin/python3
# Copy github file version in python
import sys
import requests

if len(sys.argv) < 2:
    print('You Have to pass a url to the github file')
else:
    url: str = sys.argv[1]
    # Get the raw version of the file url
    raw_url: str = url.replace('/github.com', '/raw.githubusercontent.com').replace('/blob/','/')
    # get the filename
    if len(sys.argv) > 2:
        filename: str = sys.argv[2]
    else:
        filename: str = raw_url.split('/')[-1]
    # get the content of the raw url
    file_contents = requests.get(raw_url).text
    # Write to file
    f = open(filename,'w')
    f.write(file_contents)
    f.close()

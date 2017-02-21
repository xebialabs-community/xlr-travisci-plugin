#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

#!/usr/bin/python
# Launch a Travis CI Build

import json, time, urllib2

#print "Travis CI Build.\n"
#print "username   : " + username + "\n"
#print "apiversion : " + apiversion + "\n"
#print "token      : " + token + "\n"
#print "project    : " + project + "\n"
#print "branch     : " + branch + "\n"
print "wait          : %r\n" % wait
print "waitInterval  : %s\n" % waitInterval


headers = {'Content-type' : 'application/json', 'Travis-API-Version' : '%s' % apiversion, 'Accept' : 'application/json', 'Authorization' : 'token %s' % token}
url = 'https://api.travis-ci.org/repo/%s%%2f%s/requests' % (username, project)
#print "url       : " + url + "\n"

params = {'request' : {'branch' : '%s' % branch}}
req = urllib2.Request(url, json.dumps(params), headers)
response = urllib2.urlopen(req)
print response.read()
time.sleep(15)

if wait:
    url = 'https://api.travis-ci.org/repo/%s%%2f%s/builds' % (username, project)
    #print "url       : " + url + "\n"

    req = urllib2.Request(url, None, headers)
    while (True):
        response = urllib2.urlopen(req)
        data = json.load(response)
        state = data["builds"][0]["state"]
        number = data["builds"][0]["number"]
        print "build number : " + number + "\n"
        print "state        : " + state + "\n"

        if state == "passed":
            sys.exit(0)
        elif state == "failed":
            sys.exit(1)
        else:
            time.sleep(float(wait))


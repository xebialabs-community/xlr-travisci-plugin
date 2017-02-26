#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import json, time, urllib2

class TravisCIClient(object):
    def __init__(self, authentication):
        self.url = authentication["url"]
        self.username = authentication["username"]
        self.token = authentication["token"]
        self.apiversion = authentication["apiversion"]
        self.headers = {
            'Content-type' : 'application/json',
            'Accept' : 'application/vnd.travis-ci.2+json',
            'Authorization' : 'token %s' % self.token}

    @staticmethod
    def create_client(authentication):
        return TravisCIClient(authentication)

    def build_request(self, url, data=None):
        return urllib2.Request(url, data, self.headers)

    def get_accounts(self):
        accounts_endpoint = "%s%s" % (self.url, "/accounts")
        request = self.build_request(accounts_endpoint)
        response = urllib2.urlopen(request)
        if not response.getcode() == 200:
            raise Exception("Failed to retrieve accounts information for the specified Authentication Configuration.")
        response_data = json.load(response)
        return response_data["accounts"]

    def trigger_build(self, project, branch, wait, wait_interval):
        data = {'request' : {'branch' : '%s' % branch}}
        trigger_build_endpoint = "%s/repo/%s%%2f%s/requests" % (self.url, self.username, project)
        request = self.build_request(trigger_build_endpoint, json.dumps(data))
        request.add_header('Travis-API-Version', '%s' % self.apiversion)
        response = urllib2.urlopen(request)
        if not (response.getcode() == 200 or 202):
            raise Exception("Failed to trigger build for project [%s] on branch [%s]. Response code: %s" % (project, branch, response.getcode()))
        build_request_info = json.load(response)
        request_id = build_request_info["request"]["id"]

        if wait:
            while (True):
                request_info = self.request_info(request_id)
                if not "build_id" in request_info["request"]:
                    time.sleep(10)
                else:
                    break

            build_id = request_info["request"]["build_id"]
            while (True):
                build_info = self.get_build_info(build_id)
                state = build_info["build"]["state"]

                if state == "passed":
                    return request_info
                elif state == "failed":
                    sys.exit(1)
                else:
                    time.sleep(float(wait_interval))

    def request_info(self, request_id):
        request_info_endpoint = "%s/requests/%s" % (self.url, request_id)
        request = self.build_request(request_info_endpoint)
        response = urllib2.urlopen(request)
        if not response.getcode() == 200:
            raise Exception("Failed to retrieve request information for the specified request_id [%s]" % (request_id))
        return json.load(response)

    def get_build_info(self, build_id):
        build_info_endpoint = "%s/builds/%s" % (self.url, build_id)
        request = self.build_request(build_info_endpoint)
        response = urllib2.urlopen(request)
        if not response.getcode() == 200:
            raise Exception("Failed to retrieve build information for the specified build_id [%s]" % (build_id))
        return json.load(response)

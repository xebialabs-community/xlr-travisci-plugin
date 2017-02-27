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
        data = {'request' : {'branch' : branch}}
        trigger_build_endpoint = "%s/repo/%s%%2f%s/requests" % (self.url, self.username, project)
        request = self.build_request(trigger_build_endpoint, json.dumps(data))
        request.add_header('Travis-API-Version', '%s' % self.apiversion)
        response = urllib2.urlopen(request)
        if not (response.getcode() == 200 or 202):
            raise Exception("Failed to trigger build for project [%s] on branch [%s]. Response code: %s" % (project, branch, response.getcode()))
        build_request_info = json.load(response)
        if wait:
            build_request_info = self.wait_for_build_start(build_request_info)
            return self.wait_for_build(build_request_info, wait_interval)
        return build_request_info

    def wait_for_build_start(self, build_request_info):
        while (True):
            request_info = self.request_info(build_request_info["request"]["id"])
            if not "build_id" in request_info["request"]:
                time.sleep(10)
            else:
                return request_info

    def wait_for_build(self, build_request_info, wait_interval):
        while (True):
            build_info = self.get_build_info(build_request_info["request"]["build_id"])
            state = build_info["build"]["state"]
            if state == "passed":
                return build_request_info
            elif state == "failed":
                sys.exit(1)
            else:
                time.sleep(float(wait_interval))

    def request_info(self, request_id):
        return self.get_response_for_endpoint(self.url, "requests", request_id, "Failed to retrieve request information for the specified request_id [%s]" % (request_id))

    def get_build_info(self, build_id):
        return self.get_response_for_endpoint(self.url, "builds", build_id, "Failed to retrieve build information for the specified build_id [%s]" % (build_id))

    def get_response_for_endpoint(self, url, endpoint, id, error_message):
        endpoint = "%s/%s/%s" % (url, endpoint, id)
        request = self.build_request(endpoint)
        response = urllib2.urlopen(request)
        if not response.getcode() == 200:
            raise Exception(error_message)
        return json.load(response)

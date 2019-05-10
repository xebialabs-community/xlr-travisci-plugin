#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import json, time, urllib2


class TravisCIClient(object):
    def __init__(self, authentication):
        self.url = authentication["url"]
        self.username = authentication["username"]
        self.token = authentication["token"]
        self.apiversion = authentication["apiversion"]
        self.headers = [
            ('Content-type', 'application/json'),
            ('Accept', 'application/vnd.travis-ci.2+json'),
            ('Authorization', 'token %s' % self.token)]

    @staticmethod
    def create_client(authentication):
        return TravisCIClient(authentication)

    def get_accounts(self):
        accounts_endpoint = "%s%s" % (self.url, "/accounts")
        response = self.open_url(accounts_endpoint)
        if not response.getcode() == 200:
            raise Exception("Failed to retrieve accounts information for the specified Authentication Configuration.")
        response_data = json.load(response)
        return response_data["accounts"]

    def trigger_build(self, task, organization, project, branch, wait, wait_interval):
        data = {'request': {'branch': branch}}
        trigger_build_endpoint = "%s/repo/%s%%2f%s/requests" % (
        self.url, organization if organization else self.username, project)
        build_headers = self.headers[:]
        build_headers.append(('Travis-API-Version', self.apiversion))
        response = self.open_url(trigger_build_endpoint, json.dumps(data), build_headers)
        if not (response.getcode() == 200 or 202):
            raise Exception("Failed to trigger build for project [%s] on branch [%s]. Response code: %s" % (
            project, branch, response.getcode()))
        build_request_info = json.load(response)
        if wait:
            build_request_info = self.wait_for_build_start(build_request_info, wait_interval)
            return self.wait_for_build(build_request_info, wait_interval)
        return build_request_info

    def wait_for_build_start(self, build_request_info, wait_interval):
        time.sleep(float(wait_interval))
        while True:
            request_info = self.request_info(build_request_info["request"]["id"])
            if not "build_id" in request_info["request"]:
                time.sleep(float(wait_interval))
            else:
                return request_info

    def wait_for_build(self, build_request_info, wait_interval):
        time.sleep(float(wait_interval))
        while True:
            build_info = self.get_build_info(build_request_info["request"]["build_id"])
            state = build_info["build"]["state"]
            if state == "passed":
                return build_request_info
            elif state == "failed":
                sys.exit(1)
            else:
                time.sleep(float(wait_interval))

    def request_info(self, request_id):
        return self.get_response_for_endpoint(self.url, "requests", request_id,
                                              "Failed to retrieve request information for the specified request_id [%s]" % (
                                              request_id))

    def get_build_info(self, build_id):
        return self.get_response_for_endpoint(self.url, "builds", build_id,
                                              "Failed to retrieve build information for the specified build_id [%s]" % (
                                              build_id))

    def get_response_for_endpoint(self, url, endpoint, object_id, error_message):
        full_endpoint_url = "%s/%s/%s" % (url, endpoint, object_id)
        response = self.open_url(full_endpoint_url)
        if not response.getcode() == 200:
            raise Exception(error_message)
        return json.load(response)

    def open_url(self, url, data=None, headers=None):
        open_director = urllib2.build_opener(urllib2.HTTPHandler)
        if headers is None:
            open_director.addheaders = self.headers
        else:
            open_director.addheaders = headers
        return open_director.open(url, data)

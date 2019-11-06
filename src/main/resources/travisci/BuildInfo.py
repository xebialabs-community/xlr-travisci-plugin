#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from travisci.TravisCIClientUtil import TravisCIClientUtil

travis_ci_client = TravisCIClientUtil.create_travis_ci_client(authentication)
build_info = travis_ci_client.get_build_info(build_id)
build_state = build_info["build"]["state"]


project = build_info["build"]["config"]["deploy"]["true"]["repo"]
build_number = build_info["build"]["number"]
build_start_date = build_info["build"]["started_at"]
build_end_date = build_info["build"]["finished_at"]
build_duration = build_info["build"]["duration"]

myBuildRecord = taskReportingApi.newBuildRecord()
myBuildRecord.targetId = task.id

myBuildRecord.project =  project
myBuildRecord.build = build_number
myBuildRecord.build_url = "%s/%s#%s" % (authentication["url"], "builds", build_number)
myBuildRecord.serverUrl = authentication["url"]
myBuildRecord.serverUser = authentication["username"]
myBuildRecord.outcome = build_state
myBuildRecord.startDate = build_start_date
myBuildRecord.endDate = build_end_date
myBuildRecord.duration = str(build_duration)

taskReportingApi.addRecord(myBuildRecord, True)

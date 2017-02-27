#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from travisci.TravisCIClientUtil import TravisCIClientUtil

travis_ci_client = TravisCIClientUtil.create_travis_ci_client(authentication)
request_info = travis_ci_client.request_info(request_id)
build_id = request_info["request"]["build_id"]

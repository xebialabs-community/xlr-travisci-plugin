#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

#!/usr/bin/python
# Launch a Travis CI Build


from travisci.TravisCIClientUtil import TravisCIClientUtil

travis_ci_client = TravisCIClientUtil.create_travis_ci_client(authentication)
build_info = travis_ci_client.get_build_info(build_id)
build_state = build_info["build"]["state"]

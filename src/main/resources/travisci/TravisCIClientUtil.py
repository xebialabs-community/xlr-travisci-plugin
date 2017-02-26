#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from travisci.TravisCIClient import TravisCIClient


class TravisCIClientUtil(object):

    @staticmethod
    def create_travis_ci_client(authentication):
        client = TravisCIClient.create_client(authentication)
        return client

# xlr-travisci-plugin

This plugin offers an interface from XL Release to Travis CI. 

# CI status #

[![Build Status][xlr-travisci-plugin-travis-image]][xlr-travisci-plugin-travis-url]

[xlr-travisci-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xlr-travisci-plugin.svg?branch=master
[xlr-travisci-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xlr-travisci-plugin

# Development #

* Start XL Release: `./gradlew runDockerCompose`
* Stop XL Release:  `./gradlew stopDockerCompose`

+ `travisci.Authentication`: Defines the Travis CI authentication credentials to be used.
    + `url`: The URL for accessing Travis CI REST API endpoints [Travis CI Rest API](https://docs.travis-ci.com/api#overview)
    + `username` The username required for some Travis CI REST API calls.
    + `token` The authentication token required for Travis CI REST API calls. [Authentication](https://docs.travis-ci.com/api#authentication)

+ `travisci.Accounts`: A user might have access to multiple accounts. This is usually the account corresponding to the user directly and one account per GitHub organization.
    + Implements the api call as described in [Accounts](docs.travis-ci.com/api#entities)
+ `travisci.BuildInfo`: Retrieves information about a specific Travis CI build.
    + Implements the api call as described in [Builds](https://docs.travis-ci.com/api#builds)
+ `travisci.RequestInfo`: Retrieves information about a specific request for a Travis CI build.
    + Implements the api call as described in [Requests](https://docs.travis-ci.com/api#requests)
+ `travisci.TriggerBuild`: Triggers a build of the specified project and branch.
    + Implements the api call as described in [Triggering builds through the API](https://docs.travis-ci.com/user/triggering-builds)
    
# References #
[Travis CI Rest API](https://docs.travis-ci.com/api)


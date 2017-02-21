# xlr-travisci-plugin

This plugin offers an interface from XL Release to Travis CI. 

# CI status #

[![Build Status][xlr-travisci-plugin-travis-image]][xlr-travisci-plugin-travis-url]

[xlr-travisci-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xlr-travisci-plugin.svg?branch=master
[xlr-travisci-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xlr-travisci-plugin

# Development #

* Start XLR: `./gradlew runDockerCompose`

+ `travisci.TriggerBuild`: Triggers a build of the specified project and branch.
    + Implements the api call as described in [Triggering builds through the API](https://docs.travis-ci.com/user/triggering-builds)
    
# References #
[Travis CI Rest API](https://docs.travis-ci.com/api)


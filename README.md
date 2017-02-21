# xlr-travisci-plugin

This plugin offers an interface from XL Release to Travis CI. 

# CI status #

[![Build Status][xlr-travisci-plugin-travis-image]][xlr-travisci-plugin-travis-url]
#[![Codacy Badge][xlr-travisci-plugin-codacy-image] ][xlr-travisci-plugin-codacy-url]
#[![Code Climate][xlr-travisci-plugin-code-climate-image] ][xlr-travisci-plugin-code-climate-url]

[xlr-travisci-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xlr-travisci-plugin.svg?branch=master
[xlr-travisci-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xlr-travisci-plugin
#[xlr-travisci-plugin-codacy-image]: https://api.codacy.com/project/badge/Grade/a76c515de76640fc9e1f282575382937
#[xlr-travisci-plugin-codacy-url]: https://www.codacy.com/app/joris-dewinne/xlr-circleci-plugin
#[xlr-travisci-plugin-code-climate-image]: https://codeclimate.com/github/xebialabs-community/xlr-circleci-plugin/badges/gpa.svg
#[xlr-travisci-plugin-code-climate-url]: https://codeclimate.com/github/xebialabs-community/xlr-circleci-plugin

# Development #

* Start XLR: `./gradlew runDockerCompose`

# Type definitions #
#+ `circleci.Server`: Defines your Circle CI endpoint to be used.
#    + `username`: Use this property to define the token as described in [Authentication](https://circleci.com/docs/api/#authentication)
#+ `circleci.GetUser`: Provides information about the signed in user
#    + Implements the api call as described in [User](https://circleci.com/docs/api/#user)
#+ `circleci.TriggerBuild`: Triggers a build of the specified project and branch.
#    + Implements the api call as described in [Trigger a new Build with a Branch](https://circleci.com/docs/api/#new-build-branch)
    
# References #
[Travis CI Rest API](https://docs.travis-ci.com/api)


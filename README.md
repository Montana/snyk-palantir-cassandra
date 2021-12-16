![image](https://user-images.githubusercontent.com/20936398/146291011-e2a74fa8-c94d-4ab1-87d0-4a64137d141b.png)

[![Build Status](https://app.travis-ci.com/Montana/snyk-palantir-cassandra.svg?branch=master)](https://app.travis-ci.com/Montana/snyk-palantir-cassandra)


## Testing Palantir's remix of Apache Cassandra with Snyk & Travis CI

This repository is to show Travis CI testing a Dockerfile based on Palantir's remix of Apache Cassandra, testing IaC's (Terraform, Kubernetes), and testing the integration health of Debian.

## Usage 

So we hade to define in the `.travis.yml` file the language as `node`, via we have to grab `Snyk` and to do that we need to use `npm`. We then grab `pipenv`, there is the `.travis.yml` I've created for this project: 

```yaml
install:
  - pip install pipenv
language: node_js
node_js:
  - lts/*
script:
  - npm install -g snyk@latest # Globally install Snyk via node package manager, using condition `@latest` for latest version.
  - snyk -v # Print out the current version of Snyk symlinked. 
  - snyk code
  - snyk test --docker debian --file=Dockerfile --exclude-base-image-vulns # Scan the Palantir Cassandra container. 
  - snyk iac test variable.tf # Test an IaC method, say in this case Terraform. With simple variables that really equal to moot.
  - snyk iac test Kubernetes.yaml  # Test the Kubernetes.yaml file to see if there's any vuln's, this is defined to run on nginx.
  
# The rest of the .travis.yml in this repo, is my branching process. So if you look at the existing .travis.yml in this repo, and wonder why it's different, that's the reson. The above snippet will get you going. 
  ```

It's important to note you'll need your Snyk `env vars`. I started this out `language: python`, then switched it to `node` to fetch `Snyk`, it's a quirky workaround, but works. I've also added cursory checks for Palantir's Apache Cassandra Dockerfile, to see if Snyk crashes when doing things in succession.

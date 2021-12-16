![image](https://user-images.githubusercontent.com/20936398/146291011-e2a74fa8-c94d-4ab1-87d0-4a64137d141b.png)


## Testig IaC's, Dockerfiles, Palantir's Remix of Apache Cassandra with Snyk & Travis CI

Breadth-first search I made to have Snyk/Travis CI in conjunction, to test it. 


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
  - snyk -v # Print out version 
  - snyk code
  - snyk test --docker debian --file=Dockerfile --exclude-base-image-vulns # Scan the Palantir Cassandra container. 
  - snyk iac test variable.tf # Test an IaC method, say in this case Terraform. With simple variables that really equal to moot.
```

It's important to note you'll need your Snyk `env vars`. I started this out `language: python`, then switched it to `node` to fetch `Snyk`, it's a quirky workaround, but works. I've also added cursory checks for Palantir's Apache Cassandra Dockerfile, to see if Snyk crashes when doing things in succession.

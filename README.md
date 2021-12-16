# Testing a BFS with Travis CI & Snyk

Breadth-first search I made to have Travis CI/Snyk to test it. 


## Usage 

So we hade to define in the `.travis.yml` file the language as `node`, via we have to grab `Snyk` and to do that we need to use `npm`. We then grab `pipenv`, there is the `.travis.yml` I've created for this project: 

```yaml
install:
  - pip install pipenv
language: node_js
node_js:
  - lts/*
script:
  - npm install -g snyk # Globally install Snyk via node package manager
  - snyk -v # Print out version 
  - snyk code
```

It's important to note you'll need your Snyk `env vars`. 

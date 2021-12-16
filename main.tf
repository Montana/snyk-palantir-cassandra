provider "local" {
  version = "~> 1.4"
}
resource "local_file" "hello snyk, palantir, cassandra and travis" {
  content = "Hello, user"
  filename = "foobar.txt"
}

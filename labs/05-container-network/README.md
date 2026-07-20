# Lab 05 — Container Networking and DNS

Create a network:

~~~bash
docker network create learning-net
~~~

Start a web server:

~~~bash
docker run -d --name lab-web --network learning-net nginx:1.27-alpine
~~~

Use a temporary client on the same network:

~~~bash
docker run --rm --network learning-net curlimages/curl:8.12.1 \
  http://lab-web
~~~

The client resolves `lab-web` using Docker's embedded DNS.

Inspect:

~~~bash
docker network inspect learning-net
~~~

Cleanup:

~~~bash
docker rm -f lab-web
docker network rm learning-net
~~~

Challenges:

1. Run the client without `--network learning-net`.
2. Explain why no host port is required for container-to-container traffic.
3. Publish Nginx to the host and compare internal and external access.

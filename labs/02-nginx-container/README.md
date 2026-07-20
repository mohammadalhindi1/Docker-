# Lab 02 — Run an Nginx Web Server

## Objective

Run a long-lived service, publish a port, inspect logs, enter the container, and clean up safely.

## Start the server

~~~bash
docker run -d --name docker-lab-web -p 8080:80 nginx:1.27-alpine
~~~

Open:

~~~text
http://localhost:8080
~~~

The mapping `8080:80` means traffic arriving at host port 8080 is forwarded to port 80 inside the container.

## Inspect it

~~~bash
docker ps
docker port docker-lab-web
docker logs docker-lab-web
docker inspect docker-lab-web
docker stats docker-lab-web
~~~

Stop `docker stats` with Ctrl+C; this does not stop the container.

## Enter the running container

~~~bash
docker exec -it docker-lab-web sh
~~~

Inside the container:

~~~sh
hostname
ps
ls /usr/share/nginx/html
cat /usr/share/nginx/html/index.html
exit
~~~

The Alpine image uses `sh`; Bash may not be installed.

## Understand the lifecycle

~~~bash
docker stop docker-lab-web
docker ps
docker ps -a
docker start docker-lab-web
~~~

Refresh the browser after restarting it. This is the same container, not a new one.

## Cleanup

~~~bash
docker stop docker-lab-web
docker rm docker-lab-web
~~~

The Nginx image remains available locally.

## Challenges

1. Run a second Nginx container on host port 8081.
2. Try to run two containers using host port 8080. Explain the error.
3. Use `docker logs -f`, then refresh the browser and observe the request.
4. Find the container IP with `docker inspect`.

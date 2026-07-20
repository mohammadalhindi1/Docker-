# 07 — Docker Networking

Docker networking allows containers to communicate with each other, the host, and external networks.

## Common network drivers

| Driver | Purpose |
|---|---|
| bridge | Default networking for containers on one Docker host |
| host | Share the host network namespace on supported systems |
| none | Disable external networking |
| overlay | Connect services across multiple Docker hosts, commonly with Swarm |
| macvlan | Give containers network identities on the physical network |

## User-defined bridge

~~~bash
docker network create app-net
docker run -d --name api --network app-net my-api
docker run -d --name db --network app-net postgres:17
~~~

Containers on a user-defined bridge can resolve each other by name. The API should connect to host `db`, not `localhost`.

Inside the API container, `localhost` means the API container itself.

## Port publishing

~~~bash
docker run -d -p 127.0.0.1:8080:80 nginx
~~~

Format:

~~~text
HOST_IP:HOST_PORT:CONTAINER_PORT
~~~

Publishing on `127.0.0.1` restricts access to the local machine. `-p 8080:80` may publish on all host interfaces depending on configuration.

`EXPOSE 80` documents a port in an image. It does not publish the port.

## Useful commands

~~~bash
docker network ls
docker network inspect app-net
docker network connect app-net CONTAINER
docker network disconnect app-net CONTAINER
docker port CONTAINER
~~~

## Troubleshooting order

1. Confirm both containers are running.
2. Confirm they share a network.
3. Use the correct container/service name.
4. Confirm the process listens on `0.0.0.0`, not only `127.0.0.1`.
5. Confirm the internal port.
6. Check published host ports only when host access is required.

# 06 — Storage, Volumes, and Bind Mounts

A container has a writable layer, but that layer belongs to the container. Deleting the container deletes that writable data.

## Storage types

| Type | Managed by | Best use |
|---|---|---|
| Volume | Docker | Persistent application and database data |
| Bind mount | User/host | Source code and configuration during development |
| tmpfs | Memory | Temporary sensitive or high-speed data |

## Named volume

~~~bash
docker volume create db-data
docker run -d --name db -v db-data:/var/lib/postgresql/data postgres:17
docker volume inspect db-data
~~~

The volume survives container replacement.

## Bind mount

~~~bash
docker run --rm -v "$PWD":/workspace -w /workspace alpine ls
~~~

A bind mount exposes a host path inside the container. Changes may be visible in both places. On PowerShell, use the appropriate current-directory syntax for the shell.

## Explicit mount syntax

~~~bash
docker run --mount type=volume,src=db-data,dst=/data IMAGE
docker run --mount type=bind,src=/host/path,dst=/app IMAGE
~~~

`--mount` is longer but clearer.

## Important rules

- never assume container writable data is persistent
- back up important volumes
- avoid mounting the Docker socket unless you fully understand the security impact
- use read-only mounts when write access is unnecessary
- do not commit real `.env` files or secrets
- inspect before pruning volumes

~~~bash
docker volume ls
docker volume inspect NAME
docker volume prune
~~~

`docker volume prune` deletes unused volumes and can destroy data.

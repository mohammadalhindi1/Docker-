# Docker: From Zero to Deployment

A practical Docker reference covering the concepts, commands, storage, networking, image builds, Compose, security, troubleshooting, and reproducible labs required to move from first container to a small multi-service application.

## What is Docker?

Docker is a platform for building, distributing, and running applications in isolated environments called **containers**. It packages application code, runtime dependencies, and configuration into portable **images**.

Docker helps reduce environment differences, simplify delivery, and make builds and tests more reproducible.

## Core mental model

~~~text
Source Code + Dockerfile
          |
      docker build
          |
        Image -------- docker push --------> Registry
          |
       docker run
          |
       Container
~~~

| Object | Meaning |
|---|---|
| Dockerfile | Recipe used to build an image |
| Image | Immutable application package and template |
| Container | Running or stopped instance of an image |
| Registry | Service that stores and distributes images |
| Volume | Persistent storage managed by Docker |
| Network | Communication boundary connecting containers |
| Compose | Definition of a multi-container application |

See the complete [Docker glossary](docs/00-glossary.md).

## Documentation

| # | Guide | Covers |
|---|---|---|
| 00 | [Glossary](docs/00-glossary.md) | Essential Docker terminology |
| 01 | [What is Docker?](docs/01-what-is-docker.md) | Purpose, architecture, benefits, and containers versus VMs |
| 02 | [Images and containers](docs/02-images-and-containers.md) | Images, containers, tags, state, `run` versus `start` |
| 03 | [Docker Hub and registries](docs/03-docker-hub-and-registries.md) | Pulling, tagging, pushing, tags, and digests |
| 04 | [Dockerfile](docs/04-dockerfile.md) | Build instructions, context, CMD, and ENTRYPOINT |
| 05 | [Layers and build cache](docs/05-image-layers-and-build-cache.md) | Cache behavior and multi-stage builds |
| 06 | [Storage and volumes](docs/06-storage-and-volumes.md) | Writable layers, volumes, bind mounts, and tmpfs |
| 07 | [Docker networking](docs/07-docker-networking.md) | Drivers, DNS, port publishing, and debugging |
| 08 | [Docker Compose](docs/08-docker-compose.md) | Services, networks, volumes, and health checks |
| 09 | [Lifecycle and signals](docs/09-container-lifecycle-and-signals.md) | PID 1, exit codes, signals, and restart policies |
| 10 | [Security best practices](docs/10-security-best-practices.md) | Users, capabilities, secrets, limits, and supply chain |
| 11 | [Troubleshooting](docs/11-troubleshooting.md) | Evidence-based diagnosis of common failures |

## Command reference

The [Docker command reference](cheat-sheets/docker-commands.md) groups the most useful commands by purpose:

- images and registries
- container lifecycle
- build and cache
- logs, inspection, and debugging
- volumes and networks
- Docker Compose
- cleanup and disk usage

## Practical labs

| Lab | Focus |
|---|---|
| [01 — Hello Docker](labs/01-hello-docker/README.md) | First container and lifecycle |
| [02 — Nginx container](labs/02-nginx-container/README.md) | Detached mode, port publishing, logs, and exec |
| [03 — Custom image](labs/03-custom-image/README.md) | Dockerfile, build context, tags, and runtime configuration |
| [04 — Volumes](labs/04-volumes/README.md) | Data surviving container deletion |
| [05 — Container network](labs/05-container-network/README.md) | User-defined bridge and container DNS |
| [06 — Docker Compose](labs/06-docker-compose/README.md) | Declarative service configuration and bind mounts |

Each lab includes commands, inspection steps, cleanup, and challenges.

## Complete example project

The [two-tier web application](projects/two-tier-web-app/README.md) combines:

- an Nginx frontend and reverse proxy
- a custom non-root Python backend image
- Compose service discovery
- public and internal networks
- a health check
- read-only runtime filesystem
- runtime environment configuration
- basic container hardening

Run it:

~~~bash
cd projects/two-tier-web-app
docker compose up -d --build
docker compose ps
~~~

Open `http://localhost:8080`, then clean up with:

~~~bash
docker compose down
~~~

## Quick command example

~~~bash
docker pull nginx:1.27-alpine
docker run -d --name web -p 8080:80 nginx:1.27-alpine
docker ps
docker logs web
docker exec -it web sh
docker stop web
docker rm web
~~~

## Important distinctions

- `docker run` creates and starts a **new** container.
- `docker start` starts an **existing** stopped container.
- `EXPOSE` documents a port; `-p` publishes it.
- Images are immutable templates; container writable layers are temporary.
- A volume can survive container deletion.
- Inside a container, `localhost` refers to that container.
- Docker Hub stores images; Docker Engine runs containers.
- Containers share a kernel and are not simply small virtual machines.
- Docker Compose and Kubernetes solve different levels of orchestration.

## Knowledge check

Use the [20-question fundamentals quiz](quizzes/fundamentals.md), then compare with the [answer key](quizzes/answers.md).

## Repository structure

~~~text
.
├── cheat-sheets/
├── docs/
├── labs/
│   ├── 01-hello-docker/
│   ├── 02-nginx-container/
│   ├── 03-custom-image/
│   ├── 04-volumes/
│   ├── 05-container-network/
│   └── 06-docker-compose/
├── projects/
│   └── two-tier-web-app/
├── quizzes/
├── CONTRIBUTING.md
├── LICENSE
└── references.md
~~~

## Safety notes

Commands such as `docker system prune`, `docker volume prune`, and `docker compose down -v` can delete resources or persistent data. Inspect the target before confirming destructive cleanup.

Never place real credentials in Dockerfiles, images, Compose files, or public repositories.

## References and contributions

Technical references are listed in [references.md](references.md). Contribution guidelines are available in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Released under the [MIT License](LICENSE).

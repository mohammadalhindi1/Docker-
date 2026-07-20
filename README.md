# Docker: From Zero to Deployment

A practical, beginner-friendly Docker learning repository that explains the core ideas, demonstrates the essential commands, and turns theory into working containers.

## Why this repository exists

Docker becomes useful only when you understand the complete flow:

**source code -> Dockerfile -> image -> container -> registry -> deployment**

This repository combines short explanations with reproducible labs. It is designed for students, junior DevOps engineers, cloud learners, and developers who want a reliable Docker reference.

## Learning path

| Step | Topic | Outcome |
|---|---|---|
| 1 | [What is Docker?](docs/01-what-is-docker.md) | Understand the problem Docker solves |
| 2 | [Images and containers](docs/02-images-and-containers.md) | Understand Docker's core objects |
| 3 | [Docker Hub and registries](docs/03-docker-hub-and-registries.md) | Learn how images are stored and shared |
| 4 | [Command reference](cheat-sheets/docker-commands.md) | Use the essential CLI commands safely |
| 5 | [Hello Docker](labs/01-hello-docker/README.md) | Run and inspect a first container |
| 6 | [Nginx web server](labs/02-nginx-container/README.md) | Publish a container port |
| 7 | [Build a custom image](labs/03-custom-image/README.md) | Package a small application |

## Mental model

~~~text
Dockerfile --docker build--> Image --docker run--> Container
                                 |
                                 +--docker push--> Registry
~~~

- A **Dockerfile** is the recipe.
- An **image** is the packaged, read-only template.
- A **container** is a running or stopped instance of an image.
- A **registry** stores and distributes images.
- Docker Hub is a public registry service.

## Quick start

~~~bash
docker --version
docker run hello-world
docker run -d --name web -p 8080:80 nginx
docker ps
docker logs web
docker stop web
docker rm web
~~~

Open `http://localhost:8080` after starting the Nginx container.

## Repository roadmap

The next stages will add:

- Dockerfiles in depth
- image layers, cache, tags, and multi-stage builds
- volumes and persistent data
- bridge networks and container DNS
- Docker Compose
- health checks and resource limits
- security and production best practices
- troubleshooting scenarios
- a complete containerized application
- quizzes and interview questions

## How to study

1. Read one document.
2. Predict what each command will do.
3. Run the related lab.
4. Inspect the container instead of stopping at “it works.”
5. Remove the resources and repeat without copying.

## Requirements

- Docker Desktop on Windows/macOS, or Docker Engine on Linux
- a terminal
- Git
- a text editor

Verify the installation:

~~~bash
docker version
docker info
~~~

## Important note

Containers are not lightweight virtual machines. They are isolated processes that share the host kernel. Docker packages the application and its dependencies while the host operating system still provides the kernel.

## License

This repository is intended for learning and portfolio use.

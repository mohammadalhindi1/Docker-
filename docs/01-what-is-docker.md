# 01 — What Is Docker?

## The problem Docker solves

An application may work on a developer's laptop but fail elsewhere because of different:

- dependency versions
- operating-system libraries
- environment variables
- configuration files
- runtime versions

Docker packages the application with the user-space files and dependencies it needs. That package can be run consistently on another machine that has a compatible Docker environment.

## What Docker is

Docker is a platform for building, distributing, and running applications in isolated environments called **containers**.

The word “Docker” may refer to several related parts:

- **Docker Engine:** builds images and runs containers.
- **Docker CLI:** the `docker` command used to communicate with the Engine.
- **Docker Desktop:** a desktop application that includes Docker Engine, CLI, Compose, and a Linux VM where required.
- **Docker Hub:** an online registry used to store and share images.
- **Docker Compose:** defines and runs multi-container applications.

## Why Docker matters

Docker provides:

- consistent application environments
- fast startup compared with full virtual machines
- reproducible builds
- simpler developer onboarding
- application isolation
- easier CI/CD and deployment
- efficient use of infrastructure

Docker does not automatically make an application secure, scalable, or production-ready. It provides a consistent packaging and runtime model; good engineering is still required.

## Containers versus virtual machines

| Virtual machine | Container |
|---|---|
| Includes a complete guest OS | Shares the host kernel |
| Usually larger | Usually smaller |
| Usually slower to start | Usually starts quickly |
| Strong machine-level isolation | Process-level isolation |
| Runs through a hypervisor | Runs through a container runtime |

On Windows, Docker Desktop commonly runs Linux containers inside a lightweight Linux VM. The containers share that VM's Linux kernel, not the Windows kernel directly.

## What happens when you run a container?

When you execute:

~~~bash
docker run nginx
~~~

Docker generally:

1. checks whether the `nginx` image exists locally
2. pulls it from the configured registry if it is missing
3. creates a new container from the image
4. adds a writable container layer
5. configures isolation, networking, and storage
6. starts the image's default process
7. attaches your terminal unless detached mode is used

A container lives only while its main process is running. If that process exits, the container stops.

## When Docker is useful

Docker is especially useful for:

- web applications and APIs
- databases used during development
- automated testing
- CI/CD jobs
- microservices
- reproducible training environments
- packaging 42 projects for easy testing

Docker is less useful when it adds complexity without solving a real environment or deployment problem.

## Check your understanding

1. Does a container include its own kernel?
2. What problem does “works on my machine” describe?
3. Why does a container usually start faster than a VM?
4. What is the difference between Docker CLI and Docker Engine?
5. What causes a container to stop?

Answers: no; inconsistent environments; it starts isolated processes rather than a complete guest OS; the CLI sends requests to the Engine; its main process exits.

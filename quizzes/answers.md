# Docker Fundamentals — Answer Key

1. An image is an immutable template; a container is its runtime instance with configuration and a writable layer.
2. `run` creates a new container, then starts it; `start` starts an existing container.
3. No. Containers normally share the host kernel.
4. Its main process.
5. A reusable, content-addressed filesystem change in an image.
6. The files available to the builder for a build.
7. To exclude unnecessary or sensitive files and reduce context size.
8. `ENTRYPOINT` defines the executable; `CMD` provides a default command or arguments.
9. No. It documents the intended port.
10. Host port 8080 is forwarded to container port 80.
11. A volume survives container replacement or deletion.
12. Sharing host source/configuration, especially during development.
13. The same container, not another container or the host.
14. Through Docker's embedded DNS using container/service names.
15. Services, networks, volumes, configuration, and related multi-container application settings.
16. No. Basic startup ordering does not prove application readiness; health conditions or retries may be needed.
17. To keep compilers and build tools out of the final runtime image.
18. It can provide powerful control over the Docker host.
19. It is a movable label and does not guarantee fixed content.
20. `docker ps -a`, `docker logs`, and `docker inspect`, followed by relevant resource and network checks.

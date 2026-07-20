# 03 — Docker Hub and Registries

## What is a registry?

A container registry is a service that stores and distributes container images.

Common registries include:

- Docker Hub
- GitHub Container Registry
- Amazon Elastic Container Registry
- Azure Container Registry
- Google Artifact Registry

Docker Hub is a registry service; it is not the Docker Engine and it does not run your local containers.

## Image name structure

A full image reference can look like:

~~~text
docker.io/library/nginx:1.27
~~~

- `docker.io`: registry
- `library`: namespace
- `nginx`: repository
- `1.27`: tag

For a personal image:

~~~text
docker.io/username/my-app:v1
~~~

## Pulling an image

~~~bash
docker pull nginx:1.27
~~~

Docker downloads only the missing layers. If another local image already uses an identical layer, Docker can reuse it.

## Publishing an image

~~~bash
docker login
docker tag my-app:local username/my-app:v1
docker push username/my-app:v1
~~~

Never place passwords or access tokens inside a Dockerfile, image, or public repository.

## Tags versus digests

A tag may be changed to point to different image content:

~~~text
my-app:v1
~~~

A digest represents specific content:

~~~text
my-app@sha256:...
~~~

Tags are convenient for humans. Digests provide stronger reproducibility.

## Public and private repositories

- Public repositories can generally be pulled by anyone.
- Private repositories require authentication and access permission.
- Publishing an image can expose files accidentally copied during the build.

Use a `.dockerignore` file and inspect what enters the build context.

## Useful commands

~~~bash
docker search nginx
docker pull nginx:1.27
docker image inspect nginx:1.27
docker login
docker logout
docker push username/my-app:v1
~~~

## Good practice

- use trusted or official base images
- prefer specific version tags
- keep images small
- scan images for vulnerabilities
- never bake secrets into images
- rebuild images to receive patched dependencies
- document the source and purpose of every published image

## Check your understanding

1. Does Docker Hub run containers on your laptop?
2. Why might a pull skip some layers?
3. What is the role of an image namespace?
4. Which is more exact: a tag or digest?
5. Why is `.dockerignore` important?

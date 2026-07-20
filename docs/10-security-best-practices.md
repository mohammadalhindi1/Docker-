# 10 — Docker Security Best Practices

Containers provide isolation, not a perfect security boundary.

## Image security

- use trusted, maintained base images
- pin intentional versions
- rebuild regularly for security patches
- scan images
- remove unnecessary packages and tools
- use multi-stage builds
- protect the build context with `.dockerignore`

## Runtime security

- run as a non-root user
- use a read-only filesystem where possible
- drop unnecessary Linux capabilities
- avoid privileged mode
- apply CPU and memory limits
- publish only required ports
- keep Docker Engine and the host updated

Example:

~~~bash
docker run --read-only \
  --cap-drop ALL \
  --memory 256m \
  --cpus 0.5 \
  --user 10001:10001 \
  IMAGE
~~~

## Secrets

Never store secrets in:

- Dockerfiles
- image layers
- public Compose files
- source repositories
- build arguments when they may persist in metadata or history

Use a proper secret-management mechanism for the deployment environment. Environment variables are configuration delivery, not automatic secret protection.

## Dangerous access

Mounting `/var/run/docker.sock` effectively grants powerful control over the Docker host. Avoid it unless the architecture explicitly requires it and the risk is understood.

## Supply chain

- review third-party images
- prefer minimal permissions for registries
- use immutable digests when exact provenance matters
- generate software inventory where appropriate
- sign and verify images in mature delivery pipelines

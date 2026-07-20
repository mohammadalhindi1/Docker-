# Lab 04 — Persistent Data with a Volume

Create a named volume and write data through one container:

~~~bash
docker volume create learning-data

docker run --rm \
  -v learning-data:/data \
  alpine sh -c 'echo "persistent value" > /data/message.txt'
~~~

Read it from a completely new container:

~~~bash
docker run --rm \
  -v learning-data:/data:ro \
  alpine cat /data/message.txt
~~~

The first container was removed, but the data remained in the volume.

Inspect and clean up:

~~~bash
docker volume inspect learning-data
docker volume rm learning-data
~~~

Challenges:

1. Try the same experiment without a volume.
2. Mount the volume read-only and attempt to modify the file.
3. Explain why deleting a container did not delete the named volume.

# 09 — Container Lifecycle, Processes, and Signals

A container is running while its main process, PID 1 inside the container, is running.

## Common states

- created
- running
- paused
- restarting
- exited
- dead

~~~bash
docker ps -a
docker inspect -f '{{.State.Status}} {{.State.ExitCode}}' CONTAINER
~~~

## Foreground and detached modes

~~~bash
docker run nginx
docker run -d nginx
~~~

Detached mode changes terminal attachment; it does not change what keeps the container alive.

Avoid fake keep-alive commands such as `tail -f /dev/null` for real applications. Run the actual application as the main process.

## Signals

`docker stop` sends the configured stop signal and waits before forcing termination. `docker kill` sends a signal immediately.

~~~bash
docker stop --time 20 app
docker kill --signal SIGTERM app
~~~

Applications should handle termination signals and shut down cleanly.

## Restart policies

~~~bash
docker run -d --restart unless-stopped IMAGE
~~~

Common policies:

- `no`
- `on-failure`
- `always`
- `unless-stopped`

A restart policy can recover a process, but it does not fix a broken application or replace monitoring.

## Exit codes

- `0`: successful completion
- non-zero: application or command failure
- `125`: Docker could not run the container
- `126`: command could not be invoked
- `127`: command not found
- `137`: commonly killed with SIGKILL, possibly due to an out-of-memory event

Always confirm the actual state and logs before diagnosing from an exit code alone.

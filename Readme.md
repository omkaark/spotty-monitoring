<p align="center">
  <img src="https://i.ibb.co/qDvxTGY/sidecar.png" height="150" alt="Spotty Sidecar" />
</p>

# Spotty Monitoring

Spotty Monitoring is a lightweight, Python-based sidecar container designed to monitor standalone containers and also containers in the Spotty Container Orchestrator (my k8s dupe only for spot containers). It provides real-time statistics (and soon logs) for Docker containers running on EC2 instances.

## Features

- Real-time CPU and memory usage monitoring
- Network I/O statistics
- Container logs streaming (Coming soon)

## Prerequisites

- Docker

## Installation

1. Pull the image:

   ```
   docker pull omkaark/spotty-monitoring:latest
   ```

## Usage

### Running as a standalone container

To run Spotty Monitoring as a standalone container:

```bash
docker run -d --name monitor-container \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -p 3928:3928 \
    omkaark/spotty-monitoring:latest
```

### Running as a sidecar (recommended)

To monitor a container (remember to name it 'main-container' using --name):

```bash
docker run -d --name monitor-container \
    --network container:main-container \
    -v /var/run/docker.sock:/var/run/docker.sock \
    omkaark/spotty-monitoring:latest
```

### Accessing the monitoring interface

Once the container is running, you can access the monitoring interface at:

```
http://localhost:3928
```

## API Endpoints

- `/`: Welcome message used as health check
- `/stats`: Get current container statistics
- `/tasks`: List all running containers

## Development

Ensure there is a container in your environment named 'main-container'.

To run the application in development mode:

```bash
python app.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

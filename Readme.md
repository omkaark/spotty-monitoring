# Spotty Monitoring

Spotty Monitoring is a lightweight, Python-based container monitoring solution designed to work with the Spotty Container Orchestrator (my k8s dupe only for spot containers). It provides real-time statistics (and soon logs) for Docker containers running on EC2 instances.

## Features

- Real-time CPU and memory usage monitoring
- Network I/O statistics
- Container logs streaming (Coming soon)

## Prerequisites

- Docker
- Python 3.8+
- pip

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/spotty-monitoring.git
   cd spotty-monitoring
   ```

2. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

3. Build the Docker image:
   ```
   docker build -t spotty-monitoring:latest .
   ```

## Usage

### Running as a standalone container

To run Spotty Monitoring as a standalone container:

```bash
docker run -d --name monitor-container \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -p 3928:3928 \
    spotty-monitoring:latest
```

### Running alongside a main container

To monitor a specific container (named 'main-container' using --name):

```bash
docker run -d --name monitor-container \
    --network container:main-container \
    -v /var/run/docker.sock:/var/run/docker.sock \
    spotty-monitoring:latest
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

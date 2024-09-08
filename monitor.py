import docker
import time
import json
from flask import Flask, jsonify, Response, stream_with_context
from datetime import datetime

app = Flask(__name__)
client = docker.from_env()

def get_container_stats(container_id):
    try:
        container = client.containers.get(container_id)
        stats = container.stats(stream=False)
        
        cpu_delta = stats["cpu_stats"]["cpu_usage"]["total_usage"] - stats["precpu_stats"]["cpu_usage"]["total_usage"]
        system_delta = stats["cpu_stats"]["system_cpu_usage"] - stats["precpu_stats"]["system_cpu_usage"]
        num_cpus = len(stats["cpu_stats"]["cpu_usage"]["percpu_usage"])
        cpu_usage_percentage = (cpu_delta / system_delta) * num_cpus * 100.0
        memory_usage = stats["memory_stats"].get("usage", 0)
        memory_limit = stats["memory_stats"].get("limit", 1)    
        memory_rss = stats["memory_stats"].get("stats", {}).get("rss", memory_usage)
        memory_usage_percentage = (memory_rss / memory_limit) * 100.0

        return {
            "cpu_usage_percentage": round(cpu_usage_percentage, 2),
            "memory_usage_percentage": round(memory_usage_percentage, 2),
            "memory_usage_mb": round(memory_rss / (1024 * 1024), 2),
            "memory_limit_mb": round(memory_limit / (1024 * 1024), 2),
            "network_rx_bytes": sum(interface["rx_bytes"] for interface in stats["networks"].values()),
            "network_tx_bytes": sum(interface["tx_bytes"] for interface in stats["networks"].values()),
        }
    except Exception as e:
        return {"error": str(e)}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Docker monitoring service"})

@app.route('/stats')
def stats():
    containers = client.containers.list()
    if not containers:
        return jsonify({"error": "No running containers found"})
    
    container_id = next((container.id for container in containers if container.name == 'main-container'), containers[0].id)
    return jsonify(get_container_stats(container_id))

@app.route('/tasks')
def tasks():
    containers = client.containers.list()
    return jsonify({
        "total_containers": len(containers),
        "container_names": [container.name for container in containers]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3928)
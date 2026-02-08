import subprocess
import json

def collect_k8s_events():
    result = subprocess.run(
        ["kubectl", "get", "pods", "-o", "json"],
        capture_output=True,
        text=True
    )

    pods = json.loads(result.stdout)
    events = []

    for pod in pods["items"]:
        pod_name = pod["metadata"]["name"]
        status = pod.get("status", {})

        container_statuses = status.get("containerStatuses", [])
        for container in container_statuses:
            last_state = container.get("lastState", {})
            terminated = last_state.get("terminated")

            if terminated and terminated.get("reason") == "OOMKilled":
                events.append({
                    "source": "kubernetes",
                    "message": f"Pod {pod_name} was OOMKilled (exit code {terminated.get('exitCode')})"
                })

    return events

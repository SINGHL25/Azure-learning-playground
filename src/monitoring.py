
import random
import matplotlib.pyplot as plt
import os

def sample_metrics_plot(path="results/plots/monitoring_metrics.png"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    times = list(range(24))
    cpu = [random.uniform(10,80) for _ in times]
    plt.figure(figsize=(8,3))
    plt.plot(times,cpu,marker='o')
    plt.title("Sample CPU usage (last 24h)")
    plt.xlabel("Hour")
    plt.ylabel("CPU %")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path

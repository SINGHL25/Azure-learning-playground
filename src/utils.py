
import os
import pandas as pd

def ensure_dirs():
    os.makedirs("results/logs", exist_ok=True)
    os.makedirs("results/screenshots", exist_ok=True)
    os.makedirs("results/plots", exist_ok=True)

def read_csv_safe(path):
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        # return empty sample DataFrame
        return pd.DataFrame([{"Tool":"Demo","Status":"Pass","Time":"5s","Details":"sample"}])

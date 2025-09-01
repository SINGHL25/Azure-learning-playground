

---

### `main.py`
```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.utils import read_csv_safe, ensure_dirs
from src.vm_manager import list_vms_local_demo

ensure_dirs()

st.set_page_config(layout="wide", page_title="Azure Learning Playground")
st.title("Azure Learning Playground - Demo Dashboard")

st.sidebar.header("Quick Actions")
action = st.sidebar.selectbox("Choose demo", [
    "Overview", "List Demo VMs", "Show Example Logs", "Network Topology Plot"
])

if action == "Overview":
    st.header("Overview")
    st.write("Use examples/ and notebooks/ to run automated demos. See docs/ for guides.")
    st.markdown("- Create Azure account → docs/azure_account.md")
    st.markdown("- Try VM creation demo → notebooks/02_create_vm.ipynb")
    st.markdown("- Terraform template examples in examples/terraform")

elif action == "List Demo VMs":
    st.header("Demo: List VMs (local simulated)")
    df = list_vms_local_demo()
    st.table(df)

elif action == "Show Example Logs":
    st.header("Example logs")
    df = read_csv_safe("results/logs/sample_results.csv")
    st.dataframe(df)

elif action == "Network Topology Plot":
    st.header("Network Topology (sample)")
    img = "results/plots/network_topology.png"
    st.image(img, caption="Network topology (sample)")

st.sidebar.markdown("---")
st.sidebar.write("Educational purpose only")

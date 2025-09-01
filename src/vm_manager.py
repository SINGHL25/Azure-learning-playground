
import pandas as pd
import time

def list_vms_local_demo():
    """
    Demo function that returns a DataFrame of sample VMs.
    Replace with azure-mgmt-compute calls for real deployments.
    """
    data = [
        {"name":"vm-demo-1","region":"eastus","os":"Ubuntu","status":"running"},
        {"name":"vm-demo-2","region":"westeurope","os":"Windows","status":"stopped"},
    ]
    return pd.DataFrame(data)

def create_vm_demo(name, region="eastus", os_type="Ubuntu"):
    # Simulate creation delay
    time.sleep(2)
    return {"name":name,"region":region,"os":os_type,"status":"created"}

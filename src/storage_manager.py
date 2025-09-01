
def create_storage_account_demo(name="demostorage", sku="Standard_LRS"):
    return {"account":name,"sku":sku,"status":"created"}

def attach_disk_demo(vm_name, disk_size_gb=128):
    return {"vm":vm_name,"disk_gb":disk_size_gb,"status":"attached"}

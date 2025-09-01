
def create_loadbalancer_demo(name="demoLB", frontend_ip="public"):
    return {"lb":name,"frontend":frontend_ip,"status":"active"}


def create_vnet_demo(name="demoVNet", cidr="10.1.0.0/16"):
    # Simulated VNet object
    return {"vnet":name,"cidr":cidr,"subnets":[{"name":"default","cidr":"10.1.0.0/24"}]}

def create_peering_demo(vnet1, vnet2, allow_forwarding=False):
    return {"from":vnet1,"to":vnet2,"status":"peered","allow_forwarding":allow_forwarding}

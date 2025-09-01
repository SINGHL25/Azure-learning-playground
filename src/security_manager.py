
def create_nsg_rule_demo(nsg_name, rule_name, port, priority=1000, action="Allow"):
    return {"nsg":nsg_name,"rule":rule_name,"port":port,"priority":priority,"action":action}

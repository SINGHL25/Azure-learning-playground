

### `docs/load_balancer.md`
```markdown
# Load Balancer

- Internal vs Public LB
- Backend pool, health probes, rules
- Use with scale sets for autoscaling

Basic example:
```bash
az network lb create -g MyRG -n myLB --sku Standard --vnet-name myVnet --subnet mySubnet

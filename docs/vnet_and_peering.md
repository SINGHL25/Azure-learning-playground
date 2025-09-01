

### `docs/vnet_and_peering.md`
```markdown
# Virtual Networks & Peering

- Create VNet, subnets, NSG
- VNet peering: connect VNets (same region or global)
- Use route tables or VPN Gateway for cross-region connectivity

CLI example:
```bash
az network vnet create -g MyRG -n myVnet --address-prefix 10.1.0.0/16 --subnet-name default --subnet-prefix 10.1.0.0/24
az network vnet peering create -g MyRG --name vnet1-to-vnet2 --vnet-name vnet1 --remote-vnet /subscriptions/xxx/resourceGroups/rg2/providers/Microsoft.Network/virtualNetworks/vnet2 --allow-vnet-access

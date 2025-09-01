

### `docs/security_groups.md`
```markdown
# Network Security Groups & Firewall

- NSG rules control inbound/outbound
- Azure Firewall and Application Gateway for advanced protection
- SSH/RDP best practices: just-in-time, NSG rules for management IPs

Example NSG rule:
```bash
az network nsg create -g MyRG -n myNsg
az network nsg rule create -g MyRG --nsg-name myNsg -n AllowSSH --priority 1000 --destination-port-ranges 22 --access Allow --protocol Tcp --direction Inbound

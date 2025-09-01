

### `docs/security_groups.md`
<img width="2048" height="2048" alt="Gemini_Generated_Image_tifqa3tifqa3tifq (7)" src="https://github.com/user-attachments/assets/ac085bb2-e19d-4244-b7e0-1e723d0462b6" />

```markdown
# Network Security Groups & Firewall

- NSG rules control inbound/outbound
- Azure Firewall and Application Gateway for advanced protection
- SSH/RDP best practices: just-in-time, NSG rules for management IPs

Example NSG rule:
```bash
az network nsg create -g MyRG -n myNsg
az network nsg rule create -g MyRG --nsg-name myNsg -n AllowSSH --priority 1000 --destination-port-ranges 22 --access Allow --protocol Tcp --direction Inbound

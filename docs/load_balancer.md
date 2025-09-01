

### `docs/load_balancer.md`
<img width="2048" height="2048" alt="Gemini_Generated_Image_tifqa3tifqa3tifq (5)" src="https://github.com/user-attachments/assets/38d016c7-81e9-49e2-9cde-5fa1b7f50b80" />

```markdown
# Load Balancer

- Internal vs Public LB
- Backend pool, health probes, rules
- Use with scale sets for autoscaling

Basic example:
```bash
az network lb create -g MyRG -n myLB --sku Standard --vnet-name myVnet --subnet mySubnet


# Monitoring & Alerts
<img width="2048" height="2048" alt="Gemini_Generated_Image_tifqa3tifqa3tifq (6)" src="https://github.com/user-attachments/assets/bff31d14-c947-4bb3-afd9-e6f7d2dc7ff5" />


- Azure Monitor, Log Analytics workspace, Alerts
- Create metric alert via CLI:
```bash
az monitor metrics alert create -g MyRG -n HighCPUAlert --scopes /subscriptions/.../resourceGroups/MyRG/providers/Microsoft.Compute/virtualMachines/myVM --condition "avg Percentage CPU > 80"

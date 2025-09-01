
# Monitoring & Alerts

- Azure Monitor, Log Analytics workspace, Alerts
- Create metric alert via CLI:
```bash
az monitor metrics alert create -g MyRG -n HighCPUAlert --scopes /subscriptions/.../resourceGroups/MyRG/providers/Microsoft.Compute/virtualMachines/myVM --condition "avg Percentage CPU > 80"

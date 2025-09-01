
#!/bin/bash
az network vnet create -g demo-rg -n demoVnet --address-prefix 10.5.0.0/16 --subnet-name default --subnet-prefix 10.5.0.0/24

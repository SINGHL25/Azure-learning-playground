
#!/bin/bash
# Minimal script to create a VM (requires az cli and login)
RESOURCE_GROUP="demo-rg"
VM_NAME="demo-vm"
az group create -n $RESOURCE_GROUP -l eastus
az vm create -g $RESOURCE_GROUP -n $VM_NAME --image UbuntuLTS --admin-username azureuser --generate-ssh-keys

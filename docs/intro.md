
# Introduction to Azure
<img width="2048" height="2048" alt="Gemini_Generated_Image_ee7chree7chree7c" src="https://github.com/user-attachments/assets/765d776f-dc32-4919-946a-fe61e078c51a" />

Azure is Microsoft's cloud platform offering compute, networking, storage and many managed services.

This guide provides practical, hands-on steps to:
- Create an Azure account and subscription
- Use Azure CLI and SDK
- Deploy VMs, VNets, storage, load balancer
- Monitor resources and automate with IaC
'''
azure-learning-playground/
│── README.md                     # Overview, objectives, setup instructions
│── requirements.txt              # Streamlit, matplotlib, Azure SDK, etc.
│── .gitignore                    # Ignore venv, logs, cache, temp files
│── main.py                       # Streamlit dashboard main file
│
├── docs/
│   ├── intro.md                  # Basics of Azure Cloud & setup guide
│   ├── azure_account.md          # Creating & managing Azure account
│   ├── vm_basics.md              # Linux & Windows VM creation
│   ├── vnet_and_peering.md       # Virtual Networks, Peering (regional/global)
│   ├── security_groups.md        # NSG, firewall, tunneling
│   ├── load_balancer.md          # Internal/External load balancer setup
│   ├── storage.md                # Blob, Disk, File storage, attaching disks
│   ├── availability.md           # Availability sets & zones
│   ├── monitoring.md             # Azure Monitor, Alerts, Logs
│   ├── automation.md             # Terraform/ARM/Bicep automation
│   └── ci_cd_azure_devops.md     # CI/CD pipelines using Azure DevOps
│
├── src/
│   ├── __init__.py
│   ├── vm_manager.py             # Python wrapper for creating/deleting VMs
│   ├── vnet_manager.py           # Create VNet, subnets, and peering
│   ├── security_manager.py       # Configure NSGs, firewall rules
│   ├── storage_manager.py        # Blob/File/Disk storage automation
│   ├── lb_manager.py             # Load balancer deployment scripts
│   ├── monitoring.py             # Collect metrics & logs
│   └── utils.py                  # Helper functions (auth, logging)
│
├── examples/
│   ├── terraform/                # Terraform IaC templates
│   │    ├── main.tf              # Example: Create VM + VNet
│   │    └── variables.tf
│   ├── arm_templates/            # Azure Resource Manager templates
│   │    ├── vm.json
│   │    └── vnet.json
│   ├── bicep/                    # Bicep IaC templates
│   │    ├── vm.bicep
│   │    └── vnet.bicep
│   └── scripts/                  # Bash/PowerShell helper scripts
│        ├── create_vm.sh
│        ├── create_vnet.sh
│        └── monitor_metrics.ps1
│
├── notebooks/
│   ├── 01_intro_to_azure.ipynb          # Hello Azure SDK
│   ├── 02_create_vm.ipynb               # Automating VM creation
│   ├── 03_vnet_peering.ipynb            # VNet peering & connectivity
│   ├── 04_load_balancer.ipynb           # Deploy LB with multiple VMs
│   ├── 05_storage_operations.ipynb      # Upload/download blobs, attach disks
│   ├── 06_availability_zones.ipynb      # Deploying HA VMs
│   ├── 07_global_peering_tunnel.ipynb   # Advanced networking demo
│   └── 08_monitoring_alerts.ipynb       # Setup alerts, logs & dashboards
│
├── tests/
│   ├── test_vm_manager.py
│   ├── test_vnet_manager.py
│   ├── test_security_manager.py
│   ├── test_storage_manager.py
│   └── test_lb_manager.py
│
└── results/
    ├── logs/                     # Store execution logs
    ├── screenshots/              # Screenshots of Azure portal
    │    ├── vm_creation.png
    │    ├── vnet_peering.png
    │    ├── lb_dashboard.png
    │    └── storage_blob.png
    └── plots/                    # Auto-generated plots
         ├── network_topology.png
         ├── resource_flow.png
         └── monitoring_metrics.png

'''

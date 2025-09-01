# Minimal Terraform example (educational)
provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "tf-demo-rg"
  location = "eastus"
}

resource "azurerm_virtual_network" "vnet" {
  name                = "tf-demo-vnet"
  address_space       = ["10.2.0.0/16"]
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

# Note: add VM and other resources as exercises


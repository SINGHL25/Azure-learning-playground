
resource vm 'Microsoft.Compute/virtualMachines@2021-07-01' = {
  name: 'bicep-demo-vm'
  location: resourceGroup().location
  properties: {}
}

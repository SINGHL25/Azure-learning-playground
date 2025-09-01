
resource vnet 'Microsoft.Network/virtualNetworks@2021-02-01' = {
  name: 'bicep-demo-vnet'
  location: resourceGroup().location
  properties: {
    addressSpace: {
      addressPrefixes: ['10.4.0.0/16']
    }
  }
}

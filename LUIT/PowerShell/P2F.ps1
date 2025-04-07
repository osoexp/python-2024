# Connect to Azure (if not already authenticated)
# Make sure you've logged in using Connect-AzAccount

# Step 1: Define variables for the deployment
$resourceGroupName = "Project2-RG"  # Name of the Resource Group
$location = "EastUS"               # Azure region for resources
$vmName = "LinuxVM01"              # Name of the Virtual Machine
$adminUsername = "azureuser"       # Admin username for the VM
$sshPublicKeyPath = "~/.ssh/id_rsa.pub" # Path to the SSH public key file
$virtualNetworkName = "Project2-VNet"
$subnetName = "Project2-Subnet"
$networkSecurityGroupName = "Project2-NSG"

# Step 2: Create a Resource Group (if it doesn’t already exist)
Write-Host "Creating Resource Group..."
New-AzResourceGroup -Name $resourceGroupName -Location $location

# Step 3: Create a Virtual Network and Subnet
Write-Host "Creating Virtual Network and Subnet..."
$virtualNetwork = New-AzVirtualNetwork -ResourceGroupName $resourceGroupName `
    -Location $location -Name $virtualNetworkName `
    -AddressPrefix "10.0.0.0/16"
Add-AzVirtualNetworkSubnetConfig -Name $subnetName `
    -AddressPrefix "10.0.1.0/24" -VirtualNetwork $virtualNetwork
$virtualNetwork | Set-AzVirtualNetwork

# Step 4: Create a Network Security Group (NSG) and Allow SSH
Write-Host "Creating Network Security Group and allowing SSH..."
$nsg = New-AzNetworkSecurityGroup -ResourceGroupName $resourceGroupName `
    -Location $location -Name $networkSecurityGroupName
$sshRule = Add-AzNetworkSecurityRuleConfig -Name "AllowSSH" `
    -NetworkSecurityGroup $nsg -Priority 1000 -Access Allow `
    -Protocol Tcp -Direction Inbound -SourceAddressPrefix "*" `
    -SourcePortRange "*" -DestinationAddressPrefix "*" `
    -DestinationPortRange 22
$nsg | Set-AzNetworkSecurityGroup

# Step 5: Deploy the Linux VM with SSH Key
Write-Host "Deploying Linux VM..."
$publicKey = Get-Content -Path $sshPublicKeyPath
$vmConfig = New-AzVMConfig -VMName $vmName -VMSize "Standard_B1s" `
    | Set-AzVMOperatingSystem -Linux -ComputerName $vmName -Credential (New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $adminUsername, (ConvertTo-SecureString -String "PlaceHolderPassword!" -AsPlainText -Force)) `
    | Set-AzVMSourceImage -PublisherName "Canonical" -Offer "UbuntuServer" -Skus "18.04-LTS" -Version "latest" `
    | Add-AzVMNetworkInterface -Id (New-AzNetworkInterface -Name "$vmName-NIC" `
        -ResourceGroupName $resourceGroupName -Location $location `
        -SubnetId $virtualNetwork.Subnets[0].Id `
        -NetworkSecurityGroupId $nsg.Id).Id
New-AzVM -ResourceGroupName $resourceGroupName -Location $location `
    -VM $vmConfig

# Step 6: Set up Auto Scaling using an ARM template
Write-Host "Deploying Auto Scaling with ARM template..."
$templateFilePath = "./autoscaling-template.json" # Path to your ARM template
$parametersFilePath = "./autoscaling-parameters.json" # Path to your parameter file
New-AzResourceGroupDeployment -ResourceGroupName $resourceGroupName `
    -TemplateFile $templateFilePath -TemplateParameterFile $parametersFilePath

Write-Host "Deployment complete!"

from azure.identity import DefaultAzureCredential
from azure.mgmt.containerservice import ContainerServiceClient
client_id = <CLIENT ID>
client_secret =<CLIENT SECRET>
subscription_id =<SUBSCRIPTION ID>
tenant_id = <TENANT ID>
 
# Set up the ContainerServiceClient with retrieved credentials
aks_client = ContainerServiceClient(credential, subscription_id)
 
# List AKS clusters in the subscription
aks_clusters = aks_client.managed_clusters.list()
 
# Print healthy or ready AKS clusters
print("Healthy Azure Kubernetes Service Clusters:")
for aks_cluster in aks_clusters:
    if aks_cluster.provisioning_state.lower() == "succeeded" and aks_cluster.agent_pool_profiles[0].provisioning_state.lower() == "succeeded":
        print(f" - {aks_cluster.name}")

# Running the Azure Kubernetes Service (AKS) Cluster Listing Script
 
This Python script interacts with Azure Kubernetes Service (AKS) to list healthy clusters in the specified Azure subscription.
 
## Prerequisites
 
Before running the script, ensure you have the following:
 
- Azure subscription with access to AKS resources.
- Python installed on your machine.
- Azure SDK for Python installed (`azure-mgmt-containerservice` and `azure-identity` packages).
 
## Setup
 
1. **Install Dependencies**: Install the required Python packages using pip:
 
    ```bash
    pip install azure-mgmt-containerservice azure-identity
    ```
 
2. **Retrieve Azure Credentials**: Obtain the necessary Azure credentials, including `client_id`, `client_secret`, `subscription_id`, and `tenant_id`. You can generate these credentials by registering an Azure Active Directory (AAD) application with appropriate permissions.
 
3. **Update Script**: Open the provided Python script (`list_aks_clusters.py`) in a text editor and replace the placeholders (`client_id`, `client_secret`, `subscription_id`, `tenant_id`) with your actual Azure credentials.
 
## Running the Script
 
1. **Execute Script**: Run the Python script from the command line:
 
    ```bash
    python list_aks_clusters.py
    ```
 
2. **View Output**: The script will list the healthy AKS clusters in the specified Azure subscription. Only clusters that have been successfully provisioned and have all agent pools in a ready state will be displayed.
 
## Example Output
     Healthy Azure Kubernetes Service Clusters:
     my-aks-cluster-1
     my-aks-cluster-2

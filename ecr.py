import boto3

# Create an ECR client object
ecr_client = boto3.client('ecr', region_name='us-east-1')

# Define the name of the ECR repository
repository_name = "my_monitoring_app_image"

# Create the ECR repository
response = ecr_client.create_repository(repositoryName=repository_name)

# Extract the repository URI from the response
repository_uri = response['repository']['repositoryUri']

# Print the repository URI to the console
print(repository_uri)

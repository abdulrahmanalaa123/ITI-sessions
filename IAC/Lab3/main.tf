provider "aws" {
  shared_config_files      = ["/home/tomato/.aws/config"]
  shared_credentials_files = ["/home/tomato/.aws/credentials"]
  region                   = var.region
}

## for running the lambad funciton properly you should use the backend config either dev or prod with config files alongside 
## its proper variables file
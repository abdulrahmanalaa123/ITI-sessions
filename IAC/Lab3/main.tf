provider "aws" {
  shared_config_files      = ["/home/tomato/.aws/config"]
  shared_credentials_files = ["/home/tomato/.aws/credentials"]
  region                   = var.region
}

module "aws_networking" {
  source = "./modules/aws_networking"
  vpc_cidr = var.vpc_cidr
  public_cidr = var.public_cidr
  subnets = var.subnets
}
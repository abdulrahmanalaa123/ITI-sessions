module "aws_networking" {
  source      = "./modules/aws_networking"
  vpc_cidr    = var.vpc_cidr
  public_cidr = var.public_cidr
  subnets     = var.subnets
}
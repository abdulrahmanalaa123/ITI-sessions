resource "aws_elasticache_cluster" "example" {
  cluster_id           = "cluster-example"
  engine               = "redis"
  node_type            = "cache.m4.large"
  num_cache_nodes      = 1
  parameter_group_name = "default.redis3.2"
  engine_version       = "3.2.10"
  port                 = 3000
  security_group_ids   = [module.aws_networking.private_security_group_id]
}

resource "aws_elasticache_subnet_group" "default" {
  name       = "tf-test-redis-subnet"
  subnet_ids = [module.aws_networking.created_subnets["elasticache_subnet"].id]
}
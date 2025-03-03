resource "aws_db_instance" "default" {
  allocated_storage    = 10
  db_name              = "mydb"
  engine               = "mysql"
  engine_version       = "8.0"
  # free teir
  instance_class       = "db.t3.micro"
  username             = "foo"
  password             = "foobarbaz"
  port                 = 3000
  parameter_group_name = "default.mysql8.0"
  db_subnet_group_name = aws_db_subnet_group.default.name
  vpc_security_group_ids = [aws_security_group.private_ssh.id]
  skip_final_snapshot  = true
  publicly_accessible = false
}
resource "aws_db_subnet_group" "default" {
  name       = "main"
  subnet_ids = [aws_subnet.subnets["redis_subnet"].id, aws_subnet.subnets["elasticache_subnet"].id]
  tags = {
    Name = "My DB subnet group"
  }
}

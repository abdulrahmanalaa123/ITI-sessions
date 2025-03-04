resource "aws_security_group" "allow_ssh" {
  vpc_id = aws_vpc.main_vpc.id
  egress = [
    merge({
      description      = "allow_out_all"
      ipv6_cidr_blocks = []
      prefix_list_ids  = []
      security_groups  = []
    self = false }, var.default_egress)
  ]
}

resource "aws_security_group" "private_ssh" {
  vpc_id = aws_vpc.main_vpc.id
  egress = [
    merge({
      description      = "allow_out_all"
      ipv6_cidr_blocks = []
      prefix_list_ids  = []
      security_groups  = []
    self = false }, var.default_egress)
  ]
}

resource "aws_vpc_security_group_ingress_rule" "allow_public_ssh" {
  security_group_id = aws_security_group.allow_ssh.id
  cidr_ipv4         = var.public_cidr
  from_port         = 22
  ip_protocol       = "tcp"
  to_port           = 22
}

resource "aws_vpc_security_group_ingress_rule" "allow_private_ssh" {
  security_group_id = aws_security_group.private_ssh.id
  cidr_ipv4         = var.vpc_cidr
  from_port         = 22
  ip_protocol       = "tcp"
  to_port           = 22
}

resource "aws_vpc_security_group_ingress_rule" "allow_private_3000" {
  security_group_id = aws_security_group.private_ssh.id
  cidr_ipv4         = var.vpc_cidr
  from_port         = 3000
  ip_protocol       = "tcp"
  to_port           = 3000
}
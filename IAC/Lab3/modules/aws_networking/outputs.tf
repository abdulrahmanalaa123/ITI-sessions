output "public_security_group_id" {
  value = aws_security_group.allow_ssh.id
}
output "private_security_group_id" {
  value = aws_security_group.private_ssh.id
}
output "created_subnets" {
  value = aws_subnet.subnets
}
output "main_vpc" {
  value = aws_vpc.main_vpc.id
}
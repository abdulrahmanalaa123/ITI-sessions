resource "aws_instance" "instances" {
  count         = length(var.instances)
  ami           = var.instances[count.index].ami
  instance_type = var.instances[count.index].instance_type
  # TODO
  # select a random subnet with a diminishing set where value of the private is private and the availability zone is equal
  # to the availability zone if exists
  subnet_id = module.aws_networking.created_subnets[var.instances[count.index].subnet].id
  # TODO
  # select security group private where its private and select private_ssh security group
  security_groups = [var.instances[count.index].public ? module.aws_networking.public_security_group_id : module.aws_networking.private_security_group_id]
  root_block_device {
    delete_on_termination = var.default_volume_config.delete_on_termination
    volume_size           = var.default_volume_config.volume_size
    volume_type           = var.default_volume_config.volume_type
  }
  tags = {
    Name = var.instances[count.index].name
  }
  depends_on = [module.aws_networking.created_subnets]
  provisioner "local-exec" {
    command = "echo The servers IP address is ${var.instances[count.index].public ? self.public_ip : self.private_ip}"
  }
}
resource "aws_vpc" "main_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "iti_vpc"
  }
}

resource "aws_internet_gateway" "main_igw" {
    vpc_id = aws_vpc.main_vpc.id
    tags = {
      Name = "iti_igw" 
    }
}

resource "aws_route_table" "public_route_table" {
    vpc_id = aws_vpc.main_vpc.id
    
}
# the default route for the vpc cidr = local is created by default so it doesnt need to be specified
resource "aws_route_table" "private_route_table" {
    vpc_id = aws_vpc.main_vpc.id
}

resource "aws_route" "public_route" {
    route_table_id = aws_route_table.public_route_table.id
    destination_cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main_igw.id  
}

resource "aws_route_table_association" "associate" {
  route_table_id = aws_route_table.public_route_table.id
  subnet_id = aws_subnet.bastion_subnet.id
}



resource "aws_security_group" "allow_ssh" {
    vpc_id = aws_vpc.main_vpc.id
    egress{
        from_port = 0
            to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }   
  
}

resource "aws_security_group" "private_ssh" {
    vpc_id = aws_vpc.main_vpc.id
    egress{
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }   
  
}
resource "aws_vpc_security_group_ingress_rule" "allow_public_ssh" {
    security_group_id =  aws_security_group.allow_ssh.id
    cidr_ipv4 = "0.0.0.0/0"
    from_port = 22
    ip_protocol = "tcp"
    to_port = 22
}
resource "aws_vpc_security_group_ingress_rule" "allow_private_ssh" {
    security_group_id =  aws_security_group.private_ssh.id
    cidr_ipv4 = "10.0.0.0/16"
    from_port = 22
    ip_protocol = "tcp"
    to_port = 22
}
resource "aws_vpc_security_group_ingress_rule" "allow_private_3000" {
    security_group_id =  aws_security_group.private_ssh.id
    cidr_ipv4 = "10.0.0.0/16"
    from_port = 3000
    ip_protocol = "tcp"
    to_port = 3000
}


resource "aws_subnet" "bastion_subnet" {
    vpc_id = aws_vpc.main_vpc.id
    cidr_block = "10.0.2.0/24"
}
resource "aws_subnet" "private_subnet" {
    vpc_id = aws_vpc.main_vpc.id
    cidr_block = "10.0.3.0/24"
}

resource "aws_instance" "bastion_host" {
    ami = "ami-06ee6255945a96aba"
    instance_type = "t2.micro"
    subnet_id     = aws_subnet.bastion_subnet.id
    security_groups = [aws_security_group.allow_ssh.id]
    associate_public_ip_address = true
    root_block_device {
      delete_on_termination = true
      volume_size = 8
      volume_type = "gp3"
    }
}

resource "aws_instance" "private_host" {
    ami = "ami-06ee6255945a96aba"
    instance_type = "t2.micro"
    subnet_id     = aws_subnet.private_subnet.id
    security_groups = [aws_security_group.private_ssh.id]
    root_block_device {
      delete_on_termination = true
      volume_size = 8
      volume_type = "gp3"
    }
}
variable "region" {
  type = string
}
variable "vpc_cidr" {
  type = string
}
variable "public_cidr" {
  type = string
}
variable "subnets" {
  type = list(object({
    name   = string
    cidr   = string
    public = bool
    az     = number
  }))
  default = [{
    name   = "public-subnet"
    cidr   = "10.0.2.0/24"
    public = true
    az     = 0
    },
    {
      name   = "private-subnet"
      cidr   = "10.0.3.0/24"
      public = false
      az     = 0
    }
  ]
}
variable "default_egress" {
  type = object({
    from_port = number
    to_port   = number
    # remvoing quotations on string undefines egress which doesnt make sense
    protocol    = string
    cidr_blocks = list(string)
  })
  default = {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
variable "instances" {
  type = list(object({
    name          = string
    public        = bool
    ami           = string
    instance_type = string
    subnet        = string
  }))
}

variable "default_volume_config" {
  type = object({
    delete_on_termination = bool
    volume_size           = number
    volume_type           = string
  })
  default = {
    delete_on_termination = true
    volume_size           = 8
    volume_type           = "gp3"
  }
}


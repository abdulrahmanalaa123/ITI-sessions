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
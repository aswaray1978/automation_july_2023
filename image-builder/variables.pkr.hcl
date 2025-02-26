variable app_name{
    description = "app name for server"
    type = string
    default = "web-server"
}

variable source_ami{
     description = "AMI ID of source image"
     type = string
     default = "ami-045269a1f5c90a6a0"
}

variable instance_type{
    description = "Instance type of server"
    type = string
    default = "t2.micro"
}

variable ssh_username{
    description = "ssh username of server"
    type = string
    default = "ec2-user"
}

variable region{
    description = "region of server"
    type = string
}

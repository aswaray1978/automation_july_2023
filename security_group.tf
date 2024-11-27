resource "aws_security_group" "allow_ssh_jump_server" {
  name        = "allow_ssh_jump_server"
  description = "Allow ssh into jump server from anywhere"
  vpc_id      = aws_vpc.this.id

  ingress {
    description = "TLS from VPC"
    from_port   = 22
    protocol    = "tcp"
    to_port     = 22
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1" # semantically equivalent to all ports
    cidr_blocks = ["0.0.0.0/0"]

  }

  tags = {
    Name = "allow_jump_server_${local.vpc_name}"
  }

}

resource "aws_security_group" "allow_web_server" {
  name        = "allow_access_web_server"
  description = "Allow ssh and web (80) into web server"
  vpc_id      = aws_vpc.this.id

  dynamic "ingress" {
    for_each = var.inbound_rule_web #ports we want to open
    content {
      from_port       = ingress.value.port
      to_port         = ingress.value.port
      description     = ingress.value.description
      protocol        = ingress.value.protocol
      security_groups = ingress.value.port == 22 ? [aws_security_group.allow_ssh_jump_server.id] : [aws_security_group.lb_sg.id]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1" # semantically equivalent to all ports
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "allow_web_server_${local.vpc_name}"
  }

}

#Create Security Group for ALB
resource "aws_security_group" "lb_sg" {
  name        = "allow_lb"
  description = "Allow access to load balancer from anywhere"
  vpc_id      = aws_vpc.this.id

  ingress {
    description = "TLS from VPC"
    from_port   = 80
    protocol    = "tcp"
    to_port     = 80
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1" # semantically equivalent to all ports
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "allow_lb_sg_${local.vpc_name}"
  }

}

#Create Security Group for Application Server (App-Server)
resource "aws_security_group" "allow_app_server" {
  name        = "allow_access_to_app_server"
  description = "Allow ssh access and requests on port 8080 from app-server"
  vpc_id      = aws_vpc.this.id

  dynamic "ingress" {
    for_each = var.inbound_rule_app #ports we want to open
    content {
      from_port       = ingress.value.port
      to_port         = ingress.value.port
      description     = ingress.value.description
      protocol        = ingress.value.protocol
      security_groups = ingress.value.port == 22 ? [aws_security_group.allow_ssh_jump_server.id] : [aws_security_group.allow_web_server.id]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1" # semantically equivalent to all ports
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "allow_app_server_${local.vpc_name}"
  }
}


#Create Security Group for SQL Server
resource "aws_security_group" "db_sg" {
  name        = "allow_sql_db"
  description = "Allow access to RDS DB from App Server"
  vpc_id      = aws_vpc.this.id

  ingress {
    description     = "TLS from VPC"
    from_port       = 3306
    to_port         = 3306
    protocol        = "tcp"
    security_groups = [aws_security_group.allow_app_server.id]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1" # semantically equivalent to all ports
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "allow_sql_db_sg_${local.vpc_name}"
  }

}
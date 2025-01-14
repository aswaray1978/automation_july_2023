resource "aws_instance" "web_server" {
  ami           = data.aws_ami.this.image_id #Amazon linux ami required if not providing launch template
  instance_type = var.web_server_instance_type
  key_name      = aws_key_pair.this.key_name
  subnet_id     = element([for each_subnet in aws_subnet.private_subnet : each_subnet.id], 0)
  tags = {
    Name = "web_server-${local.vpc_name}"
  }
  #user_data              = file("./user_data.sh")
  vpc_security_group_ids = [aws_security_group.allow_web_server.id]


}


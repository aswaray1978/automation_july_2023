

# resource "null_resource" "this" {
#   #Always run on timestamp...At every run the timestamp() will be updated
#   #Every time you run #terraform apply a new timestamp() will be generated
#   triggers = {
#     always_run = timestamp()
#   }
#   provisioner "local-exec" {
#     command    = "scp -o StrictHostKeyChecking=no -i ~/Downloads/devops-2024.pem ~/Downloads/devops-2024.pem ec2-user@${aws_instance.jump_server.public_ip}:~"
#     on_failure = continue
#     #when = destroy
#   }
#   connection {
#     host = aws_instance.jump_server.public_ip
#     type = "ssh"
#     user = "ec2-user"
#     #file() will get value from given path and give it back as a string
#     private_key = file("~/Downloads/devops-2024.pem")

#   }

#   provisioner "remote-exec" {
#     inline = [
#       "chmod 400 devops-2024.pem"
#     ]
#     on_failure = continue
#   }

#   provisioner "file" {
#     source      = "user_data.sh"
#     destination = "/home/ec2-user/script"
#     on_failure  = continue
#   }
#   depends_on = [aws_instance.jump_server]

# }


 
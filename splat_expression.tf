# resource "aws_instance" "web" {
#   for_each = toset([ "1","2" ])
#   ami = ami-0583d8c7a9c35822c
#   instance_type = "t2.micro"
# }


# #Splat Expression   
# output "public_ip" {
#     value = [for each_instance in aws_instance.web: each_instance.public_ip]
# }

# #Dictionary key/Value  rahul -->key / kiran --> value
# # output "public_ip" {
# #     value = {for rahul, kiran in aws_instance.web: rahul => kiran.public_ip}
# # }
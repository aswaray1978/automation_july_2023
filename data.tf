data "aws_availability_zones" "this" {
  all_availability_zones = true

  filter {
    name   = "opt-in-status"
    values = ["opt-in-not-required"]
  }
}

#Get info about web-lwplabs-packer ami created via packer
data "aws_ami" "this" {
  most_recent = true
  owners      = ["self"]

  filter {
    name   = "name"
    values = ["*-lwplabs-packer"]   #old "*-lwplabs-packer"
  }

  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

#If you want to see result on screen - output block
# output "image_name" {
#   value = data.aws_ami.this.image_id
# }



# resource "aws_key_pair" "this" {
#   key_name   = "my-key"
#   public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAjwL+1Jm9iMWrfk1hqnkAwE4Rjvi3kUO3zoicXlpj4h aswaray.com"
# }




resource "aws_key_pair" "this" {
  key_name   = "my-aws-key"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC7KuAGUzEgShiw6VfMd24B44sQcQF2jYRhuuJxjKyIN+X1dhE7nQ6/h9rYpQ3oevptKtr2vxIL0x6BhniF8F9w17w32wzbIZU23XPT/inrOgrOK4O80d0zx105hW4yyKSnHbJm8ED4A6IuhUbFesX9+4q7bbkzok2x6QN3wLovCUGGOc5B2XmkkTS87vIniK62gSiDpNIduBu0V2WfL427oYA0z2vFpj0m5wMVPF6PYQyBV+45eig9hHFwYklUiUygF9StEDDfjBm2wlwLBgKqAiOp7RfZaDirnsPsLrywhTgi6SSip+qbdrzQ1ZAo6ARyKtqgOFvm99ZUnFLedVGZ aswaray@hajjsurfacebook"
}

resource "aws_key_pair" "this" {
  key_name   = "my-key"
  public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAjwL+1Jm9iMWrfk1hqnkAwE4Rjvi3kUO3zoicXlpj4h aswaray.com"
}
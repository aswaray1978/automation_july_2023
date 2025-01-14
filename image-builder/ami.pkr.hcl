locals{
   image_name = "${var.app_name}-lwp-packer"

}


source "amazon-ebs" "this" {
  assume_role {
    role_arn     = "arn:aws:iam::503561419742:role/B60devops-sts-assume-role"
    session_name = "packer-test"
  }
  region        = var.region
  source_ami    = var.source_ami
  instance_type = var.instance_type
  ssh_username  = var.ssh_username
  ami_name      =  local.image_name
  profile = "b60devops"
}

build {
  sources = ["source.amazon-ebs.this"] #list of sources

  provisioner "shell" {
    inline = [
      "sudo yum update -y",
      "sudo yum install httpd -y",
      "sudo systemctl enable httpd",
      "sudo systemctl start httpd",
      "sudo echo '<h1>Welcome to Automation Course 2025 at LWPLabs pvt ltd</h1>'|sudo tee /var/www/html/index.html"
    ]
  }
}



#What is the differene b/n ami builder (Instance-store) vs amazon-ebs 
#Instance store is the image that will be available only til the time the server is terminated
#EBS gives you persistent volume
# All AMIs are categorized as either backed by Amazon EBS or backed by instance store.

#Amazon EBS-backed AMI – The root device for an instance launched from the AMI is an Amazon Elastic Block Store (Amazon EBS) volume created from an Amazon EBS snapshot. Supported for both Linux and Windows AMIs.

#Amazon instance store-backed AMI – The root device for an instance launched from the AMI is an instance store volume created from a template stored in Amazon S3. Supported for Linux AMIs only. Windows AMIs do not support instance store for the root device.
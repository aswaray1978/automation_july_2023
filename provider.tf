terraform {
  required_version = ">=1.4"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~>5.0.0"
    }
    null = {
      source  = "hashicorp/null"
      version = "3.2.3"
    }
  }


  backend "s3" {
    bucket = "b60-state-store-bucket"
    key    = "terraformstatestore-batch-jul-2023/terraform.tfstate"
    region = "us-east-1"
    #Role should have permission to access S3
    #role_arn       = "arn:aws:iam::503561419742:role/B60devops-sts-assume-role"
    assume_role = {
      role_arn = "arn:aws:iam::503561419742:role/B60devops-sts-assume-role"
    }
    profile        = "b60devops"
    dynamodb_table = "terraform_state_lock"
  }
}


provider "aws" {
  region = "us-east-1"
  #profile = "b60devops"
  assume_role {
    role_arn     = "arn:aws:iam::503561419742:role/B60devops-sts-assume-role"
    session_name = "test1"
  }
}



assume_role = {
      role_arn = "arn:aws:iam::503561419742:role/B60devops-sts-assume-role"
    }
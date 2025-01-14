
#resource for aws vpc creation
resource "aws_vpc" "this" {
  cidr_block           = var.cidr_for_vpc
  instance_tenancy     = var.tenancy
  enable_dns_support   = var.enable_dns_support
  enable_dns_hostnames = var.enable_dns_hostnames
  tags = {
    Name = local.vpc_name
  }
}

resource "aws_subnet" "private_subnet" {
  for_each          = { for index, az_name in slice(data.aws_availability_zones.this.names, 0, var.num_subnets) : index => az_name }
  vpc_id            = aws_vpc.this.id
  cidr_block        = cidrsubnet(var.cidr_for_vpc, local.newbits, each.key)
  availability_zone = each.value
  tags = {
    Name = "private_subnet_${each.value}"
  }
}

resource "aws_subnet" "public_subnet" {
  for_each                = { for index, az_name in slice(data.aws_availability_zones.this.names, 0, var.num_subnets) : index => az_name }
  vpc_id                  = aws_vpc.this.id
  cidr_block              = cidrsubnet(var.cidr_for_vpc, local.newbits, each.key + var.num_subnets)
  availability_zone       = each.value
  map_public_ip_on_launch = true
  tags = {
    Name = "public_subnet_${each.value}"
  }
}

resource "aws_default_route_table" "this" {
  default_route_table_id = aws_vpc.this.default_route_table_id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.this.id

  }
  tags = {
    Name = "private_rt_${local.vpc_name}"
  }
}

resource "aws_route_table" "this" {
  vpc_id = aws_vpc.this.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.this.id
  }

  tags = {
    Name = "public_rt_${local.vpc_name}"
  }
}

resource "aws_internet_gateway" "this" {
  vpc_id = aws_vpc.this.id

  tags = {
    Name = "igw_${local.vpc_name}"
  }
}

resource "aws_nat_gateway" "this" {
  allocation_id = aws_eip.this.id
  subnet_id     = element([for each_subnet in aws_subnet.public_subnet : each_subnet.id], 0)

  tags = {
    Name = "nat_gw_${local.vpc_name}"
  }
  depends_on = [aws_internet_gateway.this]
}

resource "aws_eip" "this" {
  domain = "vpc"
}

resource "aws_route_table_association" "public_rt_association" {
  for_each       = { for index, each_subnet in aws_subnet.public_subnet : index => each_subnet.id }
  subnet_id      = each.value
  route_table_id = aws_route_table.this.id
}

resource "aws_route_table_association" "private_rt_association" {
  for_each       = { for index, each_subnet in aws_subnet.private_subnet : index => each_subnet.id }
  subnet_id      = each.value
  route_table_id = aws_default_route_table.this.id
}
#Vars are for passing info into a module. Locals are for storing info inside of a module.

locals {
  vpc_name = "${var.vpc_name}-lwplabs"
  newbits  = var.num_subnets == 1 ? 1 : var.num_subnets == 2 ? 2 : (var.num_subnets == 3 || var.num_subnets == 4) ? 3 : 4
}


# locals {
#   vpc_name=var.env==dev ? "${var.vpc_name}-dev" : "${var.vpc_name}-prod"
# }





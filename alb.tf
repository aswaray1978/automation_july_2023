#Create internet facing ALB
resource "aws_lb" "this" {
  name               = "front-end-alb-${local.vpc_name}"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.lb_sg.id]
  subnets            = [for each_subnet in aws_subnet.public_subnet : each_subnet.id]
}

#Create target group and pass vpc
resource "aws_lb_target_group" "this" {
  name     = "front-end-tg-${local.vpc_name}"
  port     = 80
  protocol = "HTTP"
  vpc_id   = aws_vpc.this.id
}

#Attach instances to target group
resource "aws_lb_target_group_attachment" "this" {
  target_group_arn = aws_lb_target_group.this.arn
  target_id        = aws_instance.web_server.id
  port             = 80
}

#create listener Group
resource "aws_lb_listener" "this" {
  load_balancer_arn = aws_lb.this.arn
  port              = "80"
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.this.arn
  }
}
resource "aws_instance" "devops_nodes" {
  count		= 2
  ami		= "ami-0ec10929233384c7f"
  instance_type = "t3.micro"

  iam_instance_profile = "Terraform-Manager-Role"

  tags = {
    Name = "DevOps-Master-Node"
  }
}

output "instance_public_ip" {
  value = aws_instance.devops_node[0].public_ip

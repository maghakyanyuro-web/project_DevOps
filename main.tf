resource "aws_security_group" "allow_ssh_http" {
  name        = "allow_ssh_http"
  description = "Allow SSH and HTTP inbound traffic"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "devops_nodes" {
  count		= 2
  key_name	= "my-key"
  ami		= "ami-0ec10929233384c7f"
  instance_type = "m7i-flex.large"

  iam_instance_profile = "Terraform-Manager-Role"
  
  vpc_security_group_ids = [aws_security_group.allow_ssh_http.id]

  tags = {
    Name = "DevOps-Master-Node"
  }
}

resource "local_file" "inventory" {
  content  = templatefile("inventory.tpl", {
    ips = aws_instance.devops_nodes[*].public_ip
  })
  filename = "inventory.ini"
}

output "instance_public_ip" {
  value = aws_instance.devops_nodes[*].public_ip
}


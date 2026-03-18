resource "aws_security_group" "server_sg" {
	name = "web_server_sg"
	description = "allow http and ssh"
	vpc_id = aws_vpc.custom.id

	#allow ssh traffic into the instance
	ingress {
		from_port = 22
		to_port = 22
		protocol = "tcp"
		cidr_blocks = ["0.0.0.0/0"]
	}
	#allow http traffic into the instance
	ingress {
		from_port = 80
		to_port = 80
		protocol = "tcp"
		cidr_blocks = ["0.0.0.0/0"]
	}
	#allow internet in the instance
	egress {
		from_port = 0
		to_port = 0
		protocol = "-1"
		cidr_blocks = ["0.0.0.0/0"]
	}
	
}

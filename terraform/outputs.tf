output "instance_public_ip" {
	description = "the public ip addr of the instance"
	value = aws_eip.static_ip.public_ip
}

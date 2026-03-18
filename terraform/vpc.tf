resource "aws_vpc" "custom" {
	cidr_block = "10.0.0.0/16"
	enable_dns_hostnames = true
	
	tags = {
		Name = "production_vpc"
	}
}

resource "aws_subnet" "public_subnet" {
	cidr_block = "10.0.1.0/24"
	map_public_ip_on_launch = true
	vpc_id = aws_vpc.custom.id
	availability_zone = "us-east-1a"	
	tags = {
		Name = "public_subnet"
	}
}

resource "aws_internet_gateway" "igw" {
	vpc_id = aws_vpc.custom.id

	tags = {
		Name = "production-igw"
	}
}

resource "aws_route_table" "public_rt" {
	vpc_id = aws_vpc.custom.id
	
	route {
		cidr_block = "0.0.0.0/0"      
		gateway_id = aws_internet_gateway.igw.id
	}
	
	tags = {
		Name = "public-route-table"
	}

}


resource "aws_route_table_association" "publicassoc" {
	subnet_id = aws_subnet.public_subnet.id
	route_table_id = aws_route_table.public_rt.id
}



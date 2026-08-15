#regions
variable "regions" {
  description = "The AWS region to deploy resources in."
  type        = string
  default     = "ap-south-1"
}

#vpc_cidr
variable "vpc_cidr" {
  description = "The CIDR block for the VPC."
  type        = string
  default     = "10.0.0.0/16"
}
#subnet_cidr
variable "subnet_cidr" {
  description = "The CIDR block for the subnet."
  type        = string
  default     = "10.0.1.0/24"
}
#instance_type
variable "instance_type" {
  description = "The type of instance to launch."
  type        = string
  default     = "t3.micro"
}
variable "ami_id" {
  description = "The AMI ID for the instance."
  type        = string
  default     = "ami-0c55b159cbfafe1f0"
}
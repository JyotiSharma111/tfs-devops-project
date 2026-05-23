variable "aws_region" {
  description = "AWS region to deploy into"
  default     = "us-east-1"
}

variable "app_name" {
  description = "Name of the application"
  default     = "tfs-devops-app"
}

variable "container_port" {
  description = "Port the container listens on"
  default     = 8000
}
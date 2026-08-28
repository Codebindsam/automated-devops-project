terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "app" {
  name         = "automated-devops-app:latest"
  keep_locally = true
}

resource "docker_container" "app" {
  name  = "terraform-devops-container"
  image = docker_image.app.image_id

  ports {
    internal = 5000
    external = 5001
  }
}

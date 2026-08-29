terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

data "docker_image" "app" {
  name = "automated-devops-app:latest"
}

resource "docker_container" "app" {
  name  = "terraform-devops-container"
  image = data.docker_image.app.image_id

  ports {
    internal = 5000
    external = 5001
  }
}

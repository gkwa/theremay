packer {
  required_plugins {
    incus = {
      version = ">= 1.0.0"
      source  = "github.com/bketelsen/incus"
    }
  }
}

source "incus" "jammy" {
  image        = "images:ubuntu/jammy"
  output_image = "example-001"
  reuse        = true
}

build {
  sources = ["incus.jammy"]
  provisioner "shell" {
    scripts = [
      "provision.sh",
    ]
  }
}
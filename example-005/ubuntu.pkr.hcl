packer {
  required_plugins {
    incus = {
      version = ">= 1.0.0"
      source  = "github.com/bketelsen/incus"
    }
  }
}

source "incus" "jammy" {
  image        = "images:ubuntu/jammy/cloud"
  output_image = "example-005"
  reuse        = true
}

build {
  sources = ["incus.jammy"]

  provisioner "file" {
    source      = "cloud-init.yml"
    destination = "/etc/cloud/cloud.cfg.d/custom-cloud-init.cfg"
    max_retries = 10
  }

  provisioner "shell" {
    inline = [
      "cloud-init status --wait",
    ]
  }
}
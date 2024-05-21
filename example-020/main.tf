terraform {
  required_providers {
    incus = {
      source = "lxc/incus"
    }
  }
}

resource "incus_instance" "instance1" {
  image = "my-jammy-image"
  name  = "my-jammy-instance"

  config = {
    "boot.autostart" = false
  }
}

terraform {
  required_providers {
    incus = {
      source = "lxc/incus"
    }
  }
}

resource "incus_instance" "instance1" {
  image = "example-005"
  name  = "example-005"

  config = {
    "boot.autostart" = false
  }
}

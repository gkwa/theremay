terraform {
  required_providers {
    incus = {
      source = "lxc/incus"
    }
  }
}

resource "incus_instance" "instance1" {
  image = "example-001"
  name  = "example-001"

  config = {
    "boot.autostart" = false
  }


}

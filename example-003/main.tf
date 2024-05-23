terraform {
  required_providers {
    incus = {
      source = "lxc/incus"
    }
  }
}

resource "incus_instance" "instance1" {
  image = "example-003"
  name  = "example-003"

  config = {
    "boot.autostart" = false
  }


}

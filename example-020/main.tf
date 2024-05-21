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

   provisioner "local-exec" {
    command = "incus config set ${self.name} security.nesting true"
  }
}

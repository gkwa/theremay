terraform {
  required_providers {
    incus = {
      source = "lxc/incus"
    }
  }
}

resource "incus_instance" "instance1" {
  image = "example-002"
  name  = "example-002"

  config = {
    "boot.autostart" = false
  }


  provisioner "local-exec" {
    command = "incus config set ${self.name} security.nesting true"
  }

}
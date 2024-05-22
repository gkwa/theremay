terraform {
  required_providers {
    incus = {
      source = "lxc/incus"
    }
  }
}

resource "incus_image" "example_image" {
  source_remote = "ubuntu"
  source_image  = "example-003"
  aliases       = ["example-003"]
}

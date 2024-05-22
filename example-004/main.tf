terraform {
  required_providers {
    incus = {
      source  = "lxc/incus"
    }
  }
}

resource "incus_image" "example_image" {
  source_remote = "images"
  source_image  = "alpine/3.16"
  aliases       = ["example-003"]
}

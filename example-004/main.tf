terraform {
  required_providers {
    incus = {
      source = "lxc/incus"
    }
  }
}

resource "incus_image" "example_image1" {
  source_remote = "images"
  source_image  = "alpine/3.16"
  aliases       = ["example-003"]
}

# resource "incus_image" "example_image2" {
#   source_remote = "local"
#   source_image  = "example-003"
#   aliases       = ["example-003-test"]
# }

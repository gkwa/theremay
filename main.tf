terraform {
  required_providers {
    incus = {
      source = "lxc/incus"
    }
  }
}

resource "incus_instance" "instance1" {
  image = "ubuntu-jammy"
  name  = "instance1"
  config = {
    "boot.autostart" = false
  }
  device {
    name = "eth0"
    type = "nic"
    properties = {
      "nictype" = "bridged"
      "parent"  = incus_network.network1.name
    }
  }
  profiles = ["default"]
}

resource "incus_network" "network1" {
  name = "network1"
  config = {
    "ipv4.address" = "10.0.0.1/24"
    "ipv4.nat"     = true
  }
}

resource "incus_profile" "profile1" {
  name = "profile1"
  device {
    name = "eth0"
    type = "nic"
    properties = {
      "nictype" = "bridged"
      "parent"  = incus_network.network1.name
    }
  }
}

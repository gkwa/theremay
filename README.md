# theremay

Minimal example to create image using packer and provision it with curl and then to use it with terraform.

```bash
time {
  packer init . &&
  packer build ubuntu.pkr.hcl &&
  incus image ls &&
  terraform init &&
  terraform plan -out=tfplan -destroy &&
  terraform plan -out=tfplan &&
  terraform apply tfplan &&
  incus ls &&
  incus exec instance1 -- curl --version
  
  # cleanup
  terraform plan -out=tfplan -destroy &&
  terraform apply tfplan
  incus image rm ubuntu-jammy
}
```


# Links

- https://github.com/lxc/terraform-provider-incus?tab=readme-ov-file#terraform-provider-incus
- https://github.com/lxc/terraform-provider-incus/tree/main/docs/resources
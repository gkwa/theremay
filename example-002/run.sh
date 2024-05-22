#!/usr/bin/env bash

packer init .
packer build ubuntu.pkr.hcl
incus image ls
terraform init
terraform plan -out=tfplan -destroy
terraform plan -out=tfplan
terraform apply tfplan
incus ls
incus exec my-jammy-instance -- curl --version

# cleanup
terraform plan -out=tfplan -destroy
terraform apply tfplan
incus image rm my-jammy-image
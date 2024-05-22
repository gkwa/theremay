#!/usr/bin/env bash


if ! incus image info example-003 &>/dev/null; then
    packer init .
    packer build ubuntu.pkr.hcl
fi

terraform init
terraform plan -out=tfplan
terraform apply tfplan
incus ls example-003
incus exec example-003 -- curl --version


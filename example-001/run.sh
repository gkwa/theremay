#!/usr/bin/env bash


if ! incus image info example-001 &>/dev/null; then
    packer init .
    packer build ubuntu.pkr.hcl
fi

terraform init
terraform plan -out=tfplan
terraform apply tfplan
incus ls example-001
incus exec example-001 -- curl --version

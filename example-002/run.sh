#!/usr/bin/env bash


if ! incus image info example-002 &>/dev/null; then
    packer init .
    packer build ubuntu.pkr.hcl
fi

terraform init
terraform plan -out=tfplan
terraform apply tfplan
incus ls example-002
incus exec example-002 -- docker run hello-world

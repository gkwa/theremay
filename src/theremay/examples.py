examples = [
    [
        {"template": "README.md/README.md.j2", "outfile": "README.md"},
        {"template": "run.sh/run.sh.j2", "outfile": "run.sh"},
        {
            "template": "ubuntu.pkr.hcl/ubuntu.pkr.hcl.j2",
            "outfile": "ubuntu.pkr.hcl",
        },
        {"template": "main.tf/main.tf.j2", "outfile": "main.tf"},
        {"template": "provision.sh/provision.sh.j2", "outfile": "provision.sh"},
    ],
    [
        {"template": "README.md/README.md.j2", "outfile": "README.md"},
        {"template": "run.sh/run.sh.j2", "outfile": "run.sh"},
        {
            "template": "ubuntu.pkr.hcl/ubuntu.pkr.hcl.j2",
            "outfile": "ubuntu.pkr.hcl",
        },
        {"template": "main.tf/main2.tf.j2", "outfile": "main.tf"},
        {"template": "provision.sh/provision.sh.j2", "outfile": "provision.sh"},
    ],
]

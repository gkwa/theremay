examples = [
    [
        {"other_stuff": True},
        {
            "templates": [
                {"template": "README.md.j2", "outfile": "README.md"},
                {"template": "run.sh.j2", "outfile": "run.sh"},
                {"template": "clean.sh.j2", "outfile": "clean.sh"},
                {
                    "template": "ubuntu.pkr.hcl.j2",
                    "outfile": "ubuntu.pkr.hcl",
                },
                {"template": "main.tf.j2", "outfile": "main.tf"},
                {"template": "provision.sh.j2", "outfile": "provision.sh"},
            ]
        },
    ],
    [
        {"other_stuff": True},
        {
            "templates": [
                {"template": "README.md.j2", "outfile": "README.md"},
                {"template": "run2.sh.j2", "outfile": "run.sh"},
                {"template": "clean.sh.j2", "outfile": "clean.sh"},
                {
                    "template": "ubuntu.pkr.hcl.j2",
                    "outfile": "ubuntu.pkr.hcl",
                },
                {"template": "main2.tf.j2", "outfile": "main.tf"},
                {"template": "provision2.sh.j2", "outfile": "provision.sh"},
            ]
        },
    ],
    [
        {"other_stuff": True},
        {
            "templates": [
                {"template": "README.md.j2", "outfile": "README.md"},
                {"template": "run.sh.j2", "outfile": "run.sh"},
                {"template": "clean.sh.j2", "outfile": "clean.sh"},
                {
                    "template": "ubuntu.pkr.hcl.j2",
                    "outfile": "ubuntu.pkr.hcl",
                },
                {"template": "main.tf.j2", "outfile": "main.tf"},
                {"template": "provision.sh.j2", "outfile": "provision.sh"},
            ]
        },
    ],
    [
        {"other_stuff": True},
        {"templates": []},
    ],
    [
        {"other_stuff": True},
        {
            "templates": [
                {"template": "clean.sh.j2", "outfile": "clean.sh"},
            ]
        },
    ],
]

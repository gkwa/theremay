import argparse
import logging
import pathlib

from . import examples, format, main2

__project_name__ = "theremay"


def process_templates(templates, group_num):
    for entry in templates:
        template = entry["template"]
        outfile = entry["outfile"]
        example_name = f"example-{group_num:03d}"
        data = {
            "counter": group_num,
            "example": example_name,
            "packer_output_image": example_name,
            "container_name": example_name,
        }
        rendered = main2.render_template(
            template,
            data=data,
        )
        exdir = pathlib.Path(example_name)
        ofile = exdir / outfile
        ofile.parent.mkdir(exist_ok=True, parents=True)
        ofile.write_text(rendered)


def main() -> int:
    parser = argparse.ArgumentParser(description="Theremay")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    for group_num, group in enumerate(examples.examples, 1):
        for item in group:
            if isinstance(item, dict) and "templates" in item:
                process_templates(item["templates"], group_num)

    format.format(".", verbose=args.verbose)

    return 0

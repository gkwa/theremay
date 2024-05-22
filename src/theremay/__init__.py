import argparse
import logging
import pathlib

from . import examples, main2, format

__project_name__ = "theremay"


def main() -> int:
    parser = argparse.ArgumentParser(description="Theremay")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    for group_num, group in enumerate(examples.examples, 1):
        for entry in group:
            template = entry["template"]
            outfile = entry["outfile"]
            example_name = f"example-{group_num:03d}"
            data = {
                "counter": group_num,
                "example": example_name,
                "output_image": example_name,
            }
            rendered = main2.render_template(
                template,
                data=data,
            )
            exdir = pathlib.Path(example_name)
            ofile = exdir / outfile
            ofile.parent.mkdir(exist_ok=True, parents=True)
            ofile.write_text(rendered)

    format.format(".", verbose=args.verbose)

    return 0

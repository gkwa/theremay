import argparse
import logging
import pathlib
import subprocess

from . import examples, main2

__project_name__ = "theremay"


def format(exdir, verbose=False):
    terraform_cmd = ["terraform", "fmt", "-recursive", str(exdir)]
    terraform_result = subprocess.run(terraform_cmd, capture_output=True, text=True)
    terraform_stdout = terraform_result.stdout
    terraform_stderr = terraform_result.stderr
    terraform_exit_code = terraform_result.returncode

    packer_cmd = ["packer", "fmt", "-recursive", str(exdir)]
    packer_result = subprocess.run(packer_cmd, capture_output=True, text=True)
    packer_stdout = packer_result.stdout
    packer_stderr = packer_result.stderr
    packer_exit_code = packer_result.returncode

    if verbose:
        logging.debug(f"Terraform stdout: {terraform_stdout}")
        logging.debug(f"Terraform stderr: {terraform_stderr}")
        logging.debug(f"Terraform exit code: {terraform_exit_code}")
        logging.debug(f"Packer stdout: {packer_stdout}")
        logging.debug(f"Packer stderr: {packer_stderr}")
        logging.debug(f"Packer exit code: {packer_exit_code}")


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
            data = {
                "counter": group_num,
                "example": f"example-{group_num:03d}",
            }
            rendered = main2.render_template(
                template,
                data=data,
            )
            exdir = pathlib.Path(data["example"])
            ofile = exdir / outfile
            ofile.parent.mkdir(exist_ok=True, parents=True)
            ofile.write_text(rendered)

    format(".", verbose=args.verbose)

    return 0

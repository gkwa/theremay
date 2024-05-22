import concurrent.futures
import logging
import subprocess


def format(exdir, verbose=False):
    def run_command(cmd):
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        terraform_cmd = ["terraform", "fmt", "-recursive", str(exdir)]
        packer_cmd = ["packer", "fmt", "-recursive", str(exdir)]

        terraform_future = executor.submit(run_command, terraform_cmd)
        packer_future = executor.submit(run_command, packer_cmd)

        terraform_result = terraform_future.result()
        packer_result = packer_future.result()

        terraform_stdout = terraform_result.stdout
        terraform_stderr = terraform_result.stderr
        terraform_exit_code = terraform_result.returncode

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

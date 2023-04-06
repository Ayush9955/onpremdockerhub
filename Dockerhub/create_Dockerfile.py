import configparser
import os
import sys
from common.Arg_parser import parse_args
from string import Template


def create_dockerfile(job_name: str, config_path: str, template_path: str, dockerfile_path: str):
    config = configparser.ConfigParser()
    config.read(os.path.join(config_path, "config.ini"))

    template = configparser.ConfigParser()
    template.read(os.path.join(template_path, "template.ini"))

    # Check if job name is valid
    if job_name not in template.sections():
        print(f"Error: Invalid job name '{job_name}'. Available options are {list(template.sections())}")
        return

    # Get the relevant section from the template
    template_section = template[job_name]

    # Create the Dockerfile
    dockerfile_path = os.path.join(dockerfile_path, "Dockerfile")
    with open(dockerfile_path, "w") as dockerfile:
        # Write the base image and version
        dockerfile.write(f"FROM {template_section['FROM']}\n\n")

        # Write environment variables from config file
        for env_var, value in config.items(job_name):
            dockerfile.write(f"ENV {env_var}={value}\n")

        # Write Dockerfile commands from the template
        for key, value in template_section.items():
            if key == "FROM":
                continue
            dockerfile.write(f"{key} {value}\n")

    print(f"Dockerfile created at {dockerfile_path}")


if __name__ == "__main__":
    args = parse_args()
    create_dockerfile(args.job_name, args.config_path, args.template_path, args.dockerfile_path)

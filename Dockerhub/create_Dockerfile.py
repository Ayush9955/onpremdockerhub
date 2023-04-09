import configparser
import os
import sys
from common.Arg_parser import parse_args
from common.template import template


def create_dockerfile(job_name: str, config_path: str, template_path: str, dockerfile_path: str):
    config = configparser.ConfigParser()
    config.read(os.path.join(config_path, "config.ini"))

    # print(template.keys())
    job_config = config[job_name]


    # Check if job name is valid
    if job_name not in config.sections() or not template.keys():
        print(f"Error: Invalid job name '{job_name}'. Available options are {list(config.sections())}")
        return

    
    template_section = template.get(job_name)
    for key, value in config.items(job_name):
        template_section = template_section.replace(f"${{{key}}}", value)
    # Create the Dockerfile
    dockerfile_path = os.path.join(dockerfile_path, "Dockerfile")
    with open(dockerfile_path, "w") as dockerfile:
        dockerfile.write(template_section)

if __name__ == "__main__":
    args = parse_args()
    template=template()
    create_dockerfile(args.job_name, args.config_path, args.template_path, args.dockerfile_path)

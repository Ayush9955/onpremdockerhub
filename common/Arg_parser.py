import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Build and run a Docker container for a web application.")
    parser.add_argument("job_name", choices=["node", "react", "vue", "angular", "django", "flask", "nginx", "perl", "ruby", "fastapi", "java", "golang", "dotnet", "html", "php"], help="Name of the job to deploy")
    parser.add_argument("--config_path", type=str, help="Path to the config file")
    parser.add_argument("--template_path", type=str, help="Path to the template_path")
    parser.add_argument("--dockerfile_path", type=str, help="Path to the dockerfile_path")
    return parser.parse_args()

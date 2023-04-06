import subprocess
import typer

app = typer.Typer()

@app.command()
def build_and_run_docker(dockerfile_path: str, image_tag: str, container_name: str):
    """
    Build a Docker image using the specified Dockerfile, tag it, and run it as a container
    """
    # Build the Docker image
    build_cmd = f"docker build -t {image_tag} -f {dockerfile_path} ."
    subprocess.run(build_cmd, shell=True, check=True)

    # Run the Docker container
    run_cmd = f"docker run --name {container_name} -d {image_tag}"
    subprocess.run(run_cmd, shell=True, check=True)

    typer.echo(f"Image built with tag: {image_tag}")
    typer.echo(f"Container running with name: {container_name}")


if __name__ == '__main__':
    app()

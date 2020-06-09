import click
import subprocess

# @click.command()
# @click.option("--count", default=1, help="Number of greetings.")
# @click.option("--name", prompt="Your name", help="The person to greet.")
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for _ in range(count):
#         click.echo(f"Hello, {name}!")


def get_branch_name():
    out = subprocess.Popen(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    stdout, stderr = out.communicate()
    return stdout.decode("utf-8").replace("\n", "")


@click.command()
@click.option(
    "--message",
    "-m",
    prompt="\033[92mYour commit meesage\033[0m",
    help="The message of your commit",
)
@click.option(
    "--branch",
    "-b",
    prompt="\033[94mYour branch\033[0m",
    default=get_branch_name,
    show_default="Your current branch",
)
def rogit(message, branch):
    click.echo(
        f"\033[1mYou will do a commit on \033[94m{branch}\033[0m \033[1mwith the message: \033[92m{message}\033[0m"
    )


if __name__ == "__main__":
    rogit()

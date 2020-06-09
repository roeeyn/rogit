import click
import subprocess


def get_branch_name():
    out = subprocess.Popen(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    stdout, _stderr = out.communicate()
    return stdout.decode("utf-8").replace("\n", "")


def add_changes():
    out = subprocess.Popen(
        ["git", "add", "-A"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    stdout, _stderr = out.communicate()
    return stdout.decode("utf-8")


def create_commit(message):
    add_changes()
    out = subprocess.Popen(
        ["git", "commit", "--message", message],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    stdout, _stderr = out.communicate()
    return stdout.decode("utf-8")


def push_changes(branch):
    out = subprocess.Popen(
        ["git", "push", "origin", branch],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    stdout, _stderr = out.communicate()
    return stdout.decode("utf-8")


def abort_if_false(ctx, param, value):
    if not value:
        click.echo("\033[93mCommit aborted. Don't worry, you're doing great 🤓\033[0m")
        ctx.exit()


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
@click.option(
    "--yes",
    "-y",
    is_flag=True,
    callback=abort_if_false,
    expose_value=False,
    prompt=f"\033[1m\033[92mConfirm commit and push?\033[0m",
)
def rogit(message, branch):
    click.echo("\033[94mCool 😎! 🔥🔥🔥\n\033[0m")
    click.echo(create_commit(message))
    click.echo(push_changes(branch))
    click.echo("\033[1m\033[92mDone\033[0m")


if __name__ == "__main__":
    rogit()

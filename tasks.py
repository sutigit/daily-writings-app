from invoke import task

@task
def start(ctx):
    ctx.run(f"python3 src/main.py", pty=True)

@task
def config(ctx):
    ctx.run("gedit src/config/config.py", pty=True)
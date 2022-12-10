from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=True)

@task
def config(ctx):
    ctx.run("gedit src/config.py", pty=True)
from fabric.api import *
from fabric.operations import run
from fabric.context_managers import cd
from fabric.api import env, prefix
from fabric.colors import green
HOST_NAME = ['bankcenter.in']
USER = "bankcenter_in"
REPO_PATH = "~/bankcenter/bank_center"

env.hosts = HOST_NAME
env.user = USER
env.directory = REPO_PATH
env.activate = 'source ~/bankcenter/bin/activate'

def restart():
    print(green("Restarting...\n"))
    run("gunicorn_django -c ~/confs/gunicorn/gunicorn_cfg.py")
    print(green("Restarted\n"))

def kill_process():
    print(green("Killing gunicorn process...\n"))
    run("kill `cat ~/confs/gunicorn/pid.txt`")
    print("Killed gunicorn process")

def syncdb():
    print(green("syncdb is running...\n"))
    run("python manage.py syncdb")

def migrate():
    print(green("Migrating database...\n"))
    run("python manage.py migrate")

def pull():
    print(green("Pulling the latest code...\n"))
    run("git pull")

def deploy():
    with cd(env.directory):
        with prefix(env.activate):
            pull()
            migrate()
            syncdb()
            kill_process()
            restart()

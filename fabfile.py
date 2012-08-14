from os import path, pardir
from fabric.api import env, sudo, cd, local, run, settings, prefix, task
from fabric.operations import get, put, open_shell
from fabric.colors import green, red

REMOTE_BASE_PATH = '/var/www/'

key_path = path.join(pardir, pardir, "pwalker.pem")
env.hosts = ['ec2-54-245-118-170.us-west-2.compute.amazonaws.com']
env.user = 'ubuntu'
env.key_filename = key_path

@task
def copy_files():
    """
    Create a zip file with last version of files on git repository
    upload the zip file to the server and unzip in /var/www
    """

    if path.exists('/tmp/wundermind.zip'):
        local('rm -r /tmp/wundermind.zip')

    local('git archive --format=zip --prefix=wundermind/ HEAD > /tmp/wundermind.zip')
    put('/tmp/wundermind.zip', '/tmp')
    
    with cd(REMOTE_BASE_PATH):
        run('unzip -o /tmp/wundermind.zip')


@task
def create_virtualenv():
    """
    Create a virtualenv 
    """
    
    with cd(REMOTE_BASE_PATH):
        run('virtualenv --distribute venv')

@task
def install_deps():
    """
    Install project dependencies from requirements/requirements.txt
    """
    
    with cd(REMOTE_BASE_PATH + 'wundermind/'):
        with prefix('source ' + REMOTE_BASE_PATH + 'venv/bin/activate'):
            run('pip install -r requirements/requirements.txt')

@task
def collectstatic():
    """
    Run django command to collect static files on server
    """
    
    with cd(REMOTE_BASE_PATH + 'wundermind'):
        with prefix('source ' + REMOTE_BASE_PATH + 'venv/bin/activate'):
            run('python manage.py collectstatic --noinput')


def restart_supervisord():
    sudo('supervisorctl restart wundermind')
        
@task
def deploy():
    copy_files()
    install_deps()
    collectstatic()
    restart_supervisord()
    print(green('Deployed successfully', bold=True))

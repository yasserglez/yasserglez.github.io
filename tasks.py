import os
import sys
from pathlib import Path
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

from invoke import task


DEPLOY_PATH = Path('output').resolve()


@task
def clean(c):
    if deploy_path.is_dir():
        c.run(f'rm -rf {DEPLOY_PATH}')
        c.run(f'mkdir {DEPLOY_PATH}')

@task
def build(c):
    if not Path("pelican-plugins").is_dir():
        c.run('git clone --recursive https://github.com/getpelican/pelican-plugins')
    c.run('pelican -s develop_conf.py')


class AddressReuseTCPServer(TCPServer):
    allow_reuse_address = True

@task
def serve(c):
    os.chdir(DEPLOY_PATH)
    port = 8000
    server = AddressReuseTCPServer(('', port), SimpleHTTPRequestHandler)
    sys.stderr.write(f'Serving on port {port}...\n')
    server.serve_forever()


@task
def deploy(c):
    clean(c)
    c.run('pelican -s deploy_conf.py')
    c.run(f'mv {DEPLOY_PATH}/theme/favicon.ico {DEPLOY_PATH}')
    c.run(f'mv {DEPLOY_PATH}/theme/favicon-152.png {DEPLOY_PATH}')
    c.run(f'mv {DEPLOY_PATH}/theme/CNAME {DEPLOY_PATH}')
    c.run("ghp-import -b master -m 'Commit by ghp-import' {DEPLOY_PATH}")
    c.run('git push --force github master')

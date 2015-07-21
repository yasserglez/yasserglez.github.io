# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

import os
import sys
from SimpleHTTPServer import SimpleHTTPRequestHandler
from SocketServer import TCPServer

from fabric.api import *

env.deploy_path = 'output'

def clean():
    if os.path.isdir(env.deploy_path):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican -s develop_conf.py')

def rebuild():
    clean()
    build()

class AddressReuseTCPServer(TCPServer):
    allow_reuse_address = True

def serve():
    os.chdir(env.deploy_path)
    port = 8000
    server = AddressReuseTCPServer(('', port), SimpleHTTPRequestHandler)
    sys.stderr.write('Serving on port {0} ...\n'.format(port))
    server.serve_forever()

def reserve():
    rebuild()
    serve()

def deploy():
    clean()
    local('pelican -s deploy_conf.py')
    local('mv {deploy_path}/theme/favicon.ico {deploy_path}'.format(**env))
    local('mv {deploy_path}/theme/favicon-152.png {deploy_path}'.format(**env))
    local('mv {deploy_path}/theme/CNAME {deploy_path}'.format(**env))
    local('ghp-import -b master -m "Commit by ghp-import" {deploy_path}'.format(**env))
    local('git push --force github master')

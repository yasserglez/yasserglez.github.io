# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

import os
import sys
import SimpleHTTPServer
import SocketServer

from fabric.api import *
import fabric.contrib.project as project

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'

def clean():
    if os.path.isdir(env.deploy_path):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican -s develop_conf.py')
    local('cp theme/static/images/favicon.ico output/')

def rebuild():
    clean()
    build()

def serve():
    os.chdir(env.deploy_path)
    PORT = 8000
    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True
    server = AddressReuseTCPServer(('', PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)
    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    build()
    serve()

def publish():
    local('pelican -s deploy_conf.py')
    local('cp theme/static/images/favicon.ico output/')

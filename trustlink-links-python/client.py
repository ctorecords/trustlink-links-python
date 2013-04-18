# coding: utf-8

from __future__ import absolute_import, unicode_literals

import os
import re
import sys
import socket

PYTHON_VERSION = '-'.join(map(str, sys.version_info[:3]))

class Client(object):
    tl_verbose = 0
    tl_debug = 1
    tl_isrobot =  0
    tl_test = 0
    tl_test_count = 4
    tl_template = 'template'
    tl_charset = 'DEFAULT'
    tl_use_ssl = 0
    tl_server = 'db.trustlink.ru'
    tl_cache_lifetime = 21600
    tl_cache_reloadtime = 3600
    tl_links_db_file = ''
    tl_error = []
    tl_links = {}
    tl_links_page = []
    tl_host = ''
    tl_request_uri = ''
    tl_socket_timeout = 6
    tl_force_show_code = 0
    tl_multi_site = 0
    tl_is_static = 0
    tl_tpath = os.path.dirname(sys.argv[0])
    try:
        remote_addr = os.environ['REMOTE_ADDR']
    except:
        remote_addr = ''

    _inited = 0
    _links_loaded = 0

    def __init__(self, *args, **kwargs):
        self._inited = 0


    def init(self):
        return

    def load_links(self):
        return

    def fetch_remote_file(self, host, path):
        port = 80
        USER_AGENT = 'Trustlink Client Pyhton 0.0.1'

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, 80))
        try:
            sent = s.send("GET %s HTTP/1.0\nHOST:%s\nUSER-AGENT:%s\n\n" % (path, host, USER_AGENT))
        except socket.timeout:
            errMsg = "Connection timed-out while sent request to %s. " % (host)
            raise RuntimeError(errMsg)
        
        if sent == 0:
            raise RuntimeError("socket connection broken")

        msg = ''
        buf = 4096
        try:
            msg = s.recv(buf)

            while True:
                more = s.recv(buf)
                if not more:
                    break
                else:
                    msg += more
        except socket.timeout:
            errMsg = "Connection timed-out while receive response from %s. " % (host)
            raise RuntimeError(errMsg)

        return re.compile(r'\r\n\r\n').split(msg)[1]

    def load_links(self):
        return

    def lc_read(self):
        return

    def lc_write(self, filename, content):
        with open(filename, 'w') as f:
            f.write(content)
            f.close()

        return

    def build_links(self):
        return

    def var_dump(self):
        return

    def rawurldecode(self):
        return

    def trim(self):
        return

    def ltrim(self):
        return

    def rtrim(self):
        return

    


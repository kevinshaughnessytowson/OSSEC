#!/bin/python

import socks

#set proxy for python to use, this will be a tor proxy so tor must be setup for it to work
target_socket = socks.socksocket()
s.setproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 9050)

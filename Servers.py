#!/usr/bin/env python3

'''
Different server classes that I have found useful
'''

import socket

class JobsServer:
    
    def __init__ (self,
                  hostname,
                  port,
                  *,
                  buffer_size = 4096,
                  max_connections = 5):
        self._addr = (port, port)
        
        # default buffer size of 4MB
        self._buffer_size = kwargs.get("buffer_size", 4096)

        # start the server
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.bind(self._addr)
        self.listen(max_connections)
        
    def handle_request (self):
        pass

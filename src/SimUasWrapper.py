#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import subprocess
import traceback
import shlex
import random
from Loggers import Loggers
import os

class Command(object):
    """
    Enables to run subprocess commands in a different thread.
    """
    command = None
    process = None
    status = None
    output, error = '', ''

    myenv = os.environ.copy()
    # myenv["DISPLAY"] = ":0"

    def __init__(self, command):
        # if isinstance(command, basestring):
        #     command = shlex.split(command)
        self.command = command

    def run(self, timeout=None, **kwargs):
        """ Run a command then return: (status, output, error). """
        def target(**kwargs):
            try:
                # self.process = subprocess.Popen(self.command, env=Command.myenv, **kwargs)
                self.process = subprocess.Popen(self.command, executable="/bin/bash", env=Command.myenv, **kwargs)
                self.output, self.error = self.process.communicate()
                self.status = self.process.returncode
            except:
                self.error = traceback.format_exc()
                print(self.error)
                self.status = -1
        # default stdout and stderr
        if 'stdout' not in kwargs:
            kwargs['stdout'] = subprocess.PIPE
        if 'stderr' not in kwargs:
            kwargs['stderr'] = subprocess.PIPE
        # thread
        thread = threading.Thread(target=target, kwargs=kwargs)
        thread.start()
        # thread.join(timeout)
        #if thread.is_alive():
        #    self.process.terminate()
        #    thread.join()
        # return self.status, self.output, self.error


class SimUasWrapper:

    assigned_ports = [] # array of tuple (sys_id, port)
    port_range_start = 14550
    port_range_end = 15550

    @staticmethod
    def assign_port(sys_id, port):
        SimUasWrapper.assigned_ports.append((sys_id, port))
    
    def assign_free_port(self):
        free = False
        port = None
        num_tries = 0
        while not free and num_tries < 10:
            port = random.randint(SimUasWrapper.port_range_start, SimUasWrapper.port_range_end)
            Loggers.debug('assign_free_port: %s' % port)
            print('assign_free_port: %s' % port)
            if port not in [pa[1] for pa in self.assigned_ports]:
                free = True
            num_tries += 1
        if port:
            SimUasWrapper.assign_port(self.sys_id, port)
        return port

    def __init__(self, sys_id):
        self.sys_id = sys_id
        port = self.assign_free_port()
        if port:
            self.port = port
        else:
            raise Exception()
        # self.command = Command('sleep 4; ls -l')
        self.command = Command('sim_vehicle.py -v ArduCopter --console --out=127.0.0.1:%s' % self.port)
        self.command.run(
            timeout=None, 
            stderr=subprocess.STDOUT, 
            stdout=subprocess.PIPE, 
            shell=True,
            cwd=r'/home/vagrant/ardupilot/ArduCopter'
        )


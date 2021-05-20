#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from SimUasWrapper import SimUasWrapper
from Uas import Uas
from Loggers import Loggers
import threading
import time

class SimUasWrapperSpec(unittest.TestCase):

    def test_sim_uas_wrapper_spawn(self):

        uas0 = Uas(0, None)
        Loggers.initialise([
            uas0
            ])
        uas0.boot()
        # su1 = SimUasWrapper(0)
        uas0.connect_mavlink()
        i = 0
        while i < 100:
            try:
                # print('%s:%s %s:%s:%s' % (su1.command.command, su1.command.process.returncode, su1.command.output, su1.command.error, su1.command.status))
                Loggers.sim_vehicle_warning(0, uas0.sim_uas.command.command)
                Loggers.sim_vehicle_warning(0, uas0.sim_uas.command.status)
                Loggers.sim_vehicle_warning(0, uas0.sim_uas.command.output)
                Loggers.sim_vehicle_error(0, uas0.sim_uas.command.error)

                # Mavlink
                uas0.get_mavlink_messages()

            except Exception as e:
                print(str(e))
            time.sleep(1)
            i +=1 

        self.assertEqual(1, 2)


if __name__ == '__main__':
    unittest.main()

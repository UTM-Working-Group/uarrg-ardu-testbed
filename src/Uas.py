import pymavlink
from pymavlink import mavutil
from SimUasWrapper import SimUasWrapper
from Loggers import Loggers


class Uas:

    def __init__(
        self, 
        idx, 
        flight_plan, 
        description=None
    ):
        self.idx = idx
        self.flight_plan = flight_plan
        self.description = description

        # TODO Future 
        ## firmware version
        ## flight controller, etc.

    def __repr__(self):
        return 'UAS[%s]' % self.idx

    def connect_mavlink(self):
        self.sim_uas_mavlink_conn = mavutil.mavlink_connection("udpin:0.0.0.0:%s" % (self.sim_uas.port), baud=115200)

    def get_mavlink_messages(self):
        while True:
            try:
                mm = self.sim_uas_mavlink_conn.recv_match().to_dict()
                print(mm)
                # PARAM_NAME: GLOBAL_POSITION_INT, VFR_HUD
                # OA_TYPE: bendy ruler, dijkstra
                Loggers.mavlink_warning(self.idx, mm)
            except:
                pass

    def boot(self):
        # TODO Start Sim Uas Command
        print("Booting %s" % self)
        self.sim_uas = SimUasWrapper(self.idx)
        # TODO Connect to Telemetry using PyMAVLink
        print("Connecting to Telemetry %s" % self)
        self.connect_mavlink()

    def arm(self):
        print("Arming %s" % self)

    def disarm(self):
        print("Disarming  %s" % self)

    def shutdown(self):
        print("Shutting down %s" % self)

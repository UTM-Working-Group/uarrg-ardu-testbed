class Scenario:

    def __init__(
        self, 
        short_name, 
        description, 
        uass
    ):
        self.short_name = short_name
        self.description = description
        self.uass = uass

    def __repr__(self):
        return "Scenario %s" % self.short_name

    def run(self):
        print("Initialising Loggers")
        Loggers.initialise(self.uass)

        print("="*120)
        print("Running %s" % self)
        print("="*120)
        print(" "*120)
        for uas in self.uass:
            uas.boot()

        print("-"*120)
        print("ARMING")
        print("-"*120)
        for uas in self.uass:
            uas.arm()

        # TODO
        ## Run sim_vehicle.py / mavproxy.py
        ## Use pymavlink to subscribe to telemetry
        ## DCONF API link

        print("-"*120)
        print("DISARMING")
        print("-"*120)
        for uas in self.uass:
            uas.disarm()

        print("-"*120)
        print("SHUTTING DOWN")
        print("-"*120)
        for uas in self.uass:
            uas.shutdown()

        print("="*120)
        print("Completed %s" % self)
        print("="*120)
        print(" "*120)


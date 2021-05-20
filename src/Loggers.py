import logging
import uuid
import os


class Loggers:
    loggers = {}
    ROOT_DIR = 'run'
    FORMATTER = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s', datefmt="%Y-%m-%d %H:%M:%S")

    instance_id = str(uuid.uuid4())
    print(80*'=')
    print("RUN INSTANCE %s" % instance_id)
    print(80*'=')
    print()
    INSTANCE_DIR = '%s/%s' % (ROOT_DIR, instance_id)
    os.mkdir(INSTANCE_DIR)

    @staticmethod
    def initialise(uass):

        # Initialise CORE Logger
        logger = logging.getLogger("CORE")
        handler = logging.FileHandler('%s/CORE.log' % Loggers.INSTANCE_DIR)
        handler.setFormatter(Loggers.FORMATTER)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        Loggers.loggers['CORE'] = logger

        for uas in uass:
            # Initialise SIM VEHICLE Logger
            logger = logging.getLogger("SIM-VEHICLE-%s" % uas.idx)
            handler = logging.FileHandler('%s/SIM-VEHICLE-%s.log' % (Loggers.INSTANCE_DIR, uas.idx))
            handler.setFormatter(Loggers.FORMATTER)
            logger.setLevel(logging.DEBUG)
            logger.addHandler(handler)
            Loggers.loggers["SIM-VEHICLE-%s" % uas.idx] = logger

            # Initialise SIM VEHICLE Logger
            logger = logging.getLogger("MAVLINK-%s" % uas.idx)
            handler = logging.FileHandler('%s/MAVLINK-%s.log' % (Loggers.INSTANCE_DIR, uas.idx))
            handler.setFormatter(Loggers.FORMATTER)
            logger.setLevel(logging.DEBUG)
            logger.addHandler(handler)
            Loggers.loggers["MAVLINK-%s" % uas.idx] = logger

        print('LOGGERS INITIALISED: %s' % str(Loggers.loggers))

    @staticmethod
    def get_sim_vehicle_logger(sys_id):
        return Loggers.loggers['SIM-VEHICLE-%s' % sys_id]

    @staticmethod
    def get_mavlink_logger(sys_id):
        return Loggers.loggers['MAVLINK-%s' % sys_id]

    @staticmethod
    def get_core_logger():
        return Loggers.loggers['CORE']

    ## CORE LOG
    @staticmethod
    def info(msg):
        log = Loggers.get_core_logger()
        log.info(msg)

    @staticmethod
    def debug(msg):
        log = Loggers.get_core_logger()
        log.debug(msg)

    @staticmethod
    def warning(msg):
        log = Loggers.get_core_logger()
        log.warning(msg)

    @staticmethod
    def error(msg):
        log = Loggers.get_core_logger()
        log.error(msg)

    @staticmethod
    def critical(msg):
        log = Loggers.get_core_logger()
        log.critical(msg)

    ## MAVLINK LOG 
    @staticmethod
    def mavlink_info(sys_id, msg):
        log = Loggers.get_mavlink_logger(sys_id)
        log.info(msg)

    @staticmethod
    def mavlink_debug(sys_id, msg):
        log = Loggers.get_mavlink_logger(sys_id)
        log.debug(msg)

    @staticmethod
    def mavlink_warning(sys_id, msg):
        log = Loggers.get_mavlink_logger(sys_id)
        log.warning(msg)

    @staticmethod
    def mavlink_error(sys_id, msg):
        log = Loggers.get_mavlink_logger(sys_id)
        log.error(msg)

    @staticmethod
    def mavlink_critical(sys_id, msg):
        log = Loggers.get_mavlink_logger(sys_id)
        log.critical(msg)

    ## SIM VEHICLE LOG 
    @staticmethod
    def sim_vehicle_info(sys_id, msg):
        log = Loggers.get_sim_vehicle_logger(sys_id)
        log.info(msg)

    @staticmethod
    def sim_vehicle_debug(sys_id, msg):
        log = Loggers.get_sim_vehicle_logger(sys_id)
        log.debug(msg)

    @staticmethod
    def sim_vehicle_warning(sys_id, msg):
        log = Loggers.get_sim_vehicle_logger(sys_id)
        log.warning(msg)

    @staticmethod
    def sim_vehicle_error(sys_id, msg):
        log = Loggers.get_sim_vehicle_logger(sys_id)
        log.error(msg)

    @staticmethod
    def sim_vehicle_critical(sys_id, msg):
        log = Loggers.get_sim_vehicle_logger(sys_id)
        log.critical(msg)

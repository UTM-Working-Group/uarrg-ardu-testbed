from Scenario import Scenario
from Uas import Uas

def main():
    # Static flight Plans
    # 0 - 25 m/s
    # 0 - 359
    # MTOW - 0kg - 300kg
    scenario = Scenario("0", "High Wind", [
       Uas(0, None),
       ])
    scenario.run()

    # Static flight Plans
    scenario = Scenario("1", "One Conflict", [
       Uas(0, None),
       ])
    scenario.run()

if __name__=='__main__':
    main()

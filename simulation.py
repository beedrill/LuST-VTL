import os, sys
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")
import traci

sumoBinary = "sumo-gui"
sumoCmd = [sumoBinary, "-c", "LuSTScenario/scenario/due.static.sumocfg"]
traci.start(sumoCmd)


while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()


traci.close()

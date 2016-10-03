

class Troop(object):
    "A specific troop of a specific level"

    def __init__(self,troopCfg,level):
        self.__name = troopCfg.name
        self.__type = troopCfg.type   #elixir or dark elixir
        self.__buildTime = troopCfg.buildTime  #in seconds
        self.__space = troopCfg.space
        self.__cost = troopCfg.cost[level]
        self.__troopCfg = troopCfg

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @property
    def buildTime(self):
        return self.__buildTime

    @property
    def space(self):
        return self.__space

    @property
    def level(self):
        return self.__level

    @property
    def cost(self):
        return self.__cost


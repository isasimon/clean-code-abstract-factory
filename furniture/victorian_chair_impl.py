from furniture.chair import Chair


class VictorianChairImpl(Chair):
    @staticmethod
    def hasLegs():
        return True

    @staticmethod
    def sitOn():
        return True

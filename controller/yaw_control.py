from pid import PID

class YawController(PID):

    def __init__(self):
        PID.__init__(self, p=0, i=0, d=1.0, derivator=0, integrator=0, integrator_max=500, integrator_min=-500)

    def update(self, current_value):
        super(PID, self).update(current_value)
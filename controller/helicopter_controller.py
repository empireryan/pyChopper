from control_outputs.arduino_out import Serial
#from controller import pitch_control, roll_control, yaw_control, thrust_control
from optitrack_feedback import motive_client as optitrack
from pid import PID
from collections import namedtuple

Reference = namedtuple("Reference", 'x y z yaw', verbose=False, rename=False)
Configurator = namedtuple("Configurator", 'p i d set', verbose=False, rename=False)
PidOutputs = namedtuple("PidOutputs", 'roll pitch yaw thrust')

class PitchController(PID):

    def __init__(self, gains):
        PID.__init__(self, gains, derivator=0, integrator=0, integrator_max=500, integrator_min=-500)

    def update(self, current_value):
        super(PID, self).update(current_value)


class RollController(PID):

    def __init__(self, gains):
        PID.__init__(self, gains, derivator=0, integrator=0, integrator_max=500, integrator_min=-500)

    def update(self, current_value):
        super(PID, self).update(current_value)


class YawController(PID):

    def __init__(self, gains):
        PID.__init__(self, gains, derivator=0, integrator=0, integrator_max=500, integrator_min=-500)

    def update(self, current_value):
        super(PID, self).update(current_value)


class ThrustController(PID):

    def __init__(self, gains):
        PID.__init__(self, gains, derivator=0, integrator=0, integrator_max=500, integrator_min=-500)

    def update(self, current_value):
        #super(PID, self).update(current_value)
        self.PID.update(current_value)

class HelicopterController(object):

    def __init__(self, ref, pitch_gains, roll_gains, yaw_gains, thrust_gains):

        self.reference = ref
        self.pitch_controller = PitchController(pitch_gains)
        self.roll_controller = RollController(roll_gains)
        self.yaw_controller = YawController(yaw_gains)
        self.thrust_controller = ThrustController(thrust_gains)
        self.controllers = [self.pitch_controller, self.roll_controller, self.yaw_controller, self.thrust_controller]

    def update_controllers(self):
        #results = [pid.update(state) for pid in self.controllers]
        pass


reference = Reference(x=0, y=1, z=0, yaw=0)
pitch_gains = Configurator(p=0, i=0, d=0, set=0)
roll_gains = Configurator(p=0, i=0, d=0, set=0)
yaw_gains = Configurator(p=0, i=0, d=0, set=0)
thrust_gains = Configurator(p=0, i=0, d=0, set=0)

# Instantiate a PID controlled helicopter object
chopper = HelicopterController(reference, pitch_gains, roll_gains, yaw_gains, thrust_gains)
# configure controllers
print chopper.thrust_controller.set_point

# Initialize Serial object
Serial(115200)


# run control loop
while 1:

    # get state
    state = optitrack.recv_data()
    # run PID
    pid_outputs = chopper.update_controllers(state)
    # update outputs with results of PIDs, where 'pid_outputs' is an array containing
    # the results of all four PIDs for the chopper. Will likely need to mess with the order
    Serial.output(pid_outputs)
    pass



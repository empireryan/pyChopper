"""

"""
class PID(object):
    """
    Discrete PID control
    """

    def __init__(self, gains, derivator=0, integrator=0, integrator_max=500, integrator_min=-500):

        self.Kp = gains.p
        self.Ki = gains.i
        self.Kd = gains.d
        self.Derivator = derivator
        self.Integrator = integrator
        self.Integrator_max = integrator_max
        self.Integrator_min = integrator_min

        self.P_value = 0
        self.I_value = 0
        self.D_value = 0

        self.Derivator = 0
        self.Integrator = 0

        self.set_point = gains.set
        self.error = 0.0

    def update(self, current_value):
        """
        Calculate PID output value for given reference input and feedback
        :param current_value:
        """

        self.error = self.set_point - current_value
        self.P_value = self.Kp * self.error
        self.D_value = self.Kd * (self.error - self.Derivator)
        self.Derivator = self.error

        self.Integrator += self.error

        # @todo: can probably use the property setters/getters to implement this saturation
        if self.Integrator > self.Integrator_max:
            self.Integrator = self.Integrator_max
        elif self.Integrator < self.Integrator_min:
            self.Integrator = self.Integrator_min

        self.I_value = self.Integrator * self.Ki

        pid = self.P_value + self.I_value + self.D_value

        return pid

    def set_point(self, set_point):
        """
        Initilize the setpoint of PID
        :param set_point:
        """
        self.set_point = set_point
        self.Integrator = 0
        self.Derivator = 0

    def set_integrator(self, Integrator):
        """

        :param Integrator:
        """
        self.Integrator = Integrator

    def set_derivator(self, Derivator):
        """

        :param Derivator:
        """
        self.Derivator = Derivator

    def set_kp(self, P):
        """

        :param P:
        """
        self.Kp = P

    def set_ki(self, I):
        """

        :param I:
        """
        self.Ki = I

    def set_kd(self, D):
        """

        :param D:
        """
        self.Kd = D

    @property
    def get_point(self):
        return self.set_point

    @property
    def get_error(self):
        return self.error

    @property
    def get_integrator(self):
        return self.Integrator

    @property
    def get_derivator(self):
        return self.Derivator

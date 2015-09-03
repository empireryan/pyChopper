# noinspection PyAttributeOutsideInit
class PID(object):
    """
    Discrete PID control
    """

    def __init__(self, gains=0, derivator=0, integrator=0, integrator_max=500, 
                 integrator_min=-500, set_point_max=1, set_point_min=-1):

        self.Kp = 0
        self.Ki = 0
        self.Kd = 0
        self.integrator_max = integrator_max
        self.integrator_min = integrator_min        
        self.derivator = derivator
        self.integrator = integrator
        self.P_value = 0
        self.I_value = 0
        self.D_value = 0
        self.set_point_max = set_point_max
        self.set_point_min = set_point_min
        self.set_point = 0
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

        self.I_value = self.Integrator * self.Ki

        pid = self.P_value + self.I_value + self.D_value

        return pid

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
    def set_point(self):
        return self._set_point

    @set_point.setter
    def set_point(self, set_point):
        """
        Initilize the setpoint of PID
        :param set_point:
        """
        if set_point > self.set_point_max:
            self._set_point = self.set_point_max
        elif set_point < self.set_point_min:
            self._set_point = self.set_point_min
        else:
            self._set_point = set_point
        self.Integrator = 0
        self.Derivator = 0

    @property
    def integrator(self):
        return self._integrator

    @integrator.setter
    def integrator(self, integrator):
        """

        :param Integrator:
        """
        if integrator > self.integrator_max:
            self._integrator = self.integrator_max
        elif integrator < self.integrator_min:
            self._integrator = self.integrator_min
        else:
            self._integrator = integrator

            
    @property
    def derivator(self):
        return self._derivator

    @derivator.setter
    def derivator(self, derivator):
        """

        :param Derivator:
        """
        self._derivator = derivator



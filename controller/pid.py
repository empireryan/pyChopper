# noinspection PyAttributeOutsideInit
class PID(object):
    """
    Discrete PID control
    """

    def __init__(self, gains=0, set_point_max=1, set_point_min=-1, saturate_max = None, saturate_min = None):

        self.Kp = 0
        self.Ki = 0
        self.Kd = 0
        self._Ti = self.Kp / self.Ki
        self._Td = self.Kd / self.Kp

        self.set_point_max = set_point_max
        self.set_point_min = set_point_min
        self.set_point = 0
        self.saturate_max = saturate_max
        self.saturate_min = saturate_min

        self.ut = 0.0
        self.ut_1 = 0.0
        self.et = 0.0
        self.et_1 = 0.0
        self.et_2 = 0.0

    def update(self, feedback):
        """
        Calculate PID output value for given reference input and feedback
        :param feedback: state of the plant
        """
        self.et = self.set_point - feedback
        self.ut = self.ut_1 + self.Kp * (
            (1 + self.dt / self._Ti + self._Td / self.dt) * self.et - (1 + 2 * self._Td / self.dt) * self.et_1
            + (self._Td * self.et_2) / self.dt)

        self.et_2 = self.et_1
        self.et_1 = self.et
        self.ut_1 = self.ut

        return self.ut

    @property
    def Kp(self, Kp):
        return self._Kp

    @Kp.setter
    def Kp(self, p):
        """

        :param P:
        """
        self._Kp = p
        self._Ti = self._Kp / self.Ki
        self._Td = self.Kd / self._Kp

    @property
    def Ki(self, i):
        return self._Ki


    @Ki.setter
    def Ki(self, i):
        self._Ki = i
        self._Ti = self.Kp / self._Ki
        self._Td = self.Kd / self.Kp

    @property
    def Kd(self, d):
        self._Kd = d
        self._Ti = self.Kp / self.Ki
        self._Td = self._Kd / self.Kp

    @property
    def set_point(self):
        return self._set_point

    @set_point.setter
    def set_point(self, set_point):
        if set_point > self.set_point_max:
            self._set_point = self.set_point_max
        elif set_point < self.set_point_min:
            self._set_point = self.set_point_min
        else:
            self._set_point = set_point

        # @todo: ask the professor about this
        self.ut = 0
        self.ut_1 = 0

    @property
    def ut(self):
        return self._ut

    @ut.setter
    def ut(self, ut):
        self._ut = ut

        if self.saturate_max or self.saturate_min:
            if self.saturate_max and ut > self.saturate_max:
                self._ut = self.saturate_max
            elif self.saturate_min and ut < self.saturate_min:
                self._ut = self.saturate_min

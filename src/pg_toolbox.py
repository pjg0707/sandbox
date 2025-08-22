import math
from numerize import numerize


class Toolbox:
    # def __init__(self):
    #    self.x = 1

    def f0_RC(self, R, C, string_needed=0, digits=2):
        freq = 1 / (2 * math.pi * R * C)
        if string_needed == 0:
            return freq
        return numerize.numerize(freq, digits) + "Hz"

    def f0_LC(self, L, C, string_needed=0, digits=2):
        freq = 1 / (2 * math.pi * math.sqrt(L * C))
        if string_needed == 0:
            return freq
        return numerize.numerize(freq, digits) + "Hz"

    def f0_LR(self, L, R, string_needed=0, digits=2):
        freq = R / (2 * math.pi * L)
        if string_needed == 0:
            return freq
        return numerize.numerize(freq, digits) + "Hz"

    def RPar(self, R1, R2):
        return R1 * R2 / (R1 + R2)

    def RAntiPar(self, RT, R1):
        return RT * R1 / (R1 - RT)


#########################################################
#                      Testbench                        #
#########################################################
Pablo = Toolbox()
print(str(round(Pablo.f0_LC(1e-9, 100e-9) / 1e6, 2)) + " MHz")
print(str(round(Pablo.f0_RC(10e3, 10e-9) / 1e3, 2)) + " kHz")
print(str(round(Pablo.f0_LR(10e-6, 1e3) / 1e6, 2)) + " MHz")

print(Pablo.f0_LC(1e-9, 100e-9, 1))
print(Pablo.f0_RC(10e3, 10e-9, 1))
print(Pablo.f0_LR(10e-6, 1e3, 1))

print(Pablo.RPar(1e3, 1e3))
print(Pablo.RAntiPar(500, 1e3))

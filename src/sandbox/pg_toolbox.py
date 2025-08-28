import numpy as np


def humanize_number(value, digits=2):
    """Format a number with SI prefixes (k, M, G, etc.)."""
    prefixes = [
        (1e9, "G"),
        (1e6, "M"),
        (1e3, "k"),
        (1, ""),
        (1e-3, "m"),
        (1e-6, "μ"),
        (1e-9, "n"),
        (1e-12, "p"),
    ]
    for factor, suffix in prefixes:
        if abs(value) >= factor:
            return f"{round(value / factor, digits)}{suffix}"
    return f"{round(value, digits)}"


class Toolbox:
    # def __init__(self):
    #    self.x = 1

    def f0_RC(self, R, C, string_needed=0, digits=2):
        freq = 1 / (2 * np.pi * R * C)
        if string_needed == 0:
            return freq
        return humanize_number(freq, digits) + "Hz"

    def f0_LC(self, L, C, string_needed=0, digits=2):
        freq = 1 / (2 * np.pi * np.sqrt(L * C))
        if string_needed == 0:
            return freq
        return humanize_number(freq, digits) + "Hz"

    def f0_LR(self, L, R, string_needed=0, digits=2):
        freq = R / (2 * np.pi * L)
        if string_needed == 0:
            return freq
        return humanize_number(freq, digits) + "Hz"

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

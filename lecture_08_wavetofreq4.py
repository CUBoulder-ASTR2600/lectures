#!/usr/bin/env python

import sys

try:
    wave = float(sys.argv[1])

except IndexError:
    print('Enter the wavelength in Angstroms on the command line.')
    sys.exit(1)

except ValueError as error:
    # print('The wavelength must be a number not {}'.format(type(sys.argv[1]))
    print("The error is:", error)
    sys.exit(2)

freq = 3.0e8 / (wave / 1e10)
print('frequency (Hz) = %e' % freq)

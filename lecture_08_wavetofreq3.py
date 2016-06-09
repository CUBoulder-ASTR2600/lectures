#!/usr/bin/env python

import sys

try:
    wave = float(sys.argv[1])
except:
    print('Enter the wavelength in Angstroms on the command line.')
    sys.exit(1)  # 1 indicates failure
    # sys.exit() is used to indicate success

freq = 3.0e8 / (wave / 1e10)
print('frequency (Hz) = %e' % freq)

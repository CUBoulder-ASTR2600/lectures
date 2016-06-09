#!/usr/bin/env python

import sys

if len(sys.argv) < 2:
    print('Enter the wavelength in meters on the command line.')
    sys.exit(1)  # 1 indicates failure
    # sys.exit() is used to indicate success

wave = float(sys.argv[1])
freq = 3.0e8 / (wave / 1e10)
print('frequency (Hz) = %e' % freq)

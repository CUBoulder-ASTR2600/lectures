#!/usr/bin/env python

import sys
wave = float(sys.argv[1])
freq = 3.0e8 / (wave / 1e10)
print('frequency (Hz) = %e' % freq)

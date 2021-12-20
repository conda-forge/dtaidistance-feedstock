from dtaidistance.dtw import dtw_cc
from dtaidistance.dtw import dtw_cc_numpy
from dtaidistance.dtw import dtw_cc_omp

if dtw_cc is None:
    raise ImportError('Importing dtw_cc returned None.')
if dtw_cc_numpy is None:
    raise ImportError('Importing dtw_cc_numpy returned None.')
if dtw_cc_omp is None:
    raise ImportError('Importing dtw_cc_omp returned None.')

########################################################################
# Author(s):    Ashwin Kanhere
# Date:         21 September 2021
# Desc:         Simulate GNSS measurements for previously saved trajectories
########################################################################
import sys, os, csv
parent_directory = os.path.split(os.getcwd())[0]
#TODO: Scrub paths
src_directory = os.path.join(parent_directory, 'src')
data_directory = os.path.join('/scratch/groups/gracegao', 'Google_GNSS_data')
ephemeris_data_directory = os.path.join(data_directory, 'ephemeris')
sys.path.insert(0, src_directory)
import numpy as np
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import pytz
from datetime import datetime

# Imports from local packages: gnss_lib
from gnss_lib.coordinates import geodetic2ecef
from totalrecall.simulator_utils import save_simulated_dataset

path_root = '/scratch/groups/gracegao/Google_GNSS_data'
# Execute the functions above to generate the data
start_time = datetime(2020, 5, 15, 0, 47, 15, 448796, pytz.UTC)
x_LLA = np.reshape([37.427112, -122.1764146, 16], [1, 3])
start_ECEF = np.reshape(geodetic2ecef(x_LLA), [3, 1])
steps = 1000


savepath = path_root + '/simulated_nonoise/gnss_measurements/'

traject_func = "traject_gen_zigzag"

_ = save_simulated_dataset(traject_func, steps, start_time, start_ECEF, ephemeris_data_directory, save=True, savepath=savepath, noise=True)
_ = save_simulated_dataset(traject_func, steps, start_time, start_ECEF, ephemeris_data_directory, save=True, savepath=savepath, noise=False)

traject_func = 'MATLAB_saved'
# loadpath = os.path.join(path_root, '/matlab_trajectories/')
loadpath = path_root + '/matlab_trajectories/'
for idx in range(10):
    print('Processing trajectory ', str(idx))
    savepath = path_root + '/matlab_simulated_nonoise/gnss_measurements/'
    _ = save_simulated_dataset(traject_func, None, start_time, start_ECEF, ephemeris_data_directory, traject_idx=idx, save=True, savepath=savepath, loadpath=loadpath, noise=False)
    savepath = path_root + '/matlab_simulated/gnss_measurements/'
    _ = save_simulated_dataset(traject_func, None, start_time, start_ECEF, ephemeris_data_directory, traject_idx=idx, save=True, savepath=savepath, loadpath=loadpath, noise=True)

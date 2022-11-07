import os
import numpy as np
from os import listdir
from os.path import join, isfile
from flirextractor import FlirExtractor

def imageconvert(load_path: str, save_path: str):
    for date in os.listdir(load_path):
        for view in ['view_1', 'view_2', 'view_3']:
            load_path_view = os.path.join(load_path, date, view)
            save_path_view = os.path.join(save_path, date, view)
            
            # Check if the save path exist
            if not os.path.isdir(save_path_view):
                os.makedirs(save_path_view)
            
            # Convert files
            files = [f for f in listdir(load_path_view) if isfile(join(load_path_view, f))]
            for i in files:
                with FlirExtractor() as extractor:
                    thermal_data = extractor.get_thermal(f'{load_path_view}/{i}')
                    np.savetxt(f'{save_path_view}/{i[:-5]}.csv', thermal_data, delimiter=',')


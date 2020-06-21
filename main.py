import numpy as np
import pygrib
import glob

def main():
    
    #read grib files

    u_value_lists, u_level_lists, u_date_lists, u_latlon_lists = get_grib_data(
        "./OCN_GPV_Rnwpa_Gll0p1deg/","*cur*FD01*","U-component of current"
    )
    v_value_lists, v_level_lists, v_date_lists, v_latlon_lists = get_grib_data(
        "./OCN_GPV_Rnwpa_Gll0p1deg/","*cur*FD01*","V-component of current"
    )
    temp_value_lists, temp_level_lists, temp_date_lists, temp_latlon_lists = get_grib_data(
        "./OCN_GPV_Rnwpa_Gll0p1deg/","*sbs*FD01*",None
    )
    salt_value_lists, salt_level_lists, salt_date_lists, salt_latlon_lists = get_grib_data(
        "./OCN_GPV_Rnwpa_Gll0p1deg/","*sal*FD01*",None
    )
    zeta_value_lists, zeta_level_lists, zeta_date_lists, zeta_latlon_lists = get_grib_data(
        "./OCN_GPV_Rnwpa_Gll0p1deg/","*ssh*FD01*",None
    )
    
    #Conversion : [K] -> [deg]

    #write netcdf

    
    return

def get_grib_data(parent_dir, string_filter, param_name):
    #param name list
    grb_file_list = glob.glob(parent_dir + string_filter)
    grb_file_list = list(sorted(grb_file_list))

    level_lists = []
    value_lists = []
    date_lists = []
    latlon_lists = []

    for grb_file in grb_file_list:
        level_lists.append(get_level_list(grb_file, param_name))
        value_lists.append(get_value_list(grb_file, param_name))
        date_lists.append(get_date_list(grb_file, param_name))
        latlon_lists.append(get_latlon_list(grb_file, param_name))

    return value_lists, level_lists, date_lists, latlon_lists

def get_level_list(file_name, param_name):
    grbs = pygrib.open(file_name)
    if param_name is not None:
        z_data_list = [grb.level for grb in grbs if grb.name == param_name]
    else:
        z_data_list = [grb.level for grb in grbs]
    return z_data_list

def get_date_list(file_name, param_name):
    grbs = pygrib.open(file_name)
    if param_name is not None:
        date_list = [grb.validDate for grb in grbs if grb.name == param_name]
    else:
        date_list = [grb.validDate for grb in grbs]
    return date_list
    
def get_value_list(file_name, param_name):
    grbs = pygrib.open(file_name)
    if param_name is not None:
        value_list = [grb.values for grb in grbs if grb.name == param_name]
    else:
        value_list = [grb.values for grb in grbs]
    return value_list

def get_latlon_list(file_name, param_name):
    grbs = pygrib.open(file_name)
    if param_name is not None:
        latlon_list = [grb.latlons() for grb in grbs if grb.name == param_name]
    else:
        latlon_list = [grb.latlons() for grb in grbs]
    return latlon_list

def lists_to_list(something_lists):
    for something_list in something_lists:
        if something_list != something_lists[0]:
            print("Warning!")
            return None

    return something_lists[0]

if __name__ == "__main__":
    main()
    pass
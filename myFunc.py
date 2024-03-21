#-------------------------------------------------------#
# Author      : Jonathan Amez-Droz
# Date        : 2020-04-20
# Description : Usefull functions for different usages
#--------------------------------------------------------#

#Import libraries
import json
import pandas as pd
import socket


#--------------------------Simple functions------------------------------#
#                                                                        #
#------------------------------------------------------------------------#
#Add two numbers
def add(a,b) :
    return a+b

#Function to substract to numbers
def substract(a,b) :
    return a-b

#--------------------------datetime functions----------------------------#
#                                                                        #
#------------------------------------------------------------------------#
def dt_to_ts(df, offset) :
    '''
    Convert a datetime dataframe to a timestamp dataframe
    Input : df, dataframe
          : offset, offset to add to the timestamp
    Output : df, dataframe with the timestamp
    '''
    df['ts'] = df.apply(lambda x: (x[0]).timestamp(), axis=1) + offset

    return df


#--------------------------UDP functions---------------------------------#
#                                                                        #
#------------------------------------------------------------------------#






#--------------------------JSON functions--------------------------------#
#                                                                        #
#------------------------------------------------------------------------#
#Convert a json to ascii
def json_to_ascii(json_data):
    """
    Convert json set of json data to ascii
    Input : json_data 
    Output : json_ascii 
    """
    json_data = json.dumps(json_data)
    json_ascii = json_data.encode('ascii','replace')
    return json_ascii

#Create a log file from a json_data line by line
def create_log_file_line(json_data, k, filename):
    """
    Create a log file with the json data
    Input : json_data
          : k, loop indey
          : filename, name of the file

    Output : log file
    """
    #Create a dataframe from the json data
    df = pd.DataFrame(json_data, index=[0])
    #Create a log file
    if k == 0:
        #On the fisrt loop, create the file with the header
        df.to_csv(filename, mode='a', header=True, index=False)
    else:
        df.to_csv(filename, mode='a', header=False, index=False)

#Create a log file from a json_data
def create_log_file(json_data, filename):
    """
    Create a log file with the json data
    Input : json_data
          : filename, name of the file

    Output : log file
    """
    #Create a dataframe from the json data
    df = pd.DataFrame(json_data, index=[0])
    #Create a log file
    df.to_csv(filename, mode='a', header=False, index=False)
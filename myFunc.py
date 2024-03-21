#-------------------------------------------------------#
# Author      : Jonathan Amez-Droz
# Date        : 2020-04-20
# Description : Usefull functions for different usages
#--------------------------------------------------------#

#Import libraries
import json
import pandas as pd
import socket
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np


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
def dt_to_ts(df, timestring='timestamp', offset=0) :
    '''
    Convert a datetime dataframe to a timestamp dataframe
    Input : df, dataframe
          : offset, offset to add to the timestamp
    Output : df, dataframe with the timestamp
    '''
    df['ts'] = df[[timestring]].apply(lambda x: (x[0]).timestamp(), axis=1).astype(int) + offset

    return df


#--------------------------UDP functions---------------------------------#
#                                                                        #
#------------------------------------------------------------------------#


#--------------------------Plot functions--------------------------------#
#                                                                        #
#------------------------------------------------------------------------#
def multiPlot(x, y, title="", xlabel="", ylabel="", time_format ='ts') :
    '''
    Plot n functions on the same plot

    '''
    if time_format == 'hms':
        x = pd.to_datetime(x, unit='s').dt.strftime('%H:%M:%S')

    fig, ax = plt.subplots(figsize=(10, 7))
    fig.suptitle(title)

    n = np.shape(y)[0]
    ax.set_xlabel(xlabel)
    ax.grid(True)
    ax.xaxis.set_tick_params(rotation=45)
    ax.xaxis.set_ticks(range(0, len(x), 100))

    for i in range(n):
        ax.plot(x, y[i])

    ax.legend(ylabel)

    
    plt.show()

def CursorPlot(x, y, title="", xlabel="", ylabel="", cursor = True) :
    '''
    Plot a function with an interactive cursor. This does
    not work with a datetime x-axis
    Input  : x, x values and labels

    Output : Display the plot
    '''

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)
    
    if cursor:
        # Define the range for the x-slider
        x_min = min(x)
        x_max = max(x)
        ax_slider_start = plt.axes([0.1, 0.03, 0.8, 0.03]) #[left, bottom, width, height]
        ax_slider_end = plt.axes([0.1, 0.01, 0.8, 0.03]) #[left, bottom, width, height]
        

        # Create the sliders
        slider_start = Slider(ax_slider_start, 'Start', x_min, x_max, valinit=x_min)
        slider_end = Slider(ax_slider_end, 'End', x_min, x_max, valinit=x_max)
        
        # Define function to update plot with new x-range
        def update(val):
            x_range_start = slider_start.val
            x_range_end = slider_end.val
            ax.set_xlim(x_range_start, x_range_end)
            plt.draw()
        
        # Connect the update function to the sliders
        slider_start.on_changed(update)
        slider_end.on_changed(update)

    plt.show()









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
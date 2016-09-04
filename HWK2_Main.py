# Python script for homework 2 in CSCI-720
# Otsu's Method of One-Dimensional Clustering
# written by Mark J. Petrie
#

#Let Python know we are going to use the function csv
#to read the excel input file
import csv
import plotly.plotly as py
import plotly.graph_objs as go

#using the csv function, read the cantelope_data.csv file
#into the file handle csv_dff
deflection_force_file = open('cantelope_data.csv')
csv_dff = csv.reader(deflection_force_file)

#for each row, calculate and store a stiffness
#coefficient

for row in csv_dff:
    force = float(row[0])
    deflection = float(row[1])
    stiffness_coefficent = deflection / force
    
#create a Histogram
#need to get the stiffness_coefficent stored  in a file
#to send to plotly
    data = [
        go.Histogram(
            x=stiffness_coefficent
        )
    ]
    py.iplot(data)
    

#set the attribute best_mixed_variance to infinite
#best_mixed_variance = float("infinite")

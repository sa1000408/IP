#!/usr/bin/python
#-*- coding:utf-8 -*-
#Calculate Statistics

import numpy as np
import arcpy

arcpy.env.overwriteOutput = True #Geoprocessing Outputs generell überschreiben

input = arcpy.env.workspace= arcpy.GetParameterAsText(0)

column1 = arcpy.GetParameterAsText(1)
column2 = arcpy.GetParameterAsText(2)
column3 = arcpy.GetParameterAsText(3)

arrayTable = arcpy.da.FeatureClassToNumPyArray(input,(column1))

max = (np.max((arrayTable[column1])))
mean = (np.mean((arrayTable[column1])))
min = (np.min((arrayTable[column1])))
std = (np.std((arrayTable[column1])))
records = (len((arrayTable[column1])))

arcpy.AddMessage("Number of in Feature" + str(records))

arcpy.AddMessage("Maximum of: " + str(column1)+str(max))
arcpy.AddMessage("Mean of: " + str(column1)+str(mean))
arcpy.AddMessage("Minimum of: " + str(column1)+str(min))
arcpy.AddMessage("Standard deviation of: " + str(column1)+ str(std))

arrayTable = arcpy.da.FeatureClassToNumPyArray(input,(column2))

max = (np.max((arrayTable[column2])))
mean = (np.mean((arrayTable[column2])))
min = (np.min((arrayTable[column2])))
std = (np.std((arrayTable[column2])))
records = (len((arrayTable[column2])))


arcpy.AddMessage("Maximum of: " + str(column2)+str(max))
arcpy.AddMessage("Mean of: " + str(column2)+str(mean))
arcpy.AddMessage("Minimum of: " + str(column2)+str(min))
arcpy.AddMessage("Standard deviation of: " + str(column2)+ str(std))

arrayTable = arcpy.da.FeatureClassToNumPyArray(input,(column3))

max = (np.max((arrayTable[column3])))
mean = (np.mean((arrayTable[column3])))
min = (np.min((arrayTable[column3])))
std = (np.std((arrayTable[column3])))
records = (len((arrayTable[column3])))


arcpy.AddMessage("Maximum of: " + str(column3)+str(max))
arcpy.AddMessage("Mean of: " + str(column3)+str(mean))
arcpy.AddMessage("Minimum of: " + str(column3)+str(min))
arcpy.AddMessage("Standard deviation of: " + str(column3)+ str(std))



#Als t


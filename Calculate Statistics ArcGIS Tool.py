#!/usr/bin/python
#-*- coding:utf-8 -*-
#Calculate Statistics
import math
import numpy as np
import arcpy

arcpy.env.overwriteOutput = True #Geoprocessing Outputs generell überschreiben

input = arcpy.env.workspace= arcpy.GetParameterAsText(0)

column0 = arcpy.GetParameterAsText(1)

arrayTable = arcpy.da.FeatureClassToNumPyArray(input,(column0))

max = (np.max((arrayTable[column0])))
mean = (np.mean((arrayTable[column0])))
min = (np.min((arrayTable[column0])))
std = (np.std((arrayTable[column0])))
records = (len((arrayTable[column0])))

arcpy.AddMessage("Maximum of" + column0+max)
arcpy.AddMessage("Mean of" + column0+mean)
arcpy.AddMessage("Minimum of" + column0+min)
arcpy.AddMessage("Standard deviation of" + column0+ std)
arcpy.AddMessage("Number of in Feature" + records)

#!/usr/bin/python
#-*- coding:utf-8 -*-

import arcpy
arcpy.env.overwriteOutput = True #Geoprocessing Outputs generell überschreiben

input = arcpy.env.workspace= arcpy.GetParameterAsText(0)



Expression = arcpy.GetParameterAsText(1)

output = arcpy.env.workspace= arcpy.GetParameterAsText(2)
arcpy.SelectLayerByAttribute_management(input, "NEW_SELECTION", Expression)

# Write the selected features to a new featureclass
arcpy.CopyFeatures_management(input, output)
arcpy.SelectLayerByAttribute_management(input,"CLEAR_SELECTION")
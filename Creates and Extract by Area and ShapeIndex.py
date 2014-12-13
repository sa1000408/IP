#!/usr/bin/python
#-*- coding:utf-8 -*-

import arcpy

arcpy.env.overwriteOutput = True #Geoprocessing Outputs generell überschreiben

# Add fields to attributetable
arcpy.AddField_management(input, "Ai", "double", "", "", "", "", "NULLABLE", "")
arcpy.AddField_management(input, "Li", "double", "", "", "", "", "NULLABLE", "")
arcpy.AddField_management(input, "Bi", "double", "", "", "", "", "NULLABLE", "")
arcpy.AddField_management(input, "ShapeIndex", "double", "", "", "", "", "NULLABLE", "")

#Calculate fields as Area, LEngth, ShapeIndex
arcpy.CalculateField_management(input, "Ai", "!shape.area!", "PYTHON")
arcpy.CalculateField_management(input, "Li", "!shape.length!", "PYTHON")
arcpy.CalculateField_management(input,"Bi", " (([Li]^2)/(4*3.14159265359))")
arcpy.CalculateField_management(input,"ShapeIndex", "Sqr ( [Ai]/[Bi])")

Expression = arcpy.GetParameterAsText(1)

output = arcpy.env.workspace= arcpy.GetParameterAsText(2)
arcpy.SelectLayerByAttribute_management(input, "NEW_SELECTION", Expression)

# Write the selected features to a new featureclass
arcpy.CopyFeatures_management(input, output)
arcpy.SelectLayerByAttribute_management(input,"CLEAR_SELECTION")
#!/usr/bin/python
#-*- coding:utf-8 -*-

# Adds the following fields to the Table: Area, ShapeLength, ShapeIndex
# http://www.spatialanalysisonline.com/HTML/?shape.htm
# Ai as the Area of polygon i, and Li as its perimeter length, and Bi as the area of a circle with perimeter Li, then example measures include:
# Shape index = sqr (Ai/Bi)
import arcpy
arcpy.env.overwriteOutput = True #Geoprocessing Outputs generell überschreiben

input = arcpy.env.workspace= arcpy.GetParameterAsText(0)

# Make a layer from the feature class
arcpy.MakeFeatureLayer_management(input, "lyr")

# Add fields to attributetable
arcpy.AddField_management("lyr", "Ai", "double", "", "", "", "", "NULLABLE", "")
arcpy.AddField_management("lyr", "Li", "double", "", "", "", "", "NULLABLE", "")
arcpy.AddField_management("lyr", "Bi", "double", "", "", "", "", "NULLABLE", "")
arcpy.AddField_management("lyr", "ShapeIndex", "double", "", "", "", "", "NULLABLE", "")

#Calculate fields as Area, LEngth, ShapeIndex
arcpy.CalculateField_management("lyr", "Ai", "!shape.area!", "PYTHON")
arcpy.CalculateField_management("lyr", "Li", "!shape.length!", "PYTHON")
arcpy.CalculateField_management("lyr","Bi", " (([Li]^2)/(4*3.14159265359))")
arcpy.CalculateField_management("lyr","ShapeIndex", "Sqr ( [Ai]/[Bi])")

# Write the selected features to a new featureclass
arcpy.CopyFeatures_management("lyr", input)
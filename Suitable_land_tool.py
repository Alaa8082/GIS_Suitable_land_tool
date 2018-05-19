# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Suitable_land_tool.py
# Created on: 2018-04-20 18:24:50.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: Suitable_land_tool <Boundaries> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
True=arcpy.env.overwriteOutput
# Script arguments
Boundaries = arcpy.GetParameterAsText(0)
if Boundaries == '#' or not Boundaries:
    Boundaries = "D:\\WCGIS\\Geog485\\Lesson1\\Lesson1\\us_boundaries.shp" # provide a default value if unspecified

# Local variables:
Cities = "us_cities"
Roads = "D:\\WCGIS\\Geog485\\Lesson1\\Lesson1\\us_roads.shp"
Suitable_land = Boundaries
Distance__value_or_field_ = "10 Miles"
Distance__value_or_field___2_ = "10 Miles"
Buffered_cities = "C:\\Users\\Alaa\\Documents\\ArcGIS\\Default.gdb\\us_cities_Buffer1"
Bufferwd_Roads = "C:\\Users\\Alaa\\Documents\\ArcGIS\\Default.gdb\\us_roads_Buffer1"
Intersected_buffers = "C:\\Users\\Alaa\\Documents\\ArcGIS\\Default.gdb\\us_cities_Buffer_Intersect"

# Process: Buffer the cities
arcpy.Buffer_analysis(Cities, Buffered_cities, Distance__value_or_field_, "FULL", "ROUND", "ALL", "", "PLANAR")

# Process: Buffer The Roads
arcpy.Buffer_analysis(Roads, Bufferwd_Roads, Distance__value_or_field___2_, "FULL", "ROUND", "ALL", "", "PLANAR")

# Process: Intersect
arcpy.Intersect_analysis("C:\\Users\\Alaa\\Documents\\ArcGIS\\Default.gdb\\us_cities_Buffer1 #;C:\\Users\\Alaa\\Documents\\ArcGIS\\Default.gdb\\us_roads_Buffer1 #", Intersected_buffers, "ALL", "", "INPUT")

# Process: Clip
arcpy.Clip_analysis(Intersected_buffers, Boundaries, Suitable_land, "")


#Creating the gdb and the garage features
import arcpy

arcpy.env.workspace = r"C:\Users\enriquevalero\OneDrive - Texas A&M University\Documents\GEOG_676(ONLINE)\repo\valero-online-GEOG676-spring2025\Lab_4\codes_env"
folder_path = r"C:\Users\enriquevalero\OneDrive - Texas A&M University\Documents\GEOG_676(ONLINE)\repo\valero-online-GEOG676-spring2025\Lab_4"
gdb_name = "New.gdb"
gdb_path = folder_path + "\\" + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

csv_path = r"C:\Users\enriquevalero\OneDrive - Texas A&M University\Documents\GEOG_676(ONLINE)\repo\valero-online-GEOG676-spring2025\Lab_4\garages.csv"
garage_layer_name = "Garage_Points"
garages = arcpy.MakeXYEventLayer_management(csv_path, "X", "Y", garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + "\\" + garage_layer_name

#Open the Campus gdb and copying the building feature to the created gdb
campus = r"C:\Users\enriquevalero\OneDrive - Texas A&M University\Documents\GEOG_676(ONLINE)\repo\valero-online-GEOG676-spring2025\Lab_4\Campus.gdb"
buildings_campus = campus + "\\Structures"
buildings = gdb_path + "\\" + "Buildings"

arcpy.Copy_management(buildings_campus, buildings)

#Reprojecting the points
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + "\\Garage_Points_ReProject", spatial_ref)

#Creating the buffer for garages
garageBuffered = arcpy.Buffer_analysis(gdb_path + "\\Garage_Points_ReProject", gdb_path + "\\Garage_Buffered", 150)

#Intersect buffer with buildings
arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + "\\Garage_Building_Intersection", "ALL")

arcpy.TableToTable_conversion(gdb_path + "\\Garage_Building_Intersection.dbf", r"C:\\Users\\enriquevalero\\OneDrive - Texas A&M University\\Documents\\GEOG_676(ONLINE)\\repo\\valero-online-GEOG676-spring2025\\Lab_4", "nearby_buildings.csv")

print("Process completed")
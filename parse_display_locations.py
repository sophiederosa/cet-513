import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as cx

# Read in the data
path = "data/vehicle_locations.shp"
gdf = gpd.read_file(path)

# Assign the CRS
gdf = gdf.set_crs(epsg=4326)

# Reproject to UTM 10N (meters)
gdf_proj = gdf.to_crs(epsg=32610)

# Basemap + data
ax = gdf_proj.plot(figsize=(10, 12), markersize=6, color="#d62839",
                   alpha=0.6, linewidth=0)

cx.add_basemap(ax, crs=gdf_proj.crs, source=cx.providers.Esri.WorldGrayCanvas)
ax.set_axis_off()
plt.tight_layout()
plt.savefig("outputs/vehicle_map.png", dpi=300, bbox_inches="tight")
plt.show()
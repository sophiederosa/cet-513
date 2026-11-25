# README
# test change
# How to setup
```python
pip install geopandas
pip install matplotlib
pip install contextily
```
# How to run

```python
python parse_display_locations.py
```

This will run the script, read in the shapefile data and display the locations on a basemap of Seattle. The map will be saved to outputs/vehicle_map.png. Avoid checking this in (it is added to the .gitignore so it shouldn't be added)

# How to make and push changes

Once your code change is done, create a new branch:

```
git checkout -b <yourname>/<description of changes>
```
for example:
```
git checkout -b sophiederosa/update-parser
```

Then add your changes to the branch:
```
git add --all
```

Then push:

```
git commit -m "Description of your changes"
git push
```

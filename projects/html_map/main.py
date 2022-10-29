import folium

# Create a map object
map = folium.Map(location=[53.383331, -1.466667], zoom_start=10, tiles="Stamen Terrain")    
# Save the map
map.save("./projects/html_map/Map1.html")

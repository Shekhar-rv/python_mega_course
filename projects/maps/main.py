import folium
import pandas as pd

# Read the volcano data as a pandas dataframe
data = pd.read_csv("./data/Volcanoes.txt")


def sheffield_map():
    # Create a map object
    map = folium.Map(
        location=[53.383331, -1.466667], zoom_start=10, tiles="Stamen Terrain"
    )

    # Add feature group and add marker
    fg = folium.FeatureGroup(name="My Map")

    # Create a location dictionary

    locations = [
        {
            "coordinates": [53.3785, -1.4663],
            "popup": "Sheffield Hallam University",
            "icon": folium.Icon(color="green"),
        },
        # coordinates for Sheffield univeristy
        {
            "coordinates": [53.3814, -1.4884],
            "popup": "Sheffield University",
            "icon": folium.Icon(color="red"),
        },
    ]

    for location in locations:
        fg.add_child(
            folium.Marker(
                location=location.get("coordinates"),
                popup=location.get("popup"),
                icon=location.get("icon", folium.Icon(color="blue")),
            )
        )
    map.add_child(fg)

    # Save the map
    map.save("sheffield_map.html")


# Function to return a color based on the value of the elevation.
def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


def volcano_map():

    # Create a HTML map object for string injection
    html = """
    <h4>Volcano information:</h4>
    Name: <a href="https://www.google.com/search?q=%s volcano" target="_blank">%s</a><br>
    Location: %s <br>
    Height: %s m <br>
    """

    # Create a map object
    map = folium.Map(
        location=[data["LAT"].mean(), data["LON"].mean()],
        zoom_start=4,
        tiles="OpenStreetMap",
    )

    # Add feature group and add marker
    fg_population = folium.FeatureGroup(name="Population Layer")

    # Add a population layer to the map using a GeoJson file
    fg_population.add_child(
        folium.GeoJson(
            data=open("./data/world.json", "r", encoding="utf-8-sig").read(),
            style_function=lambda x: {
                "fillColor": "green"
                if x["properties"]["POP2005"] < 10000000
                else "orange"
                if 10000000 <= x["properties"]["POP2005"] < 20000000
                else "red"
            },
        )
    )

    # Add feature group and add marker
    fg_volcano = folium.FeatureGroup(name="Volcano Layer")

    # Add a volcano layer to the map using the csv file
    for item in range(len(data)):
        iframe = folium.IFrame(
            html=html
            % (
                data["NAME"][item],
                data["NAME"][item],
                data["LOCATION"][item],
                str(data["ELEV"][item]),
            ),
            width=200,
            height=100,
        )
        # Add marker to the map
        # fg.add_child(
        #     folium.Marker(
        #         location=[data["LAT"][item], data["LON"][item]],
        #         popup=folium.Popup(iframe),
        #         icon=folium.Icon(color=color_producer(data["ELEV"][item])),
        #     )
        # ),
        fg_volcano.add_child(
            folium.CircleMarker(
                location=[data["LAT"][item], data["LON"][item]],
                radius=12,
                fill_opacity=0.7,
                popup=folium.Popup(iframe),
                fill_color=color_producer(data["ELEV"][item]),
                color="grey",
            )
        )

    # Add feature groups and and layer control to the map
    map.add_child(fg_population)
    map.add_child(fg_volcano)
    map.add_child(folium.LayerControl())

    # Save the map
    map.save("volcano_map.html")


if __name__ == "__main__":
    sheffield_map()
    volcano_map()

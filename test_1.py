import pandas as pd
import geojson
from shapely import wkt
from shapely.geometry import mapping

# Load the CSV data into a DataFrame
csv_file = 'csv.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file)

# Initialize an empty list to hold GeoJSON features
features = []

# Iterate over each row in the DataFrame
for _, row in df.iterrows():
    # Parse the WKT geometry
    polygon = wkt.loads(row['geometry'])

    # Convert each row into a GeoJSON feature
    feature = geojson.Feature(
        geometry=mapping(polygon),  # Convert to GeoJSON geometry format
        properties={
            'latitude': row['latitude'],
            'longitude': row['longitude'],
            'area_in_meters': row['area_in_meters'],
            'confidence': row['confidence'],
            'full_plus_code': row['full_plus_code']
        }
    )

    # Append the feature to the list
    features.append(feature)

# Create a GeoJSON FeatureCollection
feature_collection = geojson.FeatureCollection(features)

# Write the FeatureCollection to a GeoJSON file
geojson_file = 'output_file2.geojson'  # Replace with your desired output file path
with open(geojson_file, 'w') as f:
    geojson.dump(feature_collection, f)

print(f"GeoJSON file saved as {geojson_file}")

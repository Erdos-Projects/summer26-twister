import urllib.request
from pathlib import Path
import argparse
import io
import geopandas as gpd

def main(zip_url: str, output: str) -> None:
    
    print("Downloading ZIP...")
    with urllib.request.urlopen(ZIP_URL) as r:
        data = r.read()

    print("Creating GeoDataFrame...")
    gdf = gpd.read_file(io.BytesIO(data))
    
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"Saving to {output}...")
    gdf.to_file(output)
    
def parse_arguments():
    
    ZIP_URL = (
        "https://www.roc.noaa.gov/public-documents/shapefiles/" # taken from https://www.roc.noaa.gov/branches/program-branch/site-id-database/site-id-location-maps.php
        "WSR-88D_OperationalCoverage_BOB_20260430.zip"
    )
    
    parser = argparse.ArgumentParser(description="Download NEXRAD coverage into a GeoDataFrame.")
    parser.add_argument('--zip-url', 
                        type=str, 
                        help='URL to zip file containing the shapefile of NEXRAD coverage.',
                        default=ZIP_URL,
    )
    parser.add_argument('--output',
                        '-o', 
                        type=str, 
                        help='Path to output file.', 
                        default='./data/raw/coverage/WSR-88D_OperationalCoverage_BOB_20260430.shp'
    )
    args = parser.parse_args()
    
    return args

if __name__ == "__main__":
    
    args = parse_arguments()
    ZIP_URL = args.zip_url
    main(**vars(args))
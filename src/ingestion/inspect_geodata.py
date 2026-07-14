from pathlib import Path

import geopandas as gpd


def inspect_geospatial_file(file_path: str) -> None:
    """
    Load a geospatial dataset and display basic validation information.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    data = gpd.read_file(path)

    print(f"File: {path.name}")
    print(f"Number of records: {len(data)}")
    print(f"Coordinate reference system: {data.crs}")
    print(f"Geometry types: {data.geometry.geom_type.value_counts().to_dict()}")
    print(f"Columns: {list(data.columns)}")
    print(f"Missing geometries: {data.geometry.isna().sum()}")
    print(f"Invalid geometries: {(~data.geometry.is_valid).sum()}")


if __name__ == "__main__":
    dataset_path = "data/raw/sample.geojson"

    try:
        inspect_geospatial_file(dataset_path)
    except (FileNotFoundError, ValueError) as error:
        print(f"Unable to inspect dataset: {error}")
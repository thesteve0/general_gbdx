from gbdxtools import Interface
from gbdxtools.task import env
from gbdxtools.catalog import Catalog



# Loads up the gdbxtools "main" class that holds our crecentials
# Expects a .gbdx-config in the users home directory
# Specification of the file contents here - https://github.com/tdg-platform/gbdx-auth#ini-file
gbdx = Interface()


def search(bbox_local):
    types = ["SENTINEL2"]
    results = gbdx.catalog.search(searchAreaWkt=bbox_local,types=types)
    print(results)


bbox = env.inputs.get('bbox', '-104.5930463075638, 38.242156852455665, -104.59068596363069, 38.24456324037886')
search(bbox_local=bbox)
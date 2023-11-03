try:
    import geostack
    from geostack.raster import Raster
    from geostack.runner import runScript

    testA = Raster(name='testA')
    testA.init(nx=256, hx=1.0, ny=256.0, hy=1.0)
    runScript("testA = randomNormal(0, 1);", [testA])

    print("Geostack is loaded!")
except Exception as _:
    print("Geostack installation doesn't work")
    raise RuntimeError("failed")

try:
    from geostack.vector import Vector
    from geostack.io import geoJsonToVector
    from geostack.runner import runVectorScript

    # GeoJSON string
    geojson = '''{
        "features": [
            {"geometry": {"coordinates": [0, 1.5], "type": "Point"},
                "properties": {"r": 10}, "type": "Feature"},
            {"geometry": {"coordinates": [[0, 0], [1, 1], [2, 0], [3, 1]], "type": "LineString"},
                "properties": {"r": 20}, "type": "Feature"},
            {"geometry": {"coordinates": [[[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]], [[0.25, 0.25], [0.25, 0.75], [0.75, 0.75], [0.75, 0.25], [0.25, 0.25]]], "type": "Polygon"},
                "properties": {"r": 30}, "type": "Feature"},
            {"geometry": {"coordinates": [[[0.5, 0.5], [1.5, 0.5], [1.5, 1.5], [0.5, 1.5], [0.5, 0.5]]], "type": "Polygon"},
                "properties": {"r": 40}, "type": "Feature"},
            {"geometry": {"coordinates": [2, 0.75], "type": "Point"},
                "properties": {"r": 50}, "type": "Feature"}
            ], "type": "FeatureCollection"
        }'''

    # Parse GeoJSON
    v = geoJsonToVector(geojson, enforceProjection=False)
    v2 = Vector.assign(v)
    runVectorScript('if (r < 30) keep = false;', v)

    print(v)
    print(v2)
except Exception as e:
    raise e
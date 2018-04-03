import mapnik
m = mapnik.Map(1920,1080)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')

r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)

point_sym = mapnik.MarkersSymbolizer()
point_sym.filename

basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[Propinsi]'), 'DejaVu Sans Bold',5,mapnik.Color('red'))
basinsLabels.halo_fill = mapnik.Color('red')
basinsLabels.halo_radius = 2
r.symbols.append(basinsLabels)

point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap = True
r.symbols.append(point_sym)

s.rules.append(r)

m.append_style('Yoesril2',s)
ds = mapnik.Shapefile(file="D:/Tugas 2/INDONESIA_PROP.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Yoesril2')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('black'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('Yoesril',s)
ds = mapnik.Shapefile(file="D:/Tugas 2/INDONESIA_KEC.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Yoesril')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('red'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('Yoesril3',s)
ds = mapnik.Shapefile(file="D:/Tugas 2/IND_PNT_polyline.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Yoesril3')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('cyan'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('Yoesril4',s)
ds = mapnik.Shapefile(file="D:/Tugas 2/IND_SNG_polyline.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Yoesril4')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('black'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('Yoesril5',s)
ds = mapnik.Shapefile(file="D:/Tugas 2/IND_KOT_point.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Yoesril5')
m.layers.append(layer)

m.zoom_all()
mapnik.render_to_file(m,'world.jpeg','jpeg')
print "rendered image to 'world.jpeg"
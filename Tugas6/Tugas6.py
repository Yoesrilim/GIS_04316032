import mapnik
m = mapnik.Map(1280,720)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('White')
r.symbols.append(polygon_symbolizer)

s.rules.append(r)
m.append_style('Yoesril',s)
ds = mapnik.Shapefile(file="INDONESIA_PROP.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Yoesril')
m.layers.append(layer)
m.zoom_all()

s.rules.append(r)

point_sym = mapnik.MarkersSymbolizer()
point_sym.filename

s = mapnik.Style()
r = mapnik.Rule()

basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[point]'), 'DejaVu Sans Bold',2,mapnik.Color('black'))
basinsLabels.halo_fill = mapnik.Color('Yellow')
basinsLabels.halo_radius = 0.3
r.symbols.append(basinsLabels)

point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap = True
point_sym.opacity = 0.5
point_sym.file = ()
r.symbols.append(point_sym)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('Yellow'),1)
line_symbolizer.stroke_width = 9.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Yoesril2',s)
ds = mapnik.Shapefile(file="100POINT.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Yoesril2')
m.layers.append(layer)
m.zoom_all()

mapnik.render_to_file(m,'Peta.PNG', 'PNG')
print "rendered image to 'Peta.PNG' "
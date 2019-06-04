from points import find_nearest_point, find_nearest_block


def get_lines_by_layer(modelspace, layer_names):
    string = 'LINE['
    separator = ' | '
    for n, name in enumerate(layer_names):
        layer_names[n] = 'layer=="' + layer_names[n] + '"'
    string += separator.join(layer_names)
    string += ']'
    return modelspace.query(string)


def find_associated_entities(line, blocks, dot_points):
    start = line.dxf.start
    end = line.dxf.end
    leader_start = find_nearest_point(start, dot_points)
    leader_block = find_nearest_block(end, blocks)

    return leader_start, leader_block

def get_blocks_by_name(modelspace, block_names):
    string = 'INSERT['
    separator = ' | '
    for n, name in enumerate(block_names):
        block_names[n] = 'name=="' + block_names[n] + '"'
    string += separator.join(block_names)
    string += ']'
    return modelspace.query(string)


def get_ins_point_2d(block):
    return [block.get_dxf_attrib('insert')[0], block.get_dxf_attrib('insert')[1], 0.0]


def calculate_dist(point, end):
    return (end[0] - point[0]) ** 2 + (end[1] - point[1]) ** 2


def find_nearest(point, point_list):
    if point_list:
        current_dist = calculate_dist(point, point_list[0])
        current_end = point_list[0]
        for end in point_list:
            dist = calculate_dist(point, end)
            if dist < current_dist:
                current_dist = dist
                current_end = end
        return current_end
    print('list empty')

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

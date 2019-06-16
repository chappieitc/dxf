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


def get_block_text_data(block):
    string = ''
    wall_opening = False
    dno = None
    rz = None
    layer = '\'K_przebicia w stropach\' '

    for attrib in block.attribs():
        if attrib.dxf.tag in ['wymiar', 'WYMIARY']:  # identify attribute by tag
            string += attrib.dxf.text
        if attrib.dxf.tag == 'Rz.d.':
            if attrib.dxf.text:
                rz = attrib.dxf.text
                wall_opening = True
        if attrib.dxf.tag == 'dno':
            dno = attrib.dxf.text
            if 'w stropie' in attrib.dxf.text:
                wall_opening = False
    if wall_opening:
        layer = '\'K_przebicia w scianach\' '
        string += '\\\\P' + rz + dno

    string = string.replace(',', '.')

    return string, layer

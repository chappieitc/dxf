from blocks import get_blocks_by_name, get_ins_point_2d
from points import find_nearest


def destroy_arde(modelspace):
    # get leader dots insertion points
    all_dots = get_blocks_by_name(modelspace, ['_DOT'])
    dot_points = []
    if len(all_dots):
        wall_opening = 0
        for dot in all_dots:
            point = get_ins_point_2d(dot)
            dot_points.append(point)

    # find blocks and their points
    block_names = ['PEWA_przebicia_opis-tabelka_wentylaccja',
                   'PEWA_przebicia_opis-tabelka_kanalizacja',
                   'PEWA_przebicia_opis-tabelka_woda',
                   'ENERUS_przebicia_opis-tabelka',
                   'A$C39C83691'
                   ]
    all_blocks = get_blocks_by_name(modelspace, block_names)
    all_strings = ''
    if len(all_blocks):
        wall_opening = False
        for block in all_blocks:
            layer = '\'K_przebicia w stropach\' '
            string = ''
            dno = None
            rz = None
            for attrib in block.attribs():
                if attrib.dxf.tag == 'wymiar':  # identify attribute by tag
                    string += attrib.dxf.text
                if attrib.dxf.tag == 'Rz.d.':
                    if attrib.dxf.text:
                        rz = attrib.dxf.text
                        wall_opening = True
                if attrib.dxf.tag == 'dno':
                    dno = attrib.dxf.text
            if wall_opening:
                layer = '\'K_przebicia w scianach\' '
                string += ' ' + rz + dno
                string = string.replace(',', '.')
                wall_opening = False
            ins_point = get_ins_point_2d(block)
            end_point = find_nearest(ins_point, dot_points)

            all_strings += layer + str(ins_point) + ' ' + str(end_point) + ' \'' + string + '\'\P'

            all_strings = all_strings.replace('[', '\'').replace(']', '\'').replace(',', '')

    return all_strings

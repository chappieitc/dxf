import ezdxf

from blocks import *

drawing = ezdxf.readfile('tests/arch.dxf')
modelspace = drawing.modelspace()
block_names = ['PEWA_przebicia_opis-tabelka_wentylaccja',
               'PEWA_przebicia_opis-tabelka_kanalizacja',
               'PEWA_przebicia_opis-tabelka_woda',
               'ENERUS_przebicia_opis-tabelka',
               'A$C39C83691'
               ]

drawing.styles.new('custom', dxfattribs={'font': 'simplex.shx', 'width': 0.7})

all_blocks = get_blocks_by_name(modelspace, block_names)
all_dots = get_blocks_by_name(modelspace, ['_DOT'])

dot_points = []
if len(all_dots):
    flag = 0
    for dot in all_dots:
        point = get_ins_point_2d(dot)
        dot_points.append(point)
else:
    print('nic')

all_strings = ''
if len(all_blocks):
    flag = 0
    for block in all_blocks:
        layer = '\'K_przebicia w stropach\', '
        string = ''
        dno = None
        rz = None
        for attrib in block.attribs():
            if attrib.dxf.tag == 'wymiar':  # identify attribute by tag
                string += attrib.dxf.text
            if attrib.dxf.tag == 'Rz.d.':
                if attrib.dxf.text:
                    rz = attrib.dxf.text
                    flag = 1
            if attrib.dxf.tag == 'dno':
                dno = attrib.dxf.text
        if flag == 1:
            layer = '\'K_przebicia w scianach\' '
            string += ' ' + rz + dno
            string = string.replace(',', '.')  # TODO
            flag = 0
        # print(block.get_dxf_attrib('insert')[0])
        ins_point = get_ins_point_2d(block)

        # text = modelspace.add_text(string, dxfattribs={'style': 'custom', 'height': 15, 'width': 0.7}) \
        #     .set_pos(ins_point, align='MIDDLE_CENTER')

        end_point = find_nearest(ins_point, dot_points)
        # print(end_point)
        # modelspace.add_line(ins_point, end_point)

        all_strings += layer + str(ins_point) + ' ' + str(end_point) + ' \'' + string + '\'\P'

        all_strings = all_strings.replace('[', '\'').replace(']', '\'').replace(',', '')
        mtext = modelspace.add_mtext(all_strings).set_location([0, 0, 0])
        # print(all_strings)
        # print(mtext.dxfattribs())
        # block.set_dxf_attrib('insert', [10883.29218136326, 74953.8350239036, 0.0])
        # print(str(text.dxfattribs()))
        # block.set_dxf_attrib('layer', 'A_przebicia')

drawing.saveas('tests/output.dxf')

import ezdxf

from blocks import get_blocks_by_name, get_ins_point_2d, get_block_text_data
from lines import get_lines_by_layers, find_associated_entities


def extract_arde_leaders(modelspace, layers, block_names):
    # get leader dots insertion points
    dots = get_blocks_by_name(modelspace, ['_Dot'])
    dot_points = []
    if len(dots):
        for dot in dots:
            point = get_ins_point_2d(dot)
            dot_points.append(point)

    # get leader lines
    lines = get_lines_by_layers(modelspace, layers)
    # print(lines[0].dxf.start)

    # get blocks
    blocks = get_blocks_by_name(modelspace, block_names)
    strings = ''

    for line in lines:
        leader_start, block = find_associated_entities(line, blocks, dot_points)
        ins_point = get_ins_point_2d(block)
        string, layer = get_block_text_data(block)

        strings += layer + str(ins_point) + ' ' + str(leader_start) + ' \'' + string + '\'\P'
        strings = strings.replace('[', '\'').replace(']', '\'').replace(',', '')

    return strings


def add_leaders_mtext(input_path, output_path):
    drawing = ezdxf.readfile(input_path)
    modelspace = drawing.modelspace()

    # get leader lines
    layers = ['PEWA_przebicia_opis',
              'PEWA_przebicia_opis_deszczowka',
              'PEWA_przebicia_opis_kanalizacja',
              'PEWA_przebicia_opis_wentylacja',
              'PEWA_przebicia_opis_woda',
              'ENERUS_przebicia_opis'
              ]

    # find blocks and their points
    block_names = ['PEWA_przebicia_opis-tabelka_wentylaccja',
                   'PEWA_przebicia_opis-tabelka_kanalizacja',
                   'PEWA_przebicia_opis-tabelka_deszczowka',
                   'PEWA_przebicia_opis-tabelka_woda',
                   'ENERUS_przebicia_opis-tabelka',
                   'A$C39C83691',
                   'OPIS_PRZEBIĆ'
                   ]

    string = extract_arde_leaders(modelspace, layers, block_names)
    modelspace.add_mtext(string).set_location([0, 0, 0])

    drawing.saveas(output_path)
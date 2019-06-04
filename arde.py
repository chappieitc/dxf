from blocks import get_blocks_by_name, get_ins_point_2d, get_block_text_data
from lines import get_lines_by_layer, find_associated_entities


def destroy_arde(modelspace, layers, block_names):
    # get leader dots insertion points
    dots = get_blocks_by_name(modelspace, ['_DOT'])
    dot_points = []
    if len(dots):
        for dot in dots:
            point = get_ins_point_2d(dot)
            dot_points.append(point)

    # get leader lines
    lines = get_lines_by_layer(modelspace, layers)
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

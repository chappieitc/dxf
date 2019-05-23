import dxfgrabber
import ezdxf

# dxf = dxfgrabber.readfile("szalunek.dxf")
# print("DXF version: {}".format(dxf.dxfversion))
# header_var_count = len(dxf.header) # dict of dxf header vars
# layer_count = len(dxf.layers) # collection of layer definitions
# block_definition_count = len(dxf.blocks) #  dict like collection of block definitions
# entity_count = len(dxf.entities) # list like collection of entities

# drawing = ezdxf.new(dxfversion='AC1024')
# modelspace = drawing.modelspace()
# modelspace.add_line((0, 0), (10, 0), dxfattribs={'color': 7})
# drawing.layers.new('TEXTLAYER', dxfattribs={'color': 2})
# modelspace.add_text('Test', dxfattribs={'insert': (0, 0.2), 'layer': 'TEXTLAYER'})


def blocks_by_name(block_names):
    string = 'INSERT['
    separator = ' | '
    for n, name in enumerate(block_names):
        block_names[n] = 'name=="' + block_names[n] + '"'
    string += separator.join(block_names)
    string += ']'
    print(string)
    return string


drawing = ezdxf.readfile('arch.dxf')
modelspace = drawing.modelspace()
modelspace.add_line((0, 0), (10, 0), dxfattribs={'color': 7})
# all_blocks = modelspace.query('INSERT[name == "A$C39C83691" | name == "PEWA_przebicia_opis-tabelka_wentylaccja"]')
block_names = ['PEWA_przebicia_opis-tabelka_wentylaccja',
               'PEWA_przebicia_opis-tabelka_kanalizacja',
               'PEWA_przebicia_opis-tabelka_woda',
               'ENERUS_przebicia_opis-tabelka',
               'A$C39C83691'
               ]
all_blocks = modelspace.query(blocks_by_name(block_names))
# blocks = blocks.query('INSERT[name=="PEWA_przebicia_opis-tabelka_wentylaccja"]')

# all_blocks = modelspace.query('LINE[text ? ".*"]')
# for name in block_names:
#     # blocks = modelspace.query('INSERT[name=="' + name + '"]')
#     all_blocks.extend(modelspace, 'INSERT[name=="' + name + '"]')

if len(all_blocks):
    for block in all_blocks:
        # entity = all_blocks[0]  # process first entity found
        for attrib in block.attribs():
            if attrib.dxf.tag == "dno":  # identify attribute by tag
                attrib.dxf.text = "dno!"  # change attribute content
drawing.saveas('test.dxf')

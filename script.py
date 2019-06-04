import ezdxf

from arde import destroy_arde


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
                   'A$C39C83691'
                   ]

    string = destroy_arde(modelspace, layers, block_names)
    modelspace.add_mtext(string).set_location([0, 0, 0])

    drawing.saveas(output_path)


add_leaders_mtext('tests/arch.dxf', 'tests/output.dxf')

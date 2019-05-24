import ezdxf

from arde import destroy_arde


def add_leaders_mtext(input_path, output_path):
    drawing = ezdxf.readfile(input_path)
    modelspace = drawing.modelspace()

    string = destroy_arde(modelspace)
    modelspace.add_mtext(string).set_location([0, 0, 0])

    drawing.saveas(output_path)


add_leaders_mtext('tests/arch.dxf', 'tests/output.dxf')

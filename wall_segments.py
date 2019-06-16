import ezdxf

from lines import get_lines_by_layers


def create_segments(input_path, output_path, layers):
    drawing = ezdxf.readfile(input_path)
    modelspace = drawing.modelspace()

    lines = get_lines_by_layers(modelspace, layers)
    print('lines found:' + str(len(lines)))

    segment_list = SegmentList()

    for line in lines:
        if segment_list.add_line(line):
            continue
        else:
            segment = Segment(line)
            segment_list.append(segment)

    print('segments created:' + str(segment_list.list.__len__()))
    segment_list.create(modelspace)
    drawing.saveas(output_path)


class Segment:

    def __init__(self, line):
        self.start = line.dxf.start
        self.end = line.dxf.end
        self.point_list = [line.dxf.start, line.dxf.end]
        # self.axis_list = self.calculate_axis()

    def append(self, line):
        if self.is_closed():
            return False
        if line.dxf.start == self.start:
            self.start = line.dxf.end
            self.point_list.insert(0, line.dxf.end)
        elif line.dxf.end == self.start:
            self.start = line.dxf.start
            self.point_list.insert(0, line.dxf.start)
        elif line.dxf.start == self.end:
            self.end = line.dxf.end
            self.point_list.append(line.dxf.end)
        elif line.dxf.end == self.end:
            self.end = line.dxf.start
            self.point_list.append(line.dxf.start)
        else:
            return False
        return True

    def segment_length(self):
        return self.point_list.__len__() - 1

    def is_closed(self):
        if self.start == self.end:
            return True
        return False

    def create(self, modelspace):
        for i in range(1, self.segment_length() + 1):
            start = self.point_list[i - 1]
            end = self.point_list[i]
            modelspace.add_line(start, end)

    # def calculate_axis(self):


class SegmentList:

    def __init__(self):
        self.list = []

    def append(self, segment):
        self.list.append(segment)

    def add_line(self, line):
        for segment in self.list:
            if segment.append(line):
                return True
        return False

    def create(self, modelspace):
        i = 0
        for segment in self.list:
            segment.create(modelspace)
            i += segment.segment_length()
        print('lines created: ' + str(i))

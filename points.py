from blocks import get_ins_point_2d


def point_point_distance(point_1, point_2):
    return (point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2


def point_block_distance(point, block):
    ins_point = get_ins_point_2d(block)
    return point_point_distance(point, ins_point)


def find_nearest_point(point, point_list):
    if point_list:
        current_dist = point_point_distance(point, point_list[0])
        current_end = point_list[0]
        for end in point_list:
            dist = point_point_distance(point, end)
            if dist < current_dist:
                current_dist = dist
                current_end = end
        return current_end
    print('list empty')


def find_nearest_block(point, block_list):
    if block_list:
        current_dist = point_block_distance(point, block_list[0])
        current_block = block_list[0]
        for block in block_list:
            ins_point = get_ins_point_2d(block)
            dist = point_point_distance(point, ins_point)
            if dist < current_dist and abs(ins_point[1] - point[1]) <= 20.1:
                current_dist = dist
                current_block = block
        return current_block
    print('list empty')

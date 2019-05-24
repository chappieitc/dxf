def calculate_dist(point, end):
    return (end[0] - point[0]) ** 2 + (end[1] - point[1]) ** 2


def find_nearest(point, point_list):
    if point_list:
        current_dist = calculate_dist(point, point_list[0])
        current_end = point_list[0]
        for end in point_list:
            dist = calculate_dist(point, end)
            if dist < current_dist:
                current_dist = dist
                current_end = end
        return current_end
    print('list empty')

def merge(left, right):
    i = j = 0
    h1 = h2 = 0
    result = []

    while i < len(left) and j < len(right):

        if left[i][0] < right[j][0]:
            x = left[i][0]
            h1 = left[i][1]
            i += 1
        elif right[j][0] < left[i][0]:
            x = right[j][0]
            h2 = right[j][1]
            j += 1
        else:
            x = left[i][0]
            h1 = left[i][1]
            h2 = right[j][1]
            i += 1
            j += 1

        height = max(h1, h2)

        if not result or result[-1][1] != height:
            result.append([x, height])

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def skyline(buildings):
    if len(buildings) == 1:
        L, R, H = buildings[0]
        return [[L, H], [R, 0]]

    mid = len(buildings) // 2
    left = skyline(buildings[:mid])
    right = skyline(buildings[mid:])

    return merge(left, right)


buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]

result = skyline(buildings)

print(result)

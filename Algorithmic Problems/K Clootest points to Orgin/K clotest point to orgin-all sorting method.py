'''
def closest_points(list_points, n):
    import math
    sorted_list_points = sorted(list_points, key = lambda l: math.sqrt(l[0]**2+l[1]**2))
    return sorted_list_points[:n]


n=3
points=[(-2,4), (0,-2), (-1,0), (3,5), (-2,-3), (3,2)]

print(closest_points(points, n))
'''

'''
def closest_points(points, n):
    import math
    points.sort(key = lambda l: math.sqrt(l[0]**2+l[1]**2))
    return points[:n]


n=2
points=[(-2,4), (0,-2), (-1,0), (3,5), (-2,-3), (3,2)]

print(closest_points(points, n))
'''


'''
def closest_points(points, n):
    import math
    def magnitude(p):
        return math.sqrt(p[0]**2+p[1]**2)
        
    points.sort(key = magnitude)
    return points[:n]


n=2
points=[(-2,4), (0,-2), (-1,0), (3,5), (-2,-3), (3,2)]

print(closest_points(points, n))

'''

from __future__ import division
import cv2
import numpy
import math


__author__ = 'Eirik'


def find_start_pos(img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i][j] == 255:
                return i, j
    return 0, 0


def get_new_pos(current, direction):
    if direction == 0:
        return current[0] + 0, current[1] - 1
    elif direction == 1:
        return current[0] - 1, current[1] - 1
    elif direction == 2:
        return current[0] - 1, current[1] + 0
    elif direction == 3:
        return current[0] - 1, current[1] + 1
    elif direction == 4:
        return current[0] + 0, current[1] + 1
    elif direction == 5:
        return current[0] + 1, current[1] + 1
    elif direction == 6:
        return current[0] + 1, current[1] + 0
    else:
        return current[0] + 1, current[1] - 1


def get_next_neighbor(current, prev, img):
    neighbors = [
        img[current[0] + 0][current[1] - 1],
        img[current[0] - 1][current[1] - 1],
        img[current[0] - 1][current[1] + 0],
        img[current[0] - 1][current[1] + 1],
        img[current[0] + 0][current[1] + 1],
        img[current[0] + 1][current[1] + 1],
        img[current[0] + 1][current[1] + 0],
        img[current[0] + 1][current[1] - 1]
    ]
    direction = (prev + 1) % 8
    while direction != prev:
        if neighbors[direction] == 255:
            return get_new_pos(current, direction), (direction + 4) % 8
        direction = (direction + 1) % 8
    return None, (direction + 4) % 8


def first_difference(list):
    fd_list = []
    c = list[-1]
    list.insert(0, c)
    for x in range(len(list)-1):
        counter = 0
        pointer = list[x]
        while True:
            if list[x+1] == pointer:
                fd_list.append(counter)
                break
            else:
                counter += 1
                pointer = (pointer + 1) % 8
    return fd_list


def subsample_set(sample_list):
    subsample = []
    sample_counter = 0
    for sample in sample_list:
        if (sample_counter % 50) == 0:
            subsample.append(sample)
        sample_counter += 1
    return subsample


def major_axis(points):
    max_diam = None
    for p1 in points:
        for p2 in points:
            if max_diam is None:
                max_diam = p1, p2
            elif dist(max_diam[0], max_diam[1]) < dist(p1, p2):
                max_diam = p1, p2
    return max_diam


def minor_axis(points, major_axis):
    max_diam = None
    desired_slope = des_slope(major_axis)
    error = 0.00001
    for p1 in points:
        for p2 in points:
            if p1 is not major_axis[0] and p1 is not major_axis[1] and p2 is not major_axis[1] and p2 is not major_axis[0]:
                if desired_slope + error >= slope(p1, p2) >= desired_slope - error:
                    if max_diam is None:
                        max_diam = p1, p2
                    elif dist(max_diam[0], max_diam[1]) < dist(p1, p2):
                        max_diam = p1, p2
    print(slope(major_axis[0], major_axis[1]))
    print(slope(max_diam[0], max_diam[1]))
    return max_diam

def dist(p1, p2):
    return math.sqrt(math.pow(p2[1] - p1[1], 2) + math.pow(p2[0] - p1[0], 2))


def des_slope(axis):
    #print axis
    if slope(axis[0], axis[1]) == 0:
        return 0.0000001
    else:
        return -1/(slope(axis[0], axis[1]))


def slope(p1, p2):
    max_x = p1
    min_x = p2
    if p1[1] < p2[1]:
        max_x = p2
        min_x = p1
    if (max_x[1] - min_x[1]) == 0:
        return 0
    else:
        return (max_x[0] - min_x[0])/(max_x[1] - min_x[1])


def boundary_and_chain(img):
    """
    :rtype : tuple
    """
    chain = []
    boundary = []
    prev = 0
    current = find_start_pos(binary_img)
    start = current
    boundary.append(current)
    start_counter = 0

    while start_counter < 2:
        if start == current:
            start_counter += 1
        current, prev = get_next_neighbor(current, prev, img)
        if current is None:
            break
        boundary.append(current)
        #print len(boundary)
        chain.append((prev + 4) % 8)
    return boundary, chain

def boxRatio(box):
    xs = [p[0] for p in box]
    ys = [p[1] for p in box]
    xMin, xMax, yMin, yMax = min(xs), max(xs), min(ys), max(ys)
    h = yMax - yMin
    w = xMax - xMin
    ratio = float(max(h, w))/float(min(h, w))
    return ratio, h, w

def shapeBox(box, sq):
    xs = [p[0] for p in box]
    ys = [p[1] for p in box]
    xMin, xMax, yMin, yMax = min(xs), max(xs), min(ys), max(ys)
    h = yMax - yMin
    w = xMax - xMin

    addedHeight = shapeAdd(h, sq)
    addedWidth = shapeAdd(w, sq)

    newBox = numpy.array(map(lambda p: [p[0] + addedWidth, p[1] + addedHeight] if (p[0] == xMax and p[1] == yMax) 
                        else [p[0] + addedWidth, p[1]] if (p[0] == xMax)
                        else [p[0], p[1] + addedHeight] if (p[1] == yMax)
                        else p, box))

    return newBox

def shapeAdd(d, sq):
    return 0 if d % sq == 0 else sq - d % sq


def grid(shapeBox):
    shapeBox = map(list, shapeBox)
    orderedPoints = []

    yMin = 99999
    for p in shapeBox:
        if p[1] < yMin:
            first = p
            yMin = p[1]
        elif p[1] == yMin and p[0] < first[0]:
            first = p
    orderedPoints.append(first)

    xMax = -99999
    for p in shapeBox:
        if p[0] > xMax:
            second = p
            xMax = p[0]
        elif p[0] == xMax and p[1] < second[1]:
            second = p
    orderedPoints.append(second)

    yMax = -99999
    for p  in shapeBox:
        if p[1] > yMax:
            third = p
            yMax = p[1]
        elif p[1] == yMax and p[0] > third[0]:
            third = p
    orderedPoints.append(third)

    xMin = 99999
    for p  in shapeBox:
        if p[0] < xMin:
            fourth = p
            xMin = p[0]
        elif p[0] == xMin and p[1] > fourth[1]:
            fourth = p
    orderedPoints.append(fourth)


    xSteps = int((orderedPoints[1][0] - orderedPoints[0][0]) / 10)
    ySteps = int((orderedPoints[3][1] - orderedPoints[0][1]) / 10)
    
    opposite = orderedPoints[1][0] - orderedPoints[0][0]
    close = orderedPoints[1][1] - orderedPoints[0][1]

    if close != 0:
        angle = math.atan(opposite/close)
    else:
        angle = 0

    grid = [[] for _ in range(ySteps + 1)]

    for y in range(0, ySteps + 1):
        for x in range(0, xSteps + 1):
            grid[y].append([orderedPoints[0][0] + x * 10, orderedPoints[0][1] + y * 10])

    return grid



def valid_grid_points(grid_points, boundary_points):
    valid_points = []
    for i in boundary_points:
        for j in grid_points:
            if dist(i, j) <= 5 and j not in valid_points:
                valid_points.append(j)
                break
    return valid_points


def get_chain_code(boundary):
    current = boundary[-1]
    chain = []
    for i in boundary:
        dx = i[0]-current[0]
        dy = i[1]-current[1]
        if dx < 0 and dy == 0:
            chain.append(0)
        if dx < 0 and dy < 0:
            chain.append(1)
        if dx == 0 and dy < 0:
            chain.append(2)
        if dx > 0 and dy < 0:
            chain.append(3)
        if dx > 0 and dy == 0:
            chain.append(4)
        if dx > 0 and dy > 0:
            chain.append(5)
        if dx == 0 and dy > 0:
            chain.append(6)
        if dx < 0 and dy > 0:
            chain.append(7)
        current = i
    return chain

def cyclic_equiv(u, v):
    n, i, j = len(u), 0, 0
    if n != len(v):
        return False
    while i < n and j < n:
        k = 1
        while k <= n and u[(i + k) % n] == v[(j + k) % n]:
            k += 1
        if k > n:
            return True
        if u[(i + k) % n] > v[(j + k) % n]:
            i += k
        else:
            j += k
    return False

def classify(diff):

    no_zeroes = filter(lambda n: n != 0, diff)

    if cyclic_equiv(no_zeroes, [2, 2, 2, 2, 2, 6]):
        return "l-shape"

    if no_zeroes == [2, 2, 2, 2]:
        firstTwo = diff.index(2)
        firstZeroes = 0
        secondZeroes = 0
        first = True
        for n in diff[firstTwo + 1:]:
            if n == 0 and first:
                firstZeroes += 1
            elif n == 0:
                secondZeroes += 1
            elif first:
                first = False
            else:
                break

        if firstZeroes == secondZeroes:
            return "square"
        else:
            return "rectangle"

    if cyclic_equiv(no_zeroes, [2, 3, 3]):
        return "triangle"

    counter = 0
    edges = 0
    for n in diff:
        if n > 4:
            counter -= (8 - n)
        else:
            counter += n
        if counter > 3 * (edges + 1):
            edges += 1
    if edges == 3:
        return "triangle"

    return diff


def circular_distance_tracing(centroid, boundary):
    distance_list = []
    for i in boundary:
        distance_list.append(dist(centroid, i))
    return distance_list


def shape_detection(distance_list):
    avarage_dist = sum(distance_list)/len(distance_list)




# importing image as gray scale image (one channel only)
image = cv2.imread('utilidades\figuras.png', 0)

# making a binary image
(thresh, im_bw) = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thresh = 127
binary_img = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)[1]

# extracting boundary points and chain code through an implementation of Moore-Neighbor algorithm
boundary_points, chain_code = boundary_and_chain(binary_img)

#making new binary image from boundary points
boundary_img = numpy.zeros(image.shape, numpy.uint8)
for i in boundary_points:
    boundary_img[i[0]][i[1]] = 255

# subsample of boundary points
subsample = subsample_set(boundary_points)
subsample_img = numpy.zeros(image.shape, numpy.uint8)
for i in subsample:
    subsample_img[i[0]][i[1]] = 255

# printing results
#print chain_code

# normalizing chain code to make it rotation independent
#print first_difference(chain_code)

#print subsample

# major and minor axis for making a bounding box. May not be applicable and should go for openCV method
#major = major_axis(boundary_points)
#minor = minor_axis(boundary_points, major)
#print major
#print minor

#drawing major and minor axis
#cv2.line(boundary_img, (major[1][1], major[1][0]), (major[0][1], major[0][0]), (255, 0, 0), 1)
#cv2.line(boundary_img, (minor[1][1], minor[1][0]), (minor[0][1], minor[0][0]), (255, 0, 0), 1)


# creating bounding box; numpy array is flipped compared to python list: x,y --> y,x
temp = []
for i in boundary_points:
    temp.append((i[1], i[0]))
numpy_boundary = numpy.array(temp)

rect = cv2.minAreaRect(numpy_boundary)
box = cv2.cv.BoxPoints(rect)
box = numpy.int0(box)
cv2.drawContours(boundary_img, [shapeBox(box, 10)], 0, (255, 0, 0), 1)

#print box, "\n"
#print shapeBox(box, 10), "\n"

# eccentricity
box_ratio = boxRatio(box)

#print box_ratio
g = grid(shapeBox(box, 10))


#for e in g:
#    print e
flat_g = [item for sublist in g for item in sublist]
v = valid_grid_points(flat_g, temp)
chain = get_chain_code(v)

#print v[0]
f_diff = first_difference(chain)

print(classify(f_diff))

# histogram of frequencies of direction changes in the chain code
histogram = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
for i in chain_code:
    histogram[i] += 1
#print histogram

for p in v:
    cv2.circle(boundary_img, (p[0], p[1]), 3, (255, 0, 255), -1)

#for p in flat_g:
#  cv2.circle(image, (p[0], p[1]), 3, (255, 0, 255), -1)



# drawing points that form major and minor axis
#cv2.circle(boundary_img, (major[1][1], major[1][0]), 3, (255, 0, 255), -1)
#cv2.circle(boundary_img, (major[0][1], major[0][0]), 3, (255, 0, 255), -1)
#cv2.circle(boundary_img, (minor[1][1], minor[1][0]), 3, (255, 0, 255), -1)
#cv2.circle(boundary_img, (minor[0][1], minor[0][0]), 3, (255, 0, 255), -1)

# showing images
cv2.imshow('original', image)
cv2.imshow('boundary', boundary_img)
#cv2.imshow('subsample', subsample_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
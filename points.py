class Point(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getX(self):
        return self._x

    def getY(self):
        return self._y


class Line(Point):
    def __init__(self, point1, point2):
        self._point_1 = point1
        self._point_2 = point2

    def getSlope(self):
        slope = abs((self._point_1.getY() - self._point_2.getY()) / (self._point_1.getX() - self._point_2.getX()))
        return slope

    def getPoint1(self):
        return self._point_1

    def getPoint2(self):
        return self._point_2


class ColinearPoints(object):
    def __init__(self, points):
        self._points = points
        self._colinear_points = []

    def CalculateSlopesOfPoints(self):

        for index, this_point in enumerate(self._points):
            local_slopes = {}
            for that_point in self._points[index+1:]:
                line = Line(this_point, that_point)
                slope = line.getSlope()

                slope = round(slope, 2)

                #print("=================")
                #print("slope is ", slope)
                #print("point is ", line.getPoint1().getX(), line.getPoint1().getY())
                #print("point is ", line.getPoint2().getX(), line.getPoint2().getY())
                #print("==================")

                # if the slope already exist, then append to it, else add to it.
                if slope not in local_slopes:
                    local_slopes[slope] = set()

                local_slopes[slope].add(line.getPoint1())
                local_slopes[slope].add(line.getPoint2())

            for key in local_slopes.keys():
                if len(local_slopes[key]) > 2:
                    local_co_points = tuple(local_slopes[key])
                    self._colinear_points.append(local_co_points)

def read_file(file):

    points = []

    try:
        f = open(file)
        file = f.readlines()

        for line in file:
            coords = line.strip("\n").split(",")

            # if more than two inputs on the same line, ignore the rest.
            if len(coords) > 2:
                coords = coords[:2]

            if len(coords) != 2:
                # not enough inputs to proceed, ignore this line.
                continue

            if type(coords[0]) is not float or type(coords[1]) is not float:
                # convert to float, if possible
                try:
                    coords = [float(entry) for entry in coords]
                except ValueError:
                    continue

            # convert the inputs to an immutable format and add to the points list.
            point = Point(coords[0], coords[1])

            points.append(point)

    except Exception as e:
        print(e)
        exit(1)


    return points


if __name__ == "__main__":

    # open the csv file and read the content.
    # read each line as a tuple
    # add all the tuples to a list for further processing
    file_name = "./test_example1.csv"
    points = read_file(file_name)

    #for entry in points:
    #    print(entry.getX(), entry.getY())

    # Not enough inputs from the file, stop the program.
    # we need at least 3 points to run the solution.
    if len(points) < 3:
        exit(0)

    obj = ColinearPoints(points)
    obj.CalculateSlopesOfPoints()

    for points in obj._colinear_points:
        print("===================")
        for point in points:
            print(point.getX(), point.getY())
        print("===================")

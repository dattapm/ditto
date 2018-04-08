"""
  This file has code to get the colinear points
  in a list of coordinates in a 2D plane.

  Inputs are from a file called "test_example.csv" and
  the output is written back to a file called "test_output.csv".

  Both the csv files are in the same path as this file.

"""

class Point(object):
    """
    Point class holds the X and Y coordinates.
    """
    def __init__(self, x, y):
        """
        :param x: X coordinate
        :param y: Y coordinate
        """
        self._x = x
        self._y = y

    def getX(self):
        """
        :return: X coordinate
        """
        return self._x

    def getY(self):
        """
        :return: Y coordinate
        """
        return self._y


class Line(Point):
    """
    Line class represents a line connecting two points
    _point_1 and _point_2.
    """
    def __init__(self, point1, point2):
        """
        :param point1: Represent _point_1
        :param point2: Represent _point_2
        """
        self._point_1 = point1
        self._point_2 = point2

    def getSlope(self):
        """
        slope = abs(Y2 - Y1/X2- X1

        Returns: slope
        """
        slope = abs((self._point_1.getY() - self._point_2.getY()) / (self._point_1.getX() - self._point_2.getX()))
        return slope

    def getPoint1(self):
        """
        :return: _point_1
        """
        return self._point_1

    def getPoint2(self):
        """
       :return: _point_2
        """
        return self._point_2


class ColinearPoints(object):
    """
    Class to calculate the co-linear points from a list of points.
    """
    def __init__(self, points):
        """
        :param points: A list of Point objects in a 2D plane.
        """
        self._points = points
        self._colinear_points = []

    def calculateSlopesOfPoints(self):
        """
        Calculate the slope of points.
        """

        for index, this_point in enumerate(self._points):
            local_slopes = {}
            for that_point in self._points[index+1:]:
                line = Line(this_point, that_point)
                slope = round(line.getSlope(), 2)

                # if the slope already exist, then append to it, else add to it.
                if slope not in local_slopes:
                    local_slopes[slope] = set()

                local_slopes[slope].add(line.getPoint1())
                local_slopes[slope].add(line.getPoint2())

            for key in local_slopes.keys():
                if len(local_slopes[key]) > 2:
                    local_co_points = local_slopes[key]
                    self._colinear_points.append(local_co_points)

    def getColinearPoints(self):
        """
        :return: co-linear points as a list.
        """
        return self._colinear_points


def read_input_file(file):
    """
    Read inputs from a file.

    :param file: input file name.
    :return: Points in a 2D plane as a list.
    """
    points = []

    try:
        f = open(file)
        for line in f.readlines():
            # Remove the "\n" from the end.
            # Split them at ","

            coords = line.strip("\n").split(",")

            # if more than two inputs on the same line, take the first 2 and ignore the rest.
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
        # Unable to open or read the file, exit the program.
        print(e)
        exit(1)

    return points

def write_output_file(points, file):
    """
    Write to an output file.

    :param points: List of tuples. Each tuple is a collection of co-linear Points.

    :param file: output file.

    """
    try:

        f = open(file,  "w")
        for index, point in enumerate(points):
            local_s = []
            for t in point:
                local_s.append(t.getX())
                local_s.append(t.getY())

            s = str(index + 1) + "," + ",".join(str(x) for x in local_s)
            f.write(s)
            f.write("\n")
    except Exception as e:
        # Unable to open or write to a file, exit the program.
        print(e)
        exit(1)


if __name__ == "__main__":

    input_file_name = "./test_example1.csv"
    output_file_name = "./test_output.csv"
    colinear_points = []

    # open the csv file and read the content.
    # read each line as a tuple.
    # add all the tuples to a list for further processing.

    points = read_input_file(input_file_name)

    # Not enough inputs from the file, stop the program.
    # we need at least 3 points to run the solution.
    if len(points) < 3:
        exit(0)

    # Find the co-linear points by using
    # a list of points in a 2D plane.

    obj = ColinearPoints(points)
    obj.calculateSlopesOfPoints()
    colinear_points = obj.getColinearPoints()

    # Write to an output file with all colinear points in a single line.
    write_output_file(colinear_points, output_file_name)
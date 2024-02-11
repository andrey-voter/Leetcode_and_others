#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

struct Point {
	int x;
	int y;

	bool operator < (const Point & other) const {
		return x < other.x;
	}
};

std::vector<Point> ReadData() {
	int n;
	std::cin >> n;
	std::vector<Point> result;
	result.reserve(n);
	while (n--) {
		Point current_point;
		std::cin >> current_point.x >> current_point.y;
		result.push_back(current_point);
	}

	return result;
}

Point GetReflected(int mid_coord, const Point & point) {
	Point reflected  = {mid_coord - point.x, point.y};
	return reflected;
}

int main() {
	std::vector<Point> points = ReadData();
	Point left_point = *std::min_element(begin(points), end(points));
	Point right_point = *std::max_element(begin(points), end(points));
	int doubled_mid_coord = (left_point.x + right_point.x);
	
	std::map<Point, int> points_map;
	
	for (const Point & point : points) {
		++points_map[point];	
	}

	for (const Point & point : points) {
		if (points_map.count(GetReflected(doubled_mid_coord, point))) {
			--points_map[GetReflected(doubled_mid_coord, point)];
			if (points_map[GetReflected(doubled_mid_coord, point)] < 0) {
				std::cout << "FALSE" << std::endl;
				return 0;
			} 
		} else {
			std::cout << "FALSE" << std::endl;
			return 0;
		}

	}
	std::cout << "TRUE" << std::endl;
	return 0;
}

#include <iostream>
#include <cmath>   // sqrt
#include <iomanip> // setprecision

int main() {
    // Координаты точек A, B, C
    float xa, ya, xb, yb, xc, yc;

    std::cout << "Введите координаты точки A (x y): ";
    std::cin >> xa >> ya;

    std::cout << "Введите координаты точки B (x y): ";
    std::cin >> xb >> yb;

    std::cout << "Введите координаты точки C (x y): ";
    std::cin >> xc >> yc;

    // Длины сторон по формуле расстояния между двумя точками
    float ab = std::sqrt((xb - xa) * (xb - xa) + (yb - ya) * (yb - ya));
    float bc = std::sqrt((xc - xb) * (xc - xb) + (yc - yb) * (yc - yb));
    float ca = std::sqrt((xa - xc) * (xa - xc) + (ya - yc) * (ya - yc));

    // Периметр
    float p = ab + bc + ca;

    // Полупериметр
    float s = p / 2.0f;

    // Площадь по формуле Герона
    float area = std::sqrt(s * (s - ab) * (s - bc) * (s - ca));

    std::cout << std::fixed << std::setprecision(3);
    std::cout << "\nРезультаты:\n";
    std::cout << "Периметр треугольника: " << p << "\n";
    std::cout << "Площадь треугольника:  " << area << "\n";

    return 0;
}
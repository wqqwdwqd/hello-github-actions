
function volume(r, h) {
    pi = 3.14159
    return pi * r * r * h
}

function lateral_area(r, h) {
    pi = 3.14159
    return 2 * pi * r * h
}

function main() {
    radius = 5    # радиус
    height = 10   # высота
    
    vol = volume(radius, height)
    area = lateral_area(radius, height)
    
    print "Расчёт параметров цилиндра:"
    print "Радиус (r):", radius
    print "Высота (h):", height
    print "Объём (V = π·r²·h):", vol
    print "Площадь боковой поверхности (S = 2·π·r·h):", area
}

BEGIN {
    main()
}

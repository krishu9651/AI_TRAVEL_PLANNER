# from geopy.distance import geodesic

# def calculate_distance():
#     return "Distance calculator placeholder ready"

from geopy.distance import geodesic

def calculate_distance(city1_coords, city2_coords):
    try:
        distance = geodesic(city1_coords, city2_coords).km
        return f"Distance: {round(distance, 2)} km"
    except:
        return "Error calculating distance"
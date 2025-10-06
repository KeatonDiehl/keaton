# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?

def print_star_names(targets):
    for star_names in targets:
        print(star_names)
print(print_star_names(targets))

def print_names_types(targets):
    for star_names, star_info in targets.items():
        spectral_type = star_info['Spectral Type']
        print({star_names : spectral_type})
print(print_names_types(targets))

def find_big_stars(targets):
    big_stars = []
    for star_name, star_info in targets.items():
        star_magnitude = star_info['Magnitude']
        if abs(star_magnitude) > 0.1:
            big_stars.append((star_name, star_magnitude))
        else:
            0
    return big_stars
print(find_big_stars(targets))

targets['Antares'] = {
    "RA": "16h 29m 24.5s",
    "Dec": "−26° 25′ 55″",
    "Magnitude": 1.09,
    "Spectral Type": "M1.5Iab-Ib"
}
print(targets)


# def declination_near_20(targets, target_declination=20):
#     closest_star = None
#     minimum_difference = 100
#     for star_name, star_info in targets.items():
#         star_declination = star_info['Dec']
#         star_degree = star_declination.split('°')[0]       # Turn the angle into an integer, subtract 20 and find the minimum difference
#         difference = abs(star_degree - target_declination)
#         if difference < minimum_difference:
#             difference = minimum_difference
#             closest_star = star_name
#     print({closest_star, difference})
#     return closest_star
# print(declination_near_20(targets, target_declination=20))

# def declination_near_20(targets, target_declination=20):                  # Trial 2, using the .strip() to get rid of spaces causing errors above
#     closest_star = None
#     min_difference = float('inf')

#     for star_name, star_info in targets.items():
#         star_declination = star_info["Dec"]
    
#         star_degree = star_declination.split('°')[0] 
        
#         # THE FIX IS HERE: .strip() is added to star_degree
#         degree_int = int(star_degree.strip())
        
#         difference = abs(degree_int - target_declination)

#         if difference < min_difference:
#             min_difference = difference
#             closest_star = star_name

#     print({closest_star, difference})
#     return closest_star

# print(declination_near_20(targets, target_declination=20))


def declination_near_20(targets, target_declination = 20):            # After an hour of troubleshooting, I decided to go character by character and inlcude only minus signs or integers
    closest_star = None
    min_difference = float('inf')

    for star_name, star_info in targets.items():
        star_declination_str = star_info["Dec"]
        
        # Get the part of the string before the '°' symbol
        degree_part = star_declination_str.split('°')[0]
        
        # Create a new, empty string to hold only wanted characters
        cleaned_degree_str = ""
        
        for char in degree_part:
            # If the character is a digit or minus sign, add it to the clean string
            if char.isdigit() or char == '-':
                cleaned_degree_str += char
        
        # 5. Convert the clean string to an integer
        degree_int = int(cleaned_degree_str)
        
        difference = abs(degree_int - target_declination)

        if difference < min_difference:
            min_difference = difference
            closest_star = star_name

    print({closest_star, cleaned_degree_str})
    return closest_star

declination_near_20(targets, target_declination = 20)


favorite_constellation = 'Orion'
print(favorite_constellation)
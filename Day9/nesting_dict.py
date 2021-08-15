# nesting a dictionary or a list inside of a dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

nested_travel_log = {
    "France": {"Cities Visited": ["Paris", "Lille", "Dijon"]},
    "Germany": {"Cities Visited": ["Berlin", "Hamburg", "Stuttgart"]}
}

print(nested_travel_log["France"]["Cities Visited"][0])
travel_log["France"][0]= "Mexico"
travel_log["Germany"][0] = "Also Mexico"
print(travel_log["France"][0])

print(travel_log)
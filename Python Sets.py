# 1. Python Sets Adventure



# our_routes = {"LAX", "JFK", "CDG", "DXB"}
# competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# # Destinations that both airlines fly to
# common_destinations = our_routes.intersection(competitor_routes)
# print(f"Common destinations: {common_destinations}")

# # Destinations unique to your airline
# unique_to_our_airline = our_routes.difference(competitor_routes)
# print(f"Destinations unique to our airline: {unique_to_our_airline}")

# # Destinations that neither airline shares
# all_destinations = our_routes.union(competitor_routes)
# neither_shared_destinations = all_destinations - common_destinations
# print(f"Destinations that neither airline shares: {neither_shared_destinations}")


# 2. Set Operations in Data Analysis




# customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

# # Remove duplicates by converting the list to a set
# unique_customer_ids = set(customer_ids)
# print(f"Unique customer IDs: {unique_customer_ids}")



# 3. Music Festival Playlist Organization




# artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]

# # Compile unique artist names into a set
# unique_artists = set()
# for artist in artist_names:
#     unique_artists.add(artist)

# print(f"Unique artist lineup: {unique_artists}")

# # Check for duplicate playlists
# duplicate_playlists = len(artist_names) != len(unique_artists)
# print(f"Duplicate playlists found: {duplicate_playlists}")
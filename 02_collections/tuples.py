"""
02_collections / tuples.py
Topic: Python Tuples (Immutable Ordered Sequences)

JAVASCRIPT DEVELOPER MENTAL MODEL:
----------------------------------
- JavaScript does NOT have a native Tuple type yet (Record & Tuple is still a proposal).
- In JS, you usually simulate tuples with frozen arrays: `Object.freeze([10, 20])`.
- In Python, Tuples are a built-in first-class citizen: `point = (10, 20)`.

WHY USE A TUPLE INSTEAD OF A LIST?
1. Immutability: Once created, elements cannot be added, removed, or changed.
   Protects against accidental mutation in function returns.
2. Performance & Memory: Tuples use less memory and are faster to construct than lists.
3. Hashable: Tuples CAN be used as dictionary keys or set elements!
   Lists CANNOT be dict keys because lists are mutable (unhashable).
"""

# ------------------------------------------------------------------------------
# 1. Tuple Creation
# ------------------------------------------------------------------------------
# Defined using parentheses () instead of square brackets []
coordinates = (37.7749, -122.4194)  # Latitude, Longitude
server_config = ("localhost", 8080, True)

# GOTCHA: A single-element tuple MUST have a trailing comma!
# Without comma, Python treats it as normal parenthesized grouping:
not_a_tuple = ("hello")     # type: str!
single_tuple = ("hello",)   # type: tuple!

print("coordinates:", coordinates, type(coordinates))
print("single_tuple:", single_tuple, type(single_tuple))


# ------------------------------------------------------------------------------
# 2. Immutability
# ------------------------------------------------------------------------------
# coordinates[0] = 40.0
# TypeError: 'tuple' object does not support item assignment!


# ------------------------------------------------------------------------------
# 3. Tuple Unpacking (Equivalent to JS Array Destructuring)
# ------------------------------------------------------------------------------
# JS: const [lat, lng] = coordinates;
lat, lng = coordinates
print(f"Unpacked: lat={lat}, lng={lng}")

# Rest pattern unpacking (like JS ...rest):
# JS: const [host, ...otherConfig] = serverConfig;
host, *other_config = server_config
print(f"host={host}, other_config={other_config}")


# ------------------------------------------------------------------------------
# 4. Using Tuples as Dictionary Keys (Lists cannot do this!)
# ------------------------------------------------------------------------------
# In JS, object keys must be strings or symbols. In Python, any hashable
# immutable type (int, str, tuple) can be a key!
geo_cache = {
    (37.7749, -122.4194): "San Francisco",
    (40.7128, -74.0060): "New York City",
    (51.5074, -0.1278): "London",
}

target_coord = (40.7128, -74.0060)
print(f"City at {target_coord}: {geo_cache[target_coord]}")

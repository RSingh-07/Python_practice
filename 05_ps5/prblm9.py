# Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]} 

print(s) #TypeError: unhashable type: 'list'

#A set in Python stores only hashable (immutable) items.
# ✅ Hashable (allowed): int, float, str, tuple (with only hashable items)

# ❌ Unhashable (not allowed): list, dict, set, etc.
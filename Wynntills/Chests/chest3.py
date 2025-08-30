import json

# Load the file
with open("Wynncraftchests.json", "r") as file:
    data = json.load(file)

# Group entries by (x, y, z) location
from collections import defaultdict

location_map = defaultdict(list)
for entry in data:
    loc = tuple(entry["location"][key] for key in ("x", "y", "z"))
    location_map[loc].append(entry)

# Filter entries to keep only one per location
cleaned_data = []

for loc, entries in location_map.items():
    if len(entries) == 1:
        # Only one entry for this location, keep it
        cleaned_data.append(entries[0])
    else:
        # More than one entry: prefer the one without " T" in the name
        no_t_entries = [e for e in entries if " T" not in e["name"]]
        if no_t_entries:
            cleaned_data.append(no_t_entries[0])
        else:
            # If all have " T", just keep the first
            cleaned_data.append(entries[0])

# Save the cleaned data to a new file
with open("cleaned_file.json", "w") as f:
    json.dump(cleaned_data, f, indent=2)

print(f"Original entries: {len(data)}")
print(f"Cleaned entries: {len(cleaned_data)}")
print("Duplicates removed based on (x, y, z) and name preference.")

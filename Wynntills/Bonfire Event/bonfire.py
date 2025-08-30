import json

# Input and output file names
input_file = "bonfire"
output_file = "bonfire.json"

# Fixed values
DEFAULT_COLOR = "#ffffffff"
DEFAULT_ICON = "star"
DEFAULT_VISIBILITY = "always"

entries = []

# Read coordinates from bonfire file
with open(input_file, "r") as f:
    for idx, line in enumerate(f, start=1):
        line = line.strip()
        if not line:
            continue  # skip empty lines
        x, y, z = map(int, line.split(","))

        entry = {
            "name": f"Bonfire 2025 {idx}",
            "color": DEFAULT_COLOR,
            "icon": DEFAULT_ICON,
            "visibility": DEFAULT_VISIBILITY,
            "location": {
                "x": x,
                "y": y,
                "z": z
            }
        }
        entries.append(entry)

# Save to JSON
with open(output_file, "w") as f:
    json.dump(entries, f, indent=2)

print(f"Converted {len(entries)} coordinates to {output_file}")

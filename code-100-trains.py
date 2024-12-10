import pandas as pd

csv_file = "100-trains-uncoded.csv"
df = pd.read_csv(csv_file, na_values=[])

replacements = {
    "long": 2, "short": 1,
    "closedblopnrect": 1, "closedrect": 2, "closedtrap": 3,
    "closedushaped": 4, "dblopnrect": 5, "ellipse": 6,
    "hexagon": 7, "jaggedrect": 8, "openrect": 9,
    "opentrap": 10, "slopetopdblopnrect": 11, "slopetoprect": 12,
    "slopetoptrap": 13, "slopetopushaped": 14, "ushaped": 15,
    "circlelod": 1, "hexagonlod": 2, "rectanglod": 3, "trianglod": 4,
    "east": 1, "west": 0
}

columns_to_replace = ['length1', 'length2', 'length3', 'length4',
                      'shape1', 'shape2', 'shape3', 'shape4',
                      'load_shape1', 'load_shape2', 'load_shape3', 'load_shape4',
                      'Class_attribute']

for col in columns_to_replace:
    df[col] = df[col].replace(replacements)

df = df.fillna(0)
df.to_csv("100-trains-coded.csv", index=False)

print("Coded file generated.")


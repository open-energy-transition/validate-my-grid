import csv

with open('../data/voltages.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        country = row['country_code']
        allowed_voltages = row['allowed_voltages'].split(';')
        rule = f"""
relation[power=~/line_section|circuit/][voltage][voltage!~ /^({'|'.join(allowed_voltages)})$/ ][inside("{country}")],
way[power=~/line|minor_line|cable/][voltage][voltage!~ /^({'|'.join(allowed_voltages)})$/ ][inside("{country}")] {{
    throwError: tr("Invalid voltage value for this country");
    suggestAlternative: "{'/'.join(allowed_voltages)}";
}}
"""
        print(rule)

import csv

with open('../data/voltages.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        country = row['country_code']
        wiki = row['wiki']
        allowed_voltages = row['allowed_voltages'].split(';')
        rule = f"""
relation[power=~/line_section|circuit/][voltage][voltage!~/;/][voltage!~ /^({'|'.join(allowed_voltages)})$/ ][inside("{country}")],
way[power=~/line|minor_line|cable/][voltage][voltage!~/;/][voltage!~ /^({'|'.join(allowed_voltages)})$/ ][inside("{country}")] {{
    throwError: tr("Invalid voltage value for this country");
    suggestAlternative: "{'/'.join(allowed_voltages)}";
    -osmoseDetail: tr("Each country has its own voltage set used for electricity transmission.");
    -osmoseExample: tr("For example, in Jordan, only 132 kV and 400 kV voltages are used.");
    -osmoseFix: tr("Check the list of possible values for this country on the wiki and correct the `{0}` tag.", "voltage");
    -osmoseTags: list("tag", "power");
    -osmoseResource: "{wiki}";
    -osmoseTrap: "If the voltage in OSM is correct but is showing as an error here, check the wiki page and make the necessary corrections. Then create [an issue on GitHub](https://github.com/open-energy-transition/validate-my-grid/issues) to update this check.";
}}
"""
        print(rule)

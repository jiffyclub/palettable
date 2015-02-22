"""
Color maps come from colorbrewer2.org as an Excel file. I've converted the
Excel file to CSV and here I convert it to JSON for easy reading into Python.

"""

import sys
from csv import DictReader
from collections import OrderedDict
import json


def new_sub_map(row, sm_dict):
    num_colors = int(row['NumOfColors'])
    sm_dict[num_colors] = OrderedDict()
    sub_map = sm_dict[num_colors]

    sub_map['NumOfColors'] = num_colors
    sub_map['Type'] = row['Type']
    sub_map['Colors'] = [(int(row['R']), int(row['G']), int(row['B']))]

    return sub_map


def read_csv_to_dict():
    color_maps = OrderedDict()

    for scheme_type in ('Sequential', 'Diverging', 'Qualitative'):
        color_maps[scheme_type] = OrderedDict()

    with open('colorbrewer_all_schemes.csv', 'r') as csvf:
        csv = DictReader(csvf)

        for row in csv:
            if row['SchemeType']:
                # first row of a new color map block
                color_maps[row['SchemeType']][row['ColorName']] = OrderedDict()
                current_map = color_maps[row['SchemeType']][row['ColorName']]

                current_submap = new_sub_map(row, current_map)

            elif row['ColorName']:
                # first row of a new sub-map block
                current_submap = new_sub_map(row, current_map)

            elif not row['ColorName']:
                # continuation of a sub-map block
                current_submap['Colors'].append((int(row['R']),
                                                 int(row['G']),
                                                 int(row['B'])))

    return color_maps


def save_to_json(color_maps):
    with open('colorbrewer_all_schemes.json', 'w') as f:
        json.dump(color_maps, f, indent=1)


def main():
    color_maps = read_csv_to_dict()
    save_to_json(color_maps)


if __name__ == '__main__':
    sys.exit(main())

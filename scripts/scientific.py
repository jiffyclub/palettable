"""
Script for translating the .txt RGB files in
http://www.fabiocrameri.ch/colourmaps.php to a colordata.py file.

This means converting 0-1 floats to 0-255 integers and formatting the
data as lists of lists.

"""
import sys
from pathlib import Path
from typing import Iterable, TextIO, Tuple

import click


def float_rgb_to_int(value: float) -> int:
    return round(value * 255)


def read_rgb_txt(filename: Path) -> Iterable[Tuple[float, float, float]]:
    with filename.open('r') as fp:
        yield from (
            tuple(float_rgb_to_int(float(x)) for x in row.split()) for row in fp
        )


def process_file(filename: str, dest: TextIO):
    filename: Path = Path(filename)
    dest.write(f'{filename.stem.upper()} = (\n')

    for rgb in read_rgb_txt(filename):
        dest.write(f'    {rgb},\n')
    dest.write(')\n\n')


@click.command()
@click.argument("dest", type=click.File("w"))
@click.argument("sources", nargs=-1)
def main(dest: TextIO, sources: Tuple):
    dest.write('# Via http://www.fabiocrameri.ch/colourmaps.php\n\n')

    for filename in sources:
        process_file(filename, dest)


if __name__ == "__main__":
    sys.exit(main())

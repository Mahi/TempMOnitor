import argparse
import os
try:
    from tkinter import messagebox
    _ALLOW_GUI = True
except ImportError:
    _ALLOW_GUI = False

import requests
import xmltodict


def parse_args():
    """Parse command line arguments."""

    parser = argparse.ArgumentParser()
    parser.add_argument('place', default='helsinki', nargs='?')
    parser.add_argument('--no-gui', dest='gui', action='store_false', default=True)
    parser.add_argument('--boundary', type=float, default=22.0)
    appdata = os.path.join(os.getenv('APPDATA'), 'tempmonitor.txt')
    parser.add_argument('--boundary-file', dest='boundary_file', default=appdata)
    return parser.parse_args()


def make_fmi_url(place):
    """Create a request URL for FMI."""

    base_url = 'http://opendata.fmi.fi/wfs'
    args = {
        'service': 'WFS',
        'version': '2.0.0',
        'request': 'getFeature',
        'storedquery_id': 'fmi::observations::weather::simple',
        'place': place,
    }
    arg_list = '&'.join(
        f'{key}={value}'
        for key, value in args.items()
    )
    return base_url + '?' + arg_list


def t2m_from_xmldict(xmldict):
    """Find the latest t2m value from an XML dict.

    Raises ValueError if a t2m value was not found.
    """

    collection = xmldict['wfs:FeatureCollection']
    for member in reversed(collection['wfs:member']):
        element = member['BsWfs:BsWfsElement']
        if element['BsWfs:ParameterName'] == 't2m':
            return float(element['BsWfs:ParameterValue'])
    raise ValueError('XML dict did not contain a t2m value')


def read_previous_result(file_path):
    """Read the previous result from a file."""

    try:
        with open(file_path) as f:
            return float(f.read())
    except (FileNotFoundError, ValueError):
        return None


def write_new_result(file_path, result):
    """Write the new result to a file."""

    with open(file_path, 'w') as f:
        f.write(str(result))


def main():
    """Main entry point for the program."""

    args = parse_args()
    url = make_fmi_url(args.place)
    response = requests.get(url)
    if not response:
        print(f'Error ({response.status_code}): {response.text}')
        return

    root = xmltodict.parse(response.text)
    t2m = t2m_from_xmldict(root)
    print(f'{t2m}°C')

    if _ALLOW_GUI and args.gui:
        prev_result = read_previous_result(args.boundary_file)
        if prev_result is None or prev_result > args.boundary > t2m:
            messagebox.showinfo('TempMonitor', f'{t2m}°C')
    write_new_result(args.boundary_file, t2m)


if __name__ == '__main__':
    main()

# TempMonitor

A simple temperature monitor that checks the temperature outside:

    $ python tempmonitor.py
    22.4°C

If the temperature has dropped below a certain boundary since the last
time this script was executed, a messagebox will also be shown.
This is useful when the script is tasked to run every X minutes
with cron or Task Scheduler, as it will let you know when
the temperature outside drops below a certain boundary.

Supported command line arguments:

- `place` (positional):
    Where to check the temperature from.
    Default: `helsinki`
- `--no-gui`:
    Don't show a messagebox even if temperature drops below boundary.
- `--boundary`:
    The boundary after which a messagebox will be shown.
    Default: `22.0`
- `--boundary-file`:
    Where to store the previous temperature.
    Default: `%APPDATA%\\tempmonitor.txt`

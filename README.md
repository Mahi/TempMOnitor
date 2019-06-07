# TempMonitor

A simple temperature monitor that checks the temperature outside:

    $ python tempmonitor.py
    22.4°C

The program also stores the latest temperature to a file, allowing
the comparison of the current temperature to the previous temperature.
This is useful if the script is tasked to run every X minutes with cron
or Task Scheduler, as it will optionally let you know when the temperature
outside drops below a certain boundary.

All supported command line arguments:

- `place` (positional):
    Location where to check the temperature from.
    Default: `helsinki`
- `--boundary`:
    Dropping below this temperature will show a messagebox.
    Default: `None`
- `--result-file`:
    Path to a file to store the previous temperature into.
    Default: `%APPDATA%\\tempmonitor.txt`

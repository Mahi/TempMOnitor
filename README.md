# TempMonitor

A simple temperature monitor that checks the temperature outside:

    $ python tempmonitor.py
    22.4°C

The program also stores the latest temperature to a file, allowing
the comparison of the current temperature to the previous temperature.
This is useful when the script is tasked to run every X minutes with cron
or Task Scheduler, as it will let you know when the temperature outside
drops below a certain boundary (optional).

All supported command line arguments:

- `place` (positional):
    Where to check the temperature from.
    Default: `helsinki`
- `--boundary [float]`:
    The boundary temperature: dropping below this will show a messagebox.
    Default: `None`
- `--result-file [str]`:
    Path to a file to store the previous temperature into.
    Default: `%APPDATA%\\tempmonitor.txt`

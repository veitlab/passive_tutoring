# Configuration

This script plays a random song from a list of songs stored in the "all_songs_for_6_birds" folder between the hours of 8:00 and 12:00, with a random wait time of 15 to 30 seconds in between each song.

## Use the script as a "systemd" service  
These commands are used to manage the passive_tutoring service using systemd, a system and service manager for Linux operating systems. systemd provides a standard way to start, stop, and manage services and is the default service manager on many Linux distributions.

- `sudo systemctl daemon-reload`: This command tells the `systemd` daemon to reload its configuration files. This is necessary to pick up any changes made to system services.

- `sudo systemctl enable passive_tutoring.service`: This command enables the `passive_tutoring` service to start automatically at boot time. (use `disable` to undo)

- `sudo systemctl start passive_tutoring.service`: This command starts the `passive_tutoring` service if it is not already running. (use `stop` to undo) 

- `sudo systemctl status passive_tutoring.service`: This command displays the status of the `passive_tutoring` service, including whether it is currently running and any errors that may have occurred.

# configuration
## use the script as a systemd service  
These commands are used to manage the passive_tutoring service using systemd, a system and service manager for Linux operating systems. systemd provides a standard way to start, stop, and manage services and is the default service manager on many Linux distributions.

- `sudo systemctl daemon-reload`: This command tells the `systemd` daemon to reload its configuration files. This is necessary to pick up any changes made to system services.

- `sudo systemctl enable passive_tutoring.service`: This command enables the `passive_tutoring` service to start automatically at boot time. (use `disable` to undo)

- `sudo systemctl start passive_tutoring.service`: This command starts the `passive_tutoring` service if it is not already running. (use `stop` toundo) 

- `sudo systemctl status passive_tutoring.service`: This command displays the status of the `passive_tutoring` service, including whether it is currently running and any errors that may have occurred.

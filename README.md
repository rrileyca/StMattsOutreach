This is for the St. Matthew's Outreach!

# Initialization

Curl the `initializer.sh` file and pipe it into `bash` to install the git repo and setup the `updater.sh` in bashrc.

```bash
curl https://raw.githubusercontent.com/Soxcks/StMattsOutreach/master/Updater/initializer.sh | bash
```

If you're having trouble with cache, use thre `-H` option

```bash
curl -H 'Cache-Control: no-cache' https://raw.githubusercontent.com/Soxcks/StMattsOutreach/master/Updater/initializer.sh | bash
```

# Updating

Updating resets the `Outreach` base folder to the previous Git commit, then `pull`s the latest commit from Github. This erases EVERYTHING in the `Outreach` folder, so don't make any changes you want to keep!!!

The `initializer.sh` script sets up `updater.sh` script to be run every time `bash` starts.

To manually update, just run the `updater.sh` script.

# Nuke and pave!

If everything has gone wrong, use the `nuker.sh` to delete everything and start over from scratch.

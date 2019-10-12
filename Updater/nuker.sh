#!/bin/bash

read -p "You are about to reset the Outreach folder. Are you sure? Press 'y' to proceed. " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    DIRECTORY=~/Desktop/Outreach
    rm -rf $DIRECTORY
    printf "\nCompleted. Run the 'initializer.sh' script to start over.\n"

else
    echo "Aborting!"
fi
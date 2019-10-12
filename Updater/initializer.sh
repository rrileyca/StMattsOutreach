#!/bin/bash

DIRECTORY=~/Desktop/Outreach

# Create the Outreach folder, if it doesn't exist
if [ ! -d "$DIRECTORY" ]; then
  mkdir $DIRECTORY
  printf "\n### ~/OUTREACH DIRECTORY CREATED\n"
fi

printf "\n### CLONING GIT REPO TO ~/OUTREACH\n"
git clone https://github.com/Soxcks/StMattsOutreach.git $DIRECTORY
printf "\nCompleted! :-)\n"
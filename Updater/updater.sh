#!/bin/bash

DIRECTORY=~/Desktop/Outreach

if [ ! -d $DIRECTORY ]; then
  printf "\nIt looks like the 'initializer.sh' script hasn't been run.\nRun that first!\n\n"

else
  cd $DIRECTORY
  git reset --hard
  git pull
  printf "\nCompleted :-)\n"
fi
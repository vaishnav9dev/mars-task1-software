#!/bin/bash

echo "Creating mission directory..."
mkdir -p rover_mission

cd rover_mission

echo "Creating mission log..."
echo "Mission initialized successfully" > mission_log.txt

echo "Listing files:"
ls

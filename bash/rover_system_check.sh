#!/bin/bash

echo "Checking system status..."

battery=75

if [ $battery -gt 20 ]; then
    echo "Battery level sufficient: $battery%"
else
    echo "Warning: Low battery!"
fi

connection="active"

if [ "$connection" == "active" ]; then
    echo "Communication link established"
else
    echo "Communication failure"
fi

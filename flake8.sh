#!/bin/bash
rm flake8.txt
clear
flake8 --ignore W191,E501,E402 --output-file flake8.txt
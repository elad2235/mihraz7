#!/bin/bash
rm flake8.txt
clear
flake8 --ignore W191,E501 --output-file flake8.txt
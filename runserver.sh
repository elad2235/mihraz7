#!/bin/bash
find . -name "manage.py" | xargs -I '{}' python3 '{}' runserver
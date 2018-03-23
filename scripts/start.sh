#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn --paste /code/production.ini

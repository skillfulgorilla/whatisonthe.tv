#!/usr/bin/env bash

rsync -av * --exclude '.env' ceaser@demo.whatisonthe.tv://var/www/demo.whatisonthe.tv/

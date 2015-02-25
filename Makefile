#!/usr/bin/env bash

init:
	bundle install

run:
	jekyll serve --watch

build:
	jekyll build

deploy:
	make build
	rsync -av _site/ root@alatar.skillfulgorilla.com://var/www/www.whatisonthe.tv/

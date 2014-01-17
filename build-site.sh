#!/bin/sh
echo ''
echo 'Build AssertJ Site ...'

python generate-html.py

./generate-bootstrap-css.sh
./generate-assertj-css.sh

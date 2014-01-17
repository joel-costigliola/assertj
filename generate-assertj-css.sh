#!/bin/sh
echo ''
echo 'Generating assertj.css ...'
lessc css/assertj.less > css/assertj.css
echo 'Generating assertj.min.css ...'
lessc --compress css/assertj.less > css/assertj.min.css

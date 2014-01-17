#!/bin/sh
echo ''
echo 'Generating assertj.css ...'
lessc site/css/assertj.less > site/css/assertj.css
echo 'Generating assertj.min.css ...'
lessc --compress site/css/assertj.less > site/css/assertj.min.css

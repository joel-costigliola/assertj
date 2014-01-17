#!/bin/sh
echo ''
echo 'Generating bootstrap.css ...'
lessc site/css/custom-bootstrap.less > site/css/bootstrap.css
echo 'Generating bootstrap.min.css ...'
lessc --compress site/css/custom-bootstrap.less > site/css/bootstrap.min.css

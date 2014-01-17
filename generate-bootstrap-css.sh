#!/bin/sh
echo ''
echo 'Generating bootstrap.css ...'
lessc css/custom-bootstrap.less > css/bootstrap.css
echo 'Generating bootstrap.min.css ...'
lessc --compress css/custom-bootstrap.less > css/bootstrap.min.css

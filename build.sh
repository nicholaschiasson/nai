#!/usr/bin/env sh

rm -rf bin
cp -rf src bin
python -m compileall bin
python -OO -m compileall bin
find bin -name *.py | while read f; do rm $f; done
tar czf bin/nai.tgz -C bin nai

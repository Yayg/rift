#! /bin/sh

for file in `ls Unit_Tests/*.py`; do
    coverage run $file;
done

for file in `ls Acceptance_Tests/*.py`; do
    coverage run $file;
done

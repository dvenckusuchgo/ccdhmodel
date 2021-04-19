#!/bin/bash
#
#   gen_markdown.sh - run linkml gen-markdown on model files, then build site with mkdocs
#

PARMS="--no-mergeimports"

echo "Begin gen_markdown.sh..."

# Confirm pipenv install has run.
bash ./install_env.sh

echo "Cleanup existing model docs."
for modeldir in `ls -d docs/*/`; do
    # DO NOT DELETE docs/hooks directory; we need it.
    if [[ $modeldir != *"docs/hooks"* ]]; then
        rm -fr $modeldir
    fi
done
rm -f ./docs/index.md

echo "Cleanup site files."
rm -fr ./site/* 

echo "Generating Markdown."
for filename in model/*.yaml; do
    basename=$(basename -- "$filename")
    BASE="${basename%.*}"
    BASEDIR=docs/`python -c "print(\"$BASE\".capitalize())"`
    echo Generating $filename
    mkdir -p $BASEDIR
    pipenv run gen-markdown $PARMS model/$BASE.yaml -d $BASEDIR --log_level INFO
done

echo "Generate mkdocs website."
pipenv run mkdocs build


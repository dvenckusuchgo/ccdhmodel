#!/bin/bash
#
#   gen_markdown.sh - run linkml gen-markdown on model files, then build site with mkdocs
#


PARMS="--no-mergeimports"

echo "Cleanup existing model docs"
for modeldir in `ls -d docs/*/`; do
    # DO NOT DELETE docs/hooks directory
    if [[ $modeldir != *"docs/hooks"* ]]; then
        rm -fr $modeldir
    fi
done
rm -f ./docs/index.md

echo "Cleanup site files"
rm -fr ./site/* 

echo "Generate Markdown"
for filename in model/*.yaml; do
    basename=$(basename -- "$filename")
    BASE="${basename%.*}"
    BASEDIR=docs/`python -c "print(\"$BASE\".capitalize())"`
    echo Generating $filename
    mkdir -p $BASEDIR
    pipenv run gen-markdown $PARMS model/$BASE.yaml -d $BASEDIR --log_level INFO
done

pipenv run mkdocs build

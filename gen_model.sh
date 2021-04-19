#!/bin/bash
#
#   gen_model.sh - generates models for: python, jsonld, jsonld-context, json-schema
#

echo "Begin gen_model.sh..."

# Make sure pipenv install has been run
INSTALLED=$(pipenv run pip list | grep linkml)
if [ -z "$INSTALLED" ]; then
    echo "'pipenv install' has not run.  Installing now."
    pipenv install
fi

echo "Generating output from models."

PARMS="--no-mergeimports"
for filename in model/*.yaml; do
    basename=$(basename -- "$filename")
    BASE="${basename%.*}"
    echo Generating $filename
    # PARMS="--no-mergeimports" triggers an error in gen-pythong
    pipenv run gen-python model/$BASE.yaml > python/$BASE.py --log_level INFO
    pipenv run gen-jsonld $PARMS model/$BASE.yaml > jsonld/$BASE.jsonld 
    pipenv run gen-jsonld-context $PARMS model/$BASE.yaml > jsonld/$BASE.context.jsonld 
done
pipenv run gen-json-schema $PARMS model/entities.yaml > json-schema/entities.json 
pipenv run gen-jsonld-context $PARMS model/prefixes.yaml > includes/prefixes.context.jsonld 

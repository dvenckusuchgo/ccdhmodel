# CCDH Models in LinkML

## Documentation:

* [Model Documentation](https://cancerdhc.github.io/ccdhmodel/)

* [Talk on the CCDH Data Harmonization Workstream meeting](https://docs.google.com/document/d/13PMvYlstQ9BNr_Br1HzZ9n7etkz5nCKxp_RbF0cL4n0)


## Automated generation of YAML

* The model yaml files are programmatically generated from the [Google Sheet](https://docs.google.com/spreadsheets/d/1oWS7cao-fgz2MKWtyr8h2dEL9unX__0bJrWKv6mQmM4/)

* The code that [generates the yamls](https://github.com/HOT-Ecosystem/crdc-node-models/tree/master/ccdh/model)

## Gen Models from the Yamls
From the main directory, run ```gen_model.sh```

## Build a ReadTheDocs Site

* From the project main directory, run ```gen_markdown.sh```
* LinkML will generate the required markdown in the docs/ directory.
* Mkdocs will generate the website docs using the markdown files from the previous step.
* The new ReadTheDocs site will be built in the site/ directory.
* Access the new website with the webserver of your choice.

#### Changes from the original cancerDHC/ccdhmodel

* switched biolinkml --> linkml
* split ```gen-markdown``` out from ```gen_model.sh``` into it's own script ```gen_markdown.sh```
* enhanced ```mkdocs build``` with plugins to customize website output

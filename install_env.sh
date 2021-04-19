#!/bin/bash
#
#  install_env.sh
#

# Make sure pipenv install has been run
BIOLINKML=$(pipenv run pip list | grep biolinkml)
if [ ! -z "$BIOLINKML" ]; then
    echo "'biolinkml (deprecated) has been detected. Removing."
    pipenv uninstall biolinkml
    # make sure the latest packages are installed
    pipenv install
fi
INSTALLED=$(pipenv run pip list | grep linkml)
if [ -z "$INSTALLED" ]; then
    echo "'pipenv install' has not run.  Installing now."
    pipenv install
fi
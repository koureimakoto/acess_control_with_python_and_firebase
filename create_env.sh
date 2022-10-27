#!/usr/bin/env bash

# PIP_CURR_VERSION='22.1.2'
# PYREBASE_CURR_VERSION='5.0.1'
# FIREBASE_CURR_VERSION='3.0.1'
# FIREBASE_ADMIN_CURR_VERSION='6.0.1'

# Busca saber se o Python 3 está disponível Virtual Env
W_PYTHON="$(which python3)"
PY_REGEX='((?![\s\S])*\b(env|python3)\w*\b)'
if [[ $(echo -n $W_PYTHON | grep --only-matching --extended-regexp "$PY_REGEX") =~ $(echo -e "env\npython3") ]];
then
    echo 'Pythos is already in VENV'   
else 
    exit 1
fi

# Busca saber se o Pip3 está disponível no Virtual Env
W_PIP="$(which pip3)"
PIP_REGEX='((?![\s\S])*\b(env|pip3)\w*\b)'
if [[ $(echo -n $W_PIP | grep --only-matching --extended-regexp "$PIP_REGEX") =~ $(echo -e "env\npip3") ]];
then
    echo 'Pip is already in VENV'   
else 
    exit 1
fi

# Busca saber se o Pip3 já possuí essa dependência instalada
PIP_SHOW_PYREBASE="$(pip3 show pyrebase5)"
PYREBASE_REGEX='((?![\s\S])*pyrebase5)'
if [[ $(echo -n $PIP_SHOW_PYREBASE | grep --only-matching --extended-regexp "$PYREBASE_REGEX") =~ $(echo -e "pyrebase5") ]];
then
    echo 'Pyrebase is already in VENV:Pip3'   
else 
    exit 1
fi

#pip3 install firebase firebase_admin pyrebase5
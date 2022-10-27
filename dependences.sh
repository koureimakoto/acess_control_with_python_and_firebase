"""
#!/usr/bin/env bash

# Versão das atuais dependência
PIP_CURR_VERSION='22.1.2'
PYREBASE_CURR_VERSION='5.0.1'
FIREBASE_CURR_VERSION='3.0.1'
FIREBASE_ADMIN_CURR_VERSION='6.0.1'

PIP_CURR_VERSION_SIZE=${#PIP_CURR_VERSION}
PYREBASE_CURR_VERSION_SIZE=${#PYREBASE_CURR_VERSION}
FIREBASE_CURR_VERSION_SIZE=${#FIREBASE_CURR_VERSION}
FIREBASE_ADMIN_CURR_VERSION_SIZE=${#FIREBASE_ADMIN_CURR_VERSION}

# Dependência para instalação de projeto
VERSION_PIP=$(pip3 --version)
VERSION_PYREBASE=$(pip3 show pyrebase5)
VERSION_FIREBASE=$(pip3 show firebase )
VERSION_FIREBASE_ADMIN=$(pip3 show firebase_admin)

PIP_REGEX='^[0-9]{2,}\.[0-9]{1,2}\.[0-9]{1,3}$'


# Trata o retorno da versão do Pip
for s in $VERSION_PIP; do 
    [[ $s =~ $PIP_REGEX ]] && REGEX_RESULT=$?;
    
    if [[ $REGEX_RESULT == 0 ]]; 
    then
        VERSION_PIP=${s}
        break
    fi
done

if [[ $VERSION_PIP =~ $PIP_CURR_VERSION ]];
then
    echo $VERSION_PIP
fi
"""
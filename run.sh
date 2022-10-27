#!/usr/bin/env bash

# Verifica se o Virtual Env está ativado, se não estiver ele ativa em outra janela
ACW_PY_FB_PATH=$(dirname $(realpath $0))
if [[ -s $VIRTUAL_ENV ]]; then
    echo $VIRTUAL_ENV  
else
    gnome-terminal -- bash -c "source $ACW_PY_FB_PATH/env/bin/activate; exec $SHELL -i;"
fi

# Ativado ele executa o script
exec "./src/__main__.py"
from enum     import Enum
from typing   import Literal
from auth     import User
from platform import platform
import subprocess


class Terminal(Enum):
    CLS  : Literal['cls']   = 'cls'
    CLEAR: Literal['clear'] = 'clear'


def create_user(user: User) -> bool:
    """
    Operações de Criar um Novo usuário 
    """
    pass


def update_user(user: User) -> bool:
    """
    Operações para Atualizar informações do usuário
    """
    pass

def delete_user(user: User) -> bool:
    """
    Operações para Deletar definitiva o usuário
    @@ Verificar se é possivel deletar em dois fatores
    @@ ou talvez pedindo para ele redigitar o e-mail e
    @@ para forçar a decisão
    """
    pass

def verify_user(user: User) -> bool:
    """
    Operações que retorna se u usuário está ou não
    cadastrado e caso não esteja retorna o usuário
    retorna menu inicial.
    """
    pass

def char_to_int( char: str ) -> int | bool:
    """
    Converte com mais segurança char para int sem
    quebrar o sistem
    """
    try:
        num = int(char)
        return num
    except:
        print('Verifique se digiou apenas números.')
        return False


# Manipulador do terminal
def clear_terminal():
    """
    Limpa o terminal para não crescer infinitamente
    """
    if platform.system() == "Windows":
        # Apenas Windows
        subprocess.Popen(Terminal.CLS  ,   shell=False).communicate() 
    else: 
        #Linux and Mac
        subprocess.Popen(Terminal.CLEAR, shell=False).communicate() 

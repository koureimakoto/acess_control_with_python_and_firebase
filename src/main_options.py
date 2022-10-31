from enum     import Enum
from ssl import _PasswordType
from turtle import update
from typing   import Literal
from auth     import User
from platform import platform
import subprocess


class Terminal(Enum):
    CLS  : Literal['cls']   = 'cls'
    CLEAR: Literal['clear'] = 'clear'


def create_user(user: User) -> bool:
    
    print("Criar novo usuario\n")
    email = input("Digite o Email: ")
    password = input("Digite a Senha: ")
    password_conf = input("Confirme a Senha: ")
    
    if password == password_conf:
        user.create_user_with_email_and_password(email, password)
        print("Usuário criado.")
        return True

    else:
        print("Senhas não correspondem, tente novamente.\n")
        create_user(user)

def update_user(user: User) -> bool:
    update_password = input("Deseja alterar a senha?(S/N)\n").upper()
    if update_password == "S":
        user.send_password_reset_email(user.get_email)
        return True
    else:
        "Operação cancelada."
        return False

def delete_user(user: User) -> bool:
    """
    Operações para Deletar definitiva o usuário
    @@ Verificar se é possivel deletar em dois fatores
    @@ ou talvez pedindo para ele redigitar o e-mail e
    @@ para forçar a decisão
    """
    user_delete = input("Deseja deletar o usuario?(S/N)\n").upper()
    if user_delete == "S":
        user.delete_user_account(user.get_id_token())
        return True
    else:
        "Operação cancelada."
        return False
    

def verify_user(user: User) -> bool:
    """
    Operações que retorna se o usuário está ou não
    cadastrado e caso não esteja retorna o usuário
    retorna menu inicial.
    """
    if user.get_email_verification:
        return True
    else:
        return False

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

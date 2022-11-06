from   auth  import User
import platform
import subprocess
import email_verification


def create_user(user: User) -> bool:
    
    print("Criar novo usuario: ")
    email: str =  input("Digite o Email: ")

    # Chamar uma função dentro da outra como estava gera chamada recursiva, dificil de
    # de Debugar e achar erros.
    while True:
        password_first : str = input("Digite a Senha: ")
        password_second: str = input("Confirme a Senha: ")
        if password_first == password_second:
            if not user.create_new_user(email, password_first): 
                clear_terminal()
                print('Não foi possivel registar, ou ja esta registrado')
                return False
            clear_terminal()
            print("Usuário criado.\n")
            return True
        clear_terminal()
        print("Senhas não correspondem, tente novamente.\n")

# def update_user(user: User) -> bool:
#     while True:
#         update_password = input("Deseja alterar a senha?(S/N)\n").upper()
   
#         if update_password == 'S':
#             return False

#         email: str = 'talles@text.com' # input("Digite o Email: ")

#         password_old : str = '!Qa1234567'  # input("Digite a Senha: ")
#         password_new: str =  '!Qa12345682'  # input("Confirme a Senha: ")
    
#         if user.update_password(email, password_old, password_new):
#             return True
#         print("Erro ao alterar a senha. Verifique seu STATUS\n")

# def delete_user(user: User) -> bool:
#     """
#     Operações para Deletar definitiva o usuário
#     @@ Verificar se é possivel deletar em dois fatores
#     @@ ou talvez pedindo para ele redigitar o e-mail e
#     @@ para forçar a decisão
#     """
#     user_delete = input("Deseja deletar o usuario?(S/N)\n").upper()
#     if user_delete == "S":
#         try:
#             firebase.auth().delete_user_account(user.get_id_token())
#             return True
#         except:
#             print("Erro ao alterar a deletar o usuario. Verifique seu STATUS\n")
#             verify_user(user)

#     else:
#         "Operação cancelada."
#         return False
    

def get_user(user: User) -> bool | User:
    """
    Operações que retorna se o usuário está ou não
    cadastrado e caso não esteja retorna o usuário
    retorna menu inicial.
    """
    
    email   : str = input("Digite o Email: ")
    password: str = input("Digite a Senha: ")
    if user.get_registed_user(email, password):
        clear_terminal()
        print("Status da Sessão: ATIVO")
        return True
    clear_terminal()
    print("Status da Sessão: INATIVO")
    return False 


def verify_user(user: User) -> bool:
    """
    Operações que retorna se o usuário está ou não
    cadastrado e caso não esteja retorna o usuário
    retorna menu inicial.
    """
    email    : str = input("Digite o Email: ")
    password : str = input("Digite a Senha: ")
    
    if not user.get_registed_user(email, password):
        print('Usuario não registrado')
        return False

   
    if not user.get_email_verification():
        print('Verificação de dois fatores')

        email_fmt = email_verification.UserEmailVerification()
        email_fmt.mail_to('auldghjvgigcgzjgdf@tmmbt.net')

        conn = email_verification.SMTPConn()
        conn.send(email_fmt)

        code = input('Digite o numero que está em seu e-mail: ')
        if  email_fmt.check_rand_number(code):
            print('Você está autenticado')
            return True
        return False

    print("Não foi possivel verificar")
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
        subprocess.Popen('cls'  ,   shell=False).communicate() 
    else: 
        #Linux and Mac
        subprocess.Popen('clear', shell=False).communicate() 

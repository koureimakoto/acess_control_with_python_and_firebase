#!/usr/bin/env python3
from auth import User
import main_options

"""
Como Usar:

    Primeiro importar o arquivo 'auth' para acessar a classe 'User'
    Você pode acessar de duas formas

        '
        import auth
        
        user = auth.User(NONE)
        
        '-> Essa primeira parte importa tudo que existe em Auth

        -- OU --

        '
        from auth import User

        user = User(NONE)
        
        '-> Dessa forma importará apenas a classe User


        A classe User possuí algums métodos Publicos, que são 
        funções dentro  da classe que você pode executar fora
        dela. E quase todos seus dados são ReadyOnly, que não
        permite  sobrescrever uma vez  escritos. Sendo  todos 
        dados privados Privados, isto é, para acessar estes a
        qualquer momento é  necessário invocar metódos que os 
        retornaram, claro  só os que  não comprometam a inte-
        gridade dos dados da classe.

"""

def main() -> bool:
    # Fazer codigos de teste iniciar e testar aqui
    # email: str = 'urusai@gmail.com'
    # passwd:str = '##$Cachorrada#Anonima'
    # user_test = User()

    # print( 'Email is   : ' , user_test.check_email(email)  )
    # print( 'Password is: ' , user_test.check_passwd(passwd))
    # print()

    # if user_test.create_new_user(email, passwd):
    #     print(user_test)
    # elif user_test.get_registed_user(email, passwd): 
    #     print(user_test)
    #     print('This e-mail is verified: ', user_test.get_register_state(), '\n')
    # else:
    #     return False

    print('Seja bem vindo ao nosso Protópico de Cadastro e Verificação')
    print('de E-mail usando o Firebase.')
    print(' - Primeiramente, começaremos de um modo muito simples, Ok?')

    user: User = User()
    while True:
        print(' - Escolha um das opções abaixo usando o "teclado numérico"')
        print(' - - 1: Verificar Situação do seu Cadastro\n'              \
              ' - - 2: Se não foi cadastrado ainda, cadastrar-se agora\n' \
              ' - - 3: Alterar sua seu e-mail ou senha\n'                 \
              ' - - 4: Deletar meu dados\n'                               \
              ' - - 0: para encerrar a aplicação\n')

        option: str = input('Digite sua opção --> ')

        # Limpa o terminal toda vez antes de entrar em uma opção
        main_options.clear_terminal()
        match option:
            case '1':
                main_options.verify_user(user)
                pass
            case '2':
                main_options.create_user(user)
                pass
            case '3':
                main_options.update_user(user)
                pass
            case '4':
                main_options.delete_user(user)
                pass
            case '0':
                print('Adeus querido ou querida')
                pass
            case   _:
                print('Não é uma opção válida!!')

    # Final
    return True

if __name__ == '__main__':
    result: bool = main()
    if result:
        print('Isso ai manolo')
        quit()
    print('ai ai ai ai ai, Zordon')
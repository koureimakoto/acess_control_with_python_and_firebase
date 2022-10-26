import pyrebase, firebase_config, re
from   typing              import Any
from   requests.exceptions import HTTPError


# ----------   class User    ----------
class User(HTTPError):
    """
    Classe para armazenar registros de um novo usuário, alterações
    ou guardar dados para manipulção

    Construtor dela é vazio

    user = User()

    """

    # ----------    __init__     ----------
    def __init__(self) -> None:
        super().__init__()

        self.__status    : dict[str, Any] = {}
        self.__info      : dict[str, Any] = {}

        self.__email     : str  = ''
        self.__token     : str  = ''
        self.__registered: bool  = False
        self.__error       : HTTPError = HTTPError()

    # ---------- create_new_user ----------
    def create_new_user(self, email: str, passwd: str ) -> bool:
        """
        Wrapper das funções de criação cria um novo usuário com verificação

        create_new_user:
            >> e-mail: String   # Qualquer tipo de e-mail que atendas formato de um\n
            >> passwd: String   # O password digitado pelo usuário\n
            << Boolean          # Se tudo correr bem, retorna Verdadeiro\n
        """
  
        # Verifica antecipadamente se o e-mail esta formatado corretamentes antes
        # da requisição para o server do Firebase.
        if self.check_email(email) and self.check_passwd(passwd):

            # Tenta criar um novo usuário
            try:
                firebase = pyrebase.initialize_app(firebase_config.firebaseConfig)
                # Registra os dados requisitados
                self.__set_response(
                    firebase.auth().create_user_with_email_and_password(email, passwd)
                )
                return True
            except HTTPError as e:
                self.__error = e
                return False
        print('Verify is your e-mail our password are correct!')
        return False

    # ----------  get_sign_user  ----------
    def get_registed_user(self, email: str, passwd: str) -> bool:
        """
        Verifica e retornar um usuário já cadastrado e um wrapper da mesma
        função nativa no Firebase.
    
        create_new_user:
            >> e-mail: String   # Qualquer tipo de e-mail que atendas formato de um\n
            >> passwd: String   # O password digitado pelo usuário\n
            << Boolean          # Se tudo correr bem, retorna Verdadeiro
        """

        if self.check_email(email) and self.check_passwd(passwd):

            # Tenta criar retornar um usuário já cadastro
            try:
                firebase = pyrebase.initialize_app(firebase_config.firebaseConfig)

                # Registra os dados requisitados
                self.__set_response(
                    firebase.auth().sign_in_with_email_and_password(email, passwd)
                )
                return True
            # implementar outros except
            except HTTPError as e:
                self.__error = e
                return False
        print('Verify is your e-mail our password are correct!')
        return False

    # ----------   check_email   ----------
    def check_email(self, email: str):
        """
        Verifica o e-mail atraves de expressão regular antes de um resquest para o Firebase

        check_email:
            >> email: String   # Qualquer tipo de e-mail que atendas formato de um\n
            << Boolean
        """
        return re.findall(r'[\w\.-]+@[\w\.-]+\.[\w]+', email) and len(email) < 256

    # ----------  check_passwd   ----------
    def check_passwd(self, passwd: str) -> bool:
        """
        Verifica se o password possuí alphanérico case caixa alta, baixa e simbolos
        entre 8 a 20 caracteres

        check_email:
            >> passwd: String   # Toda senha que segue a regra acima\n
            << Boolean
        """
        # ^  -> Inicio de Linha
        # (?=.*?[aA0-9Zz])    -> Busque 0 ou qalquer valor entre [a-z][A-Z][0-9]
        # (?!.*?[\ \n\r\t])   -> Ignore qualquer espaço branco 
        # (?=.*?[#?!@$%^&*-]) -> Busque 0 ou qalquer valor entre [ dentro dos colchetes ]
        # .{8, 100}$          -> minimo 8 máximo 100
        # $  -> Encerre no final da linha 
        return re.findall(r'^(?=.*?[a-zA-Z0-9])(?!.*?[\ \r\t])(?=.*?[#?!@$%^&*-]).{8,}$', passwd) != []
    
    # ----------    get_email    ----------
    def get_email(self) -> str:
        """
        Torna o e-mail registrado da classe 

        get_email:
            << email: str
        """
        return self.__email

    # ------ get_email_verification -------
    def get_email_verification(self):
        """
        Retorna o estado, se o e-mail foi verificado ou não.

        get_email_verification:
            << info['emailVerificied']
        """
        firebase = pyrebase.initialize_app(firebase_config.firebaseConfig)
        self.__set_info(firebase.auth().get_account_info(self.get_id_token())['users'][0])
        return self.get_info()['emailVerified']

    # ----------   __id_token    ----------
    def get_id_token(self) -> str:
        """
        Mantem reservado o token de autenticação ao invés da senha.

        get_id_token:
            << status[''idToken]

        """
        return self.__token

    # ----------    get_error    ----------
    def get_error(self) -> None:
        """
        Retorna o tipo de erro de conexão

        Ainda em implementação básica

        get_error:
            << self.__error: dict
        """
        return self.__error

    # -------- get_register_state ---------
    def get_register_state(self) -> str :
        """
        Retorna o estado do cadastro

        is_registered:
            << boolean
        """
        return self.__registered

    def get_status(self):
        """
        Função temporário para obter o status completo
        
        get_status:
            << self.__status: dict
        """
        return self.__status

    def get_info(self):
        """
        Função temporário para obter o info completo

        get_info:
            << self.__info: dict
        """
        return self.__info

    # ---------- __set_response  ----------
    def __set_response(self, auth) -> None:
        """
        Prepara todos os dados importantes para serem armazenados na class

        __set_response[private]
            >> auth: firebase.Auth   # Os dados do resquest ao Firebase\n
            << None
        """
        self.__set_status(auth)
        self.__email     = auth['email'     ]
        self.__token     = auth['idToken'   ]
        self.__registered= True

    def __set_status(self, status: dict[str, Any]):
        """
        Função que seta temporariamento o status
        """
        self.__status = status

    def __set_info(self, info: dict[str, Any]):
        """
        Função que seta temporariamento o info
        """
        self.__info = info


    def print_error(self) -> None:
        """
        Imprime diretamente o o erro da classe.
        """
        print(self.__error)


    # ----------     __str__     ----------
    def __str__(self) -> str:
        return 'User e-mail: ' + self.get_email() + '\nRegistered : ' + str(self.get_register_state()) 

        

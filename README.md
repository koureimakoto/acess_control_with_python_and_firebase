# Mecanismo de Controle de Acesso com Autenticação de Dois Fatores em Firebase

### Para iniciar:

**Componentes**  
> Python3.10
> Firebase3.0.1
> Pyrebase5
> Firebase_admin6.0.1

**Instalação**
```bash
# chmod 755 ./__main__.py
```
```bash
$ pip3 install firebase firebase_admin pyrebase5 
```

**Execução**
```bash
$ ./__main__.py 
```  
---
**Dentro do __main__.py**

```py
def main():
	# Executar os código dentro desta função	
	...
	# final
	return True


if __name__ == '__main__':
	# Caso queria testar o final do main
	result: bool = main()
```

**Classes disponíveis**
```py
	# User -> Para armazenar os dados e forma imutável depois da primeira 
	# inserção nos atributos privados.
	class User:
		def:
			__init__
				>> self
				<< None

			# Wrapper de funções do Firebase
			create_new_user
				>> email : str
				>> passwd: str
				<< bool
			
			get_registed_user
				>> email : str
				>> passwd: str
				<< bool
			# -- end --

			# verificadores de segurança
			check_email
				>> email : str
				<< bool

			check_passwd
				>> passwd: str
				<< bool
			# -- end --

			# getters
			get_email
				<< self.__email: str

			get_email_verification
				<< email_verified: str

			# unsafe
			get_id_token
				<< self.__id_token: str
				
			get_error
				<< self.__error: HTTPError

			get_register_state
				<< self.__registered: bool
			# -- end --

			__str__
				<< fmt + self.get_email + fmt + get_registerd_user + fmt: str
```

```py
	# TwoFactoryVerification -> Classe para manipular a verificação do e-mail
	class TwoFactoryVerification:
		def __init__
			>> User: class
			<< None
		...
```


```py
	# FirebaseFiles -> Classe para manipular a verificação do e-mail
	class FirebaseFiles:
		def __init__
			pass
		...
```
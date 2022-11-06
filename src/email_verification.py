import random
from smtplib import SMTP

from email.mime.multipart import MIMEMultipart
from email.mime.text      import MIMEText

class UserEmailVerification:
    def __init__(self) -> None:

        self.__uemail : str = ''
        self.__upasswd: str = ''

        self.__rand   : str = ''
        self.__message: MIMEMultipart
        self.__email_from: str = ''
        self.__email_to  : str = ''
        self.__email_subj: str = 'Numero de verificação'
        self.__email_body: str = str(random.randrange(100000, 999999))

        self.__email_states: dict[str, bool] = {
            'email_from'   : False,
            'email_to'     : False,
            'email_subject': False,
            'email_body'   : False,
        }

    
    def sender(self, email, passwd):
        self.__uemail : str = email
        self.__upasswd: str = passwd


    def mail_from(self, email):
        if self.empty(email):
            self.__email_from = email
            self.__email_states['email_from'] = True
        return self
        
    def mail_to(self, email):
        if self.empty(email):
            self.__email_to = email
            self.__email_states['email_to'] = True
        return self

    def subject(self, subj):
        if self.empty(subj):
            self.__email_subj = subj
            self.__email_states['email_subject'] = True
        return self

    def body(self, body):
        if self.empty(body):
            self.__email_body = body
            self.__email_states['email_body'] = True
        return self

    def empty(self, text):
        return text != ''

    def get_message(self) -> MIMEMultipart:
        return self.__message

    def get_user_email(self):
        return self.__uemail

    def get_user_password(self):
        return self.__upasswd

    def check_rand_number(self, rand: int):
        return self.__email_body == rand

    def wrap(self):
        for state in self.__email_states:
            if  not self.__email_states[state]:
                print( f'{state}: vazio', )
                return self.__email_states[state]

        self.__message = MIMEMultipart()
        self.__message['From']    = self.__email_from
        self.__message['To']      = self.__email_to
        self.__message['Subject'] = self.__email_subj
        self.__message.attach(
            MIMEText( self.__email_body, 'plain')
        )


class SMTPConn():
    def __init__(self):
        self.__server : str = 'smtp.gmail.com'
        self.__port   : int = 587

    def send(self, user: UserEmailVerification):
        
        conn = SMTP(self.__server, self.__port)
        conn.starttls()
        conn.login(
            user.get_user_email(),
            user.get_user_password()
        )
        conn.send_message(user.get_message())
        conn.quit()
    

# email_fmt = UserEmailVerification('urusaidenoite@gmail.com', 'bumfwllmhnpvzuct')

# email_fmt.mail_from('urusaidenoite@gmail.com').mail_to('urusaidenoite@gmail.com').wrap()


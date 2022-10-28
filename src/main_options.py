
def create_user() -> bool:
    pass

def update_user() -> bool:
    pass

def delete_user() -> bool:
    pass

def verify_user() -> bool:
    pass

def char_to_int( char: str ) -> int | bool:
    try:
        num = int(char)
        return num
    except:
        print('Verifique se digiou apenas números.')
        return False
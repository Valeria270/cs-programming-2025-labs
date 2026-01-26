def check_password_strength(password):
    errors = []
    if len(password) < 8:
        errors.append("длина менее 8 символов")
    if not any(char.isupper() for char in password):
        errors.append("отсутствуют заглавные буквы")
    if not any(char.islower() for char in password):
        errors.append("отсутствуют строчные буквы")
    if not any(char.isdigit() for char in password):
        errors.append("отсутствуют числа")
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?`~"
    if not any(char in special_chars for char in password):
        errors.append("отсутствуют специальные символы")
    
    return errors

def main():
    password = input("Введите пароль: ")
    
    errors = check_password_strength(password)
    
    if errors:
        error_message = ", ".join(errors)
        print(f"Пароль ненадежный: {error_message}")
    else:
        print("Пароль надежный!")

if __name__ == "__main__":
    main()
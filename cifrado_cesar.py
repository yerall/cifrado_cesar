
def encrypt_caesar(text, shift=1):
    # Inicializa el texto encriptado
    cipher = ''
    for char in text:
        # Si el carácter no es alfabético, se agrega directamente
        if not char.isalpha():
            cipher += char
            continue
        # Convierte el carácter a mayúscula
        char = char.upper()
        # Desplazamiento de carácter
        code = ord(char) + shift
        # Ajuste en caso de superar 'Z'
        if code > ord('Z'):
            code -= 26  # Vuelve al inicio del alfabeto
        cipher += chr(code)
    return cipher


def decrypt_caesar(cipher, shift=1):
    # Inicializa el texto desencriptado
    text = ''
    for char in cipher:
        # Si el carácter no es alfabético, se agrega directamente
        if not char.isalpha():
            text += char
            continue
        # Convierte el carácter a mayúscula
        char = char.upper()
        # Desplazamiento de carácter inverso
        code = ord(char) - shift
        # Ajuste en caso de ser menor a 'A'
        if code < ord('A'):
            code += 26  # Vuelve al final del alfabeto
        text += chr(code)
    return text

# Encriptar un mensaje
mensaje = "Soy el mensaje de ejemplo"
mensaje_encriptado = encrypt_caesar(mensaje, shift=3)
print("Mensaje encriptado:", mensaje_encriptado)  # TPZ FM NFOTBKF EF FKFNQMP

# Desencriptar el mensaje
mensaje_desencriptado = decrypt_caesar(mensaje_encriptado, shift=1)
print("Mensaje desencriptado:", mensaje_desencriptado)  # SOY EL MENSAJE DE EJEMPLO

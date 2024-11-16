# Descripción

Este es un programa en Python que implementa el cifrado César, un cifrado de sustitución simple en el que cada letra del texto original se reemplaza por otra que se encuentra un número fijo de posiciones más adelante en el alfabeto. Este método de cifrado es uno de los sistemas más antiguos y sencillos de encriptación.

El programa hace uso de dos funciones principales:

1. `encrypt_caesar(text, shift=1)`: Encripta un mensaje desplazando cada letra un número de posiciones determinado en el alfabeto.
2. `decrypt_caesar(cipher, shift=1)`: Desencripta un mensaje encriptado con el cifrado César, desplazando cada letra hacia atrás por el mismo número de posiciones.

Ambas funciones permiten especificar el desplazamiento (o "shift") deseado, por defecto igual a 1. Esto permite probar cifrados con diferentes desplazamientos, lo que aumenta la flexibilidad del código.

## Requisitos

Este programa solo requiere tener Python 3 instalado.

## Ejemplo de resultado

```shell
Ingresa tu mensaje: AVE CAESAR
Mensaje encriptado: BWF DBFTBS

Ingresa tu criptograma: BWF DBFTBS
Mensaje desencriptado: AVE CAESAR
```

## Personalización del Desplazamiento

El parámetro `shift` en las funciones permite especificar el número de posiciones para el desplazamiento en el cifrado. Por ejemplo, si `shift=3`, cada letra será desplazada tres posiciones adelante en el alfabeto.

```python
mensaje = "Soy el mensaje de ejemplo"
mensaje_encriptado = encrypt_caesar(mensaje, shift=3)
print("Mensaje encriptado con shift=3:", mensaje_encriptado)
# Salida: "VRB HO PHQVDMH GH HMHPSOR"
```

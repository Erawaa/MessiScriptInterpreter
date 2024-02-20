# MessiScript
***MessiScript*** es un lenguaje de programación esotérico en el que cada código es una jugada de Messi. Está inspirado en Brainfuck y en Shakespeare Programming Language (SPL).

## Elementos fundamentales

MessiScript usa una lista de números, una posición y un portapapeles.

- **Lista**: Es una lista de variables. La primera posición es la que más a la izquierda se encuentra, siendo las posiciones siguientes las ubicadas a su derecha. Se puede acceder a ellas cambiando la posición en uno. A cada una de las posiciones de la lista se le pueden asignar valores numéricos enteros. Comienzan todas en cero.
- **Posición**: Indica la posición de la lista en la que el programa se encuentra.
- **Portapapeles**: Es una variable en la que se puede copiar el valor de la posición actual de la lista, o viceversa.

## Syntaxis

La syntaxis de MessiScript es muy básica. Todo código se compone de comandos separados por puntos (.). El código se ejecuta de forma secuencial, y pueden haber bucles de comandos.

### Comandos

Existen 14 comandos, que se detallan a continuación:

- **la agarra messi**: Indica el comienzo del código.
- **¡gol!**: Indica el final del código.
- **va messi**: Asigna un valor a la posición actual de la lista. Es el único comando que además necesita que se le pase un parámetro. Es una oración que permite determinar el valor que se asignará.
- **encara messi (o ankara messi)**: Asigna un cero a la posición actual de la lista.
- **la mueve messi por la derecha**: Cambia la posición a la derecha.
- **la mueve messi por la izquierda**: Cambia la posición a la izquierda.
- **juega messi**: Muestra por pantalla el número de la posición actual de la lista.
- **la pisa messi**: Muestra por pantalla el caracter correspondiente en UNICODE al número de la posición actual de la lista.
- **siempre messi**: Toma un input numérico del usuario, y lo guarda en la posición actual de la lista. Si el input no es un número entero, se ignora.
- **gambetea messi**: Toma un input del usuario, y guarda el número correspondiente en UNICODE al primer caracter que se ingresa.
- **sigue messi**: Si la posición actual es cero, se saltea todos los comandos hasta encontrarse un "*vuelve messi*". Si no lo es, ejecuta los comandos hasta encontrarse con un comando "*vuelve messi*" y luego vuelve al comando. Una vez que vuelve, corrobora de vuelta el valor de la posición actual, y actúa de la misma forma.
- **vuelve messi**: Indica el final de un bucle de comandos iniciado por un comando "*sigue messi*".
- **corre messi**: Copia el contenido de la posición actual de la lista al portapapeles.
- **amaga messi**: Copia el contenido del portapapeles a la posición actual de la lista.

### Asignación de valores

El comando "*va messi*" necesita que se le pase una oración para asignar valores a la posición actual de la lista. Las palabras de la oración cambian ese valor de la siguiente forma:

- **Sustantivos**: Suman uno a la posición actual de la lista.
- **Adjetivos**: Multiplican por dos a la posición actual de la lista.
- **"fútbol"**: Cambia el signo de la posición actual de la lista.

*NOTA*: Es destacable que si el valor que se quiere modificar es negativo, al usar un sustantivo, se le suma un uno de igual forma. Es decir, si se tiene "-27" y se usa un sustantivo, se pasa a "-26".

Los sustantivos y adjetivos que se tienen en cuenta están detallados en [*words.py*](https://github.com/Erawaa/MessiScriptInterpreter/blob/main/words.py). Las palabras que no estén en ese archivo, son ignoradas.

# MessiScriptInterpreter
Intérprete de MessiScript escrito en Python.

## ¿Cómo lo uso?
Para usarlo es necesario tener instalado Python. Se instala muy facilmente desde su página oficial, y se puede instalar en Linux, Windows y MacOS. Luego, se pueden seguir los siguientes pasos:

1. Descargar los archivos.py de este repositorio.
2. En la carpeta en la que se guarde, abrís una terminal y corrés el intérprete usando Python, escribiendo:
```
python3 msinterpreter.py [dirección del archivo a correr]
```

*Ejemplo*: python3 msinterpreter.py hola_mundo.messi.

*NOTA: Puede ser que tengas que usar "python" en vez de "python3", dependiendo de como lo instales o de tu sistema.*

# Soporte para Visual Studio Code
Le agradezco a [GiovanniSCESP](https://github.com/GiovanniSCESP) por tomarse el trabajo de hacer una extensión para Visual Studio Code llamada [MessiScript Syntax](https://marketplace.visualstudio.com/items?itemName=GiovanniSCESP.messiscript-syntax), que facilita mucho la programación en MessiScript. Agrega syntax highlighting y autocompletado de comandos, entre otras cosas. Pueden instalar la extensión directamente desde VSCode, o acceder al link anterior.

![Ejemplo de MessiScript Syntax](https://raw.githubusercontent.com/GiovanniSCESP/MessiScript-Syntax/main/img/autocompletado.gif)
![Otro ejemplo de MessiScript Syntax](https://raw.githubusercontent.com/GiovanniSCESP/MessiScript-Syntax/main/img/intro.gif)

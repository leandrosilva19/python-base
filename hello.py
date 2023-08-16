#!/usr/bin/env python3.10

"""Hello Word Multi Linguas.

Dependendo da lingua configurada no 
ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:
	
	export LANG=pt_BR

Execução:
	
	python3.10 hello.py
	ou
	./hello.py
"""
__version__ = "0.0.1"
__author__ = "Leandro Silva"
__licence__= "Unlicense"

import os

current_language = os.getenv("LANG", "pt_BR.UTF-8")[:5]

msg = "Hello, Word!"

if current_language == "pt_BR":
   msg = "Olá, Mundo!"
elif current_language == "it_IT":
   msg = "Ciao, Mondo!"
elif current_language == "es_SP":
   msg = "Hola, Mundo!"
elif current_language == "fr_FR":
   msg = "Bonjour Monde!"





print(msg)

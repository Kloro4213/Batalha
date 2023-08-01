import re

efeitotodo = "receberVida(23)"

valor = re.findall(r'\(\d*\)',efeitotodo)

print(valor)
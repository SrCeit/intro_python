import operaciones as opr, sys

print("Elementos definidos dentro del módulo de operaciones", dir(opr))
print()
print("Los módulos estandar estan en C e incoporados en el interprete (builtins), lista de módulos: \n", sys.builtin_module_names)
print()
print("Los demás módulos que podemos importar se encuentran guardados en fcheros, que se encuentran en: \n", sys.path)
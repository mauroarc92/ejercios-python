
x = 5
y = 10

es_mayor = x > y
es_igual = x == y

print(f"x es mayor que y", es_mayor)
print(f"x es igual a y", es_igual)


resultado_and = es_mayor and es_igual
resultado_or = es_mayor or es_igual

print("Resultado con 'and':", resultado_and)
print("Resultado con 'or':", resultado_or)



es_mayor_de_edad = True
tiene_identificacion = False

if es_mayor_de_edad and tiene_identificacion:
    print("Acceso permitido")
else:
    print("Acceso denegado")
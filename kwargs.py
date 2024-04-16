import unittest

database= {
    "persona1":{
        "primer_nombre": "Pablo",
        "segundo_nombre": "Diego",
        "primer_apellido": "Ruiz",
        "segundo_apellido": "Picasso",
    },
    "persona2":{
        "primer_nombre": "Pablito",
        "segundo_nombre": "Diegardo",
        "primer_apellido": "Ruizino",
        "segundo_apellido": "Picassovich",
    },
    "persona3":{
        "primer_nombre": "Pablote",
        "segundo_nombre": "Diegordo",
        "primer_apellido": "Ruizeño",
        "segundo_apellido": "Picassonenelculo",
    },
}


# *args: se maneja como lista, son los parametros sin nombre.
# **kwargs: se maneja como diccionario, devuelve la key del primer 
#           diccionario que contiene esos valores en el segundo 
#           diccionario.
def buscar_datos(*args, **kwargs):
    counter = 0
    for key, value in kwargs.items():
        for k, v in value.items():
            for arg in args:
                if arg == v:
                    counter += 1
        if counter == len(value.items()):
            return key
                


print(buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database))

class TestKwargs(unittest.TestCase):
    def test_persona1(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
        self.assertEqual(resultado, "persona1")

    def test_persona2(self):
        resultado = buscar_datos("Pablito", "Diegardo", "Ruizino", "Picassovich", **database)
        self.assertEqual(resultado, "persona2")

    def test_persona3(self):
        resultado = buscar_datos("Pablote", "Diegordo", "Ruizeño", "Picassonenelculo", **database)
        self.assertEqual(resultado, "persona3")
    
    def test_none(self):
        resultado = buscar_datos("Pablo", "Die", "Rui", "Picasso", **database)
        self.assertEqual(resultado, None)

    def test_none_2(self):
        resultado = buscar_datos("Pablo", "Rui", "Picasso", **database)
        self.assertEqual(resultado, None)

    def test_none_3(self):
        resultado = buscar_datos("Pablo", 6, "Ruiz", True, **database)
        self.assertEqual(resultado, None)

unittest.main()
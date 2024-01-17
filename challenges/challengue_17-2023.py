"""
* Crea un programa que simule el comportamiento del sombrero seleccionador del
 * universo mágico de Harry Potter.
* - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 * coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
*
 Por ejemplo, en Slytherin se premia la ambición y la astucia.
 """

# gryffindor: valor
# hufflepuff: lealtad
# ravenclaw: sabiduría
# slytherin: ambición

questions = [
    """¿Qué camino te tienta más?
    a) El camino serpenteante y cubierto de hojas a través del bosque.
    b) La calle adoquinada bordeada de edificios antiguos.
    c) El camino ancho, soleado y cubierto de hierba.
    d) El callejón estrecho, oscuro e iluminado con linternas.
    Respuesta: """,

    """Si pudieras tener algún poder, ¿Cuál elegirías?
    a) Poder de invisibilidad.
    b) Poder de cambiar la apariencia.
    c) Fuerza sobrehumana.
    d) Poder de cambiar el pasado.
    Respuesta: """,

    """¿Qué tipo de instrumento agrada más a tu oído?
    a) El tambor
    b) El piano
    c) La trompeta
    d) El violín
    Respuesta: """,

    """¿Qué es lo que más esperas aprender en Hogwarts?
    a) Secretos sobre el castillo.
    b) Transformaciones y todas las áreas de la magia.
    c) Criaturas mágicas.
    d) Maleficios.
    Respuesta: """,

    """¿Cuál de los siguientes odiarías más que la gente te llame?
    a) Cobarde
    b) Ignorante
    c) Egoísta
    d) Ordinario
    Respuesta: """
]

score = [0, 0, 0, 0]
houses = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]


def hat_selection():
    for question in questions:
        answer = input(question)

        while answer not in ["a", "b", "c", "d"]:
            print("Por favor, introduce una opción válida (a/b/c/d): ")
            answer = input(question)

        if answer == "a":
            score[0] += 1
        elif answer == "b":
            score[1] += 1
        elif answer == "c":
            score[2] += 1
        elif answer == "d":
            score[3] += 1

    print("""
¡Ha sido una decisión muy dificil!
Definitivamente estás en...""", houses[score.index(max(score))], "!!!")


hat_selection()

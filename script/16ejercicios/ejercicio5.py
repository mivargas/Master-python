"""
crear lista con el contenido de esta tabla:
            JUEGOS

accion:     aventura:           deporte:
gta         assins              fifa1
cod         crash               fifa2
pugb        prince of persia    fifa3
"""

tabla = [
    {
        "categoria": "accion",
        "juegos": ["gta", "cod", "pugb"]
    },
    {
        "categoria": "aventura",
        "juegos": ["assins", "crash", "prince of persia"]
    },
    {
        "categoria": "deporte",
        "juegos": ["fifa1", "fifa2", "fifa3"]
    }
]

for categoria in tabla:
    print(f"--------{categoria['categoria']}--------")
    for juego in categoria['juegos']:
        print(juego)
# TODO Найдите количество книг, которое можно разместить на дискете
size = 4
symbols = 25
strings = 50
pages = 100
volume = 1.44

allBooks = (volume * 1024 * 1024) // (size * symbols * strings * pages)
print("Количество книг, помещающихся на дискету:", allBooks)

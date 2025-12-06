# TODO Найдите количество книг, которое можно разместить на дискете
disk_volume = 1.44 * 1024 * 1024
pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

book_size = pages * lines_per_page * chars_per_line * bytes_per_char
books_count = disk_volume // book_size
print("Количество книг, помещающихся на дискету:", int(books_count))

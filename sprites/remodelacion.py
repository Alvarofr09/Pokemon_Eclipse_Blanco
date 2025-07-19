from PIL import Image

imagen = Image.open("DS DSi - Pokemon Black White - Pokemon 5th Generation Back.png")

ancho_sprite = 98
alto_sprite = 104

columnas = 7
filas = 32

contador = 0
for fila in range(filas):
	for col in range(columnas):
		x0 = col * ancho_sprite
		y0 = fila * alto_sprite
		x1 = x0 + ancho_sprite
		y1 = y0 + alto_sprite
		sprite = imagen.crop((x0, y0, x1, y1))
		sprite.save(f"back/sprite_{contador + 1}_back.png")

		contador += 1
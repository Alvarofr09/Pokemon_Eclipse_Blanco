from PIL import Image

imagen = Image.open("front.png")

ancho_sprite = 96
alto_sprite = 103

columnas = 8
filas = 22

contador = 0
for fila in range(filas):
	for col in range(columnas):
		x0 = col * ancho_sprite
		y0 = fila * alto_sprite
		x1 = x0 + ancho_sprite
		y1 = y0 + alto_sprite
		sprite = imagen.crop((x0, y0, x1, y1))
		sprite.save(f"front/sprite_{contador + 1}_front.png")

		contador += 1
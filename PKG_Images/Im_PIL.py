# ------------------------  Технології Computer Vision з python -------------------------------

'''
Цифрова обробка зображень: ласичні алгоритми "сирої" обробки растрового зображення з апакетом  Pillow (PIL)
Джерела даних:
https://www.kaggle.com/datasets
https://www.sentinel-hub.com/
https://livingatlas2.arcgis.com/landsatexplorer/

Package         Version
--------------- -------
matplotlib      3.8.2
pillow          10.2.0

'''


import random
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN)

#------------------ Main class for all functions --------------------------------
class ImgVision: 

	def __init__(self, file_name, mix_file, finish_file):
		self.image = Image.open(file_name)  # відкриття файлу зображення
		self.draw = ImageDraw.Draw(self.image)  # створення інструменту для малювання
		self.width = self.image.size[0]   # визначення ширини картинки
		self.height = self.image.size[1]  # визначення висоти картинки
		self.pix = self.image.load()  # отримання значень пікселей для картинки
		self.mix = mix_file  
		self.finish = finish_file

	# --------------------- зчитування файлу зображення ----------------------
	def image_read(self) -> None:
		
		# self.pix[1, 1][1]: (x,y),(red, green, blue), де x,y — координати, а числовые значения RGB - в межах 0-255 кожне.
		print("START_im", "red=", self.pix[1, 1][0], "green=", self.pix[1, 1][1], "blue=", self.pix[1, 1][2])
		plt.imshow(self.image)
		plt.show()
		image_info = {"image_file": self.image, "image_draw": self.draw, "image_width": self.width, "image_height": self.height, "image_pix": self.pix}

		return image_info


	# --------------------- відтінкі сірого ----------------------
	def shades_of_gray(self) -> None:


		print('------- триває перетворення --------------')

		for i in range(self.width):
			for j in range(self.height):
				a = self.pix[i, j][0]
				b = self.pix[i, j][1]
				c = self.pix[i, j][2]
				S = (a + b + c) // 3  # усередненя пікселів
				self.draw.point((i, j), (S, S, S))

		plt.imshow(self.image)
		plt.show()
		print("STOP_im", "red=", self.pix[1, 1][0], "green=", self.pix[1, 1][1], "blue=", self.pix[1, 1][2])
		self.image.save(self.mix, "JPEG")
#		del self.draw
		print('------- перетворення завершене до файлу stop.jpg --------------')

		return


	# ------------------------- серпія  --------------------------
	def serpia(self) -> None:


		print('------- ведіть коефіціент серпії --------------')
		depth = int(input('depth:'))
		print('------- триває перетворення --------------')
		for i in range(self.width):
			for j in range(self.height):  # підрахунок середнього значення кольорової гами - перетворення з коефіціентом
				a = self.pix[i, j][0]
				b = self.pix[i, j][1]
				c = self.pix[i, j][2]
				S = (a + b + c) // 3
				a = S + depth * 2
				b = S + depth
				c = S
				if (a > 255):
					a = 255
				if (b > 255):
					b = 255
				if (c > 255):
					c = 255
				self.draw.point((i, j), (a, b, c))

		plt.imshow(self.image)
		plt.show()
		print("STOP_im", "red=", self.pix[1, 1][0], "green=", self.pix[1, 1][1], "blue=", self.pix[1, 1][2])
		self.image.save(self.mix, "JPEG")
#		del self.draw
		print('------- перетворення завершене до файлу stop.jpg --------------')

		return

	# ----------------------- негатив --------------------------
	def negative(self) -> None:

		
		print('------- триває перетворення --------------')
		for i in range(self.width):
			for j in range(self.height):
				a = self.pix[i, j][0]
				b = self.pix[i, j][1]
				c = self.pix[i, j][2]
				# від кожного пікселя віднімається 256 - макс. значення для кольору
				self.draw.point((i, j), (255 - a, 255 - b, 255 - c))

		plt.imshow(self.image)
		plt.show()
		print("STOP_im", "red=", self.pix[1, 1][0], "green=", self.pix[1, 1][1], "blue=", self.pix[1, 1][2])
		self.image.save(self.mix, "JPEG")

		print('------- перетворення завершене до файлу stop.jpg --------------')

		return

	# ----------------------- зашумлення ------------------------
	def noise(self) -> None:

		print('------- введіть коефіціент шуму --------------')
		factor = int(input('factor:'))
		print('------- триває перетворення --------------')
		for i in range(self.width):
			for j in range(self.height):
				rand = random.randint(-factor, factor)
				a = self.pix[i, j][0] + rand  # додавання рандомного числа
				b = self.pix[i, j][1] + rand
				c = self.pix[i, j][2] + rand
				if (a < 0):
					a = 0
				if (b < 0):
					b = 0
				if (c < 0):
					c = 0
				if (a > 255):
					a = 255
				if (b > 255):
					b = 255
				if (c > 255):
					c = 255
				self.draw.point((i, j), (a, b, c))

		plt.imshow(self.image)
		plt.show()
		print("STOP_im", "red=", self.pix[1, 1][0], "green=", self.pix[1, 1][1], "blue=", self.pix[1, 1][2])
		self.image.save(self.mix, "JPEG")
#		del self.draw
		print('------- перетворення завершене до файлу stop.jpg --------------')

		return

	# ---------------------- зміна яскравості  --------------------
	def brightness_change(self) -> None:

		print('введіть діапазон зміни яскравості: -100, +100')
		factor = int(input('factor:'))  # наприклад в діапазоні +100, -100
		print('------- триває перетворення --------------')
		for i in range(self.width):
			for j in range(self.height):
				a = self.pix[i, j][0] + factor  # одавання яскравості
				b = self.pix[i, j][1] + factor
				c = self.pix[i, j][2] + factor
				if (a < 0):
					a = 0
				if (b < 0):
					b = 0
				if (c < 0):
					c = 0
				if (a > 255):
					a = 255
				if (b > 255):
					b = 255
				if (c > 255):
					c = 255
				self.draw.point((i, j), (a, b, c))

		plt.imshow(self.image)
		plt.show()
		print("STOP_im", "red=", self.pix[1, 1][0], "green=", self.pix[1, 1][1], "blue=", self.pix[1, 1][2])
		self.image.save(self.mix, "JPEG")
#		del self.draw
		print('------- перетворення завершене до файлу stop.jpg --------------')

		return

	# --------------------------- монохромне зображення ------------------------
	def monochrome(self) -> None:

		print('------ введіть коефіціент розрізнення, в діапазоні 50-100 ----------')
		factor = int(input('factor:'))
		print('------- триває перетворення --------------')
		for i in range(self.width):
			for j in range(self.height):
				a = self.pix[i, j][0]
				b = self.pix[i, j][1]
				c = self.pix[i, j][2]
				S = a + b + c
				if (S > (((255 + factor) // 2) * 3)):  # рішення до якого з 2 кольорів поточне значення кольору ближче
					a, b, c = 255, 255, 255
				else:
					a, b, c = 0, 0, 0
				self.draw.point((i, j), (a, b, c))

		plt.imshow(self.image)
		plt.show()
		print("STOP_im", "red=", self.pix[1, 1][0], "green=", self.pix[1, 1][1], "blue=", self.pix[1, 1][2])
		self.image.save(self.mix, "JPEG")
#		del self.draw
		print('------- перетворення завершене до файлу stop.jpg --------------')

		return

	# ------------------ фільтрація - векторизація зображення ------------------------
	def contour_im(self) -> None:

		# -----------  фільтрація: покращення якості, ідентифікація ---------------
		image_filter = self.image.filter(CONTOUR)
		# self.image_filter = self.image.filter(BLUR)
		# self.image_filter = self.image.filter(DETAIL)

		plt.imshow(image_filter)
		plt.show()
		self.pix = image_filter.load()  # отримання значень пікселей для картинки
		print("STOP_im", "red=", self.pix[1, 1][0], "green=", self.pix[1, 1][1], "blue=", self.pix[1, 1][2])
		image_filter.save(self.finish, "JPEG")
		del self.draw
		print('------- перетворення завершене до файлу stop.jpg --------------')

		return

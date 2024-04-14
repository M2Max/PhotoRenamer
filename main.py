from renamer import Renamer
import os

def main():
	path = "D:\\Foto e Video\\Foto Piemonte Amici 2021"
	for name in os.listdir(path):
		ren = Renamer()
		ren.rename_media(os.path.join(path, name))

if __name__ == "__main__":
	main()
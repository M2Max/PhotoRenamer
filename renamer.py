from datetime import datetime
import os
from typing import Union

class Renamer():
	imageExtensions = ['.ras', '.xwd', '.bmp', '.jpe', '.jpg', '.jpeg', '.xpm', '.ief', '.pbm', '.tif', '.gif', '.ppm', '.xbm', '.tiff', '.rgb', '.pgm', '.png', '.pnm']
	videoExtensions = ['.m1v', '.mpeg', '.mov', '.qt', '.mpa', '.mpg', '.mpe', '.avi', '.movie', '.mp4']	

	def __init__(self) -> None:
		pass

	def rename_media(self, mediaPath):
		mediaMetadata = self.get_media_metadata(mediaPath)
		newName = os.path.dirname(mediaPath) + "\\" + mediaMetadata[0] + "_" + mediaMetadata[1] + mediaMetadata[2]
		print(newName)
		os.rename(mediaPath, newName)


	def get_media_metadata(self, mediaPath) -> Union[list, None]:
		_, fileExtension = os.path.splitext(mediaPath)
		stats = os.stat(mediaPath)
		timestamp = datetime.fromtimestamp(stats.st_ctime).strftime("%Y%m%d%H%M%S")
		timestamp = timestamp + str(int(stats.st_ctime_ns % 1000000000)).zfill(9)
		mediaType = "OTHER"
		if fileExtension in self.imageExtensions:
			mediaType = "IMAGE"
		elif fileExtension in self.videoExtensions:
			mediaType = "VIDEO"
		return [timestamp, mediaType, fileExtension]



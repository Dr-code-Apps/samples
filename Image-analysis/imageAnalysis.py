import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from PIL import Image


class imageAnalysis:

	def getArraysOnImage(self, inputImageFile, horizontalPosition, verticalPosition):
		"""
		Return lists of intensity distributions on a specified horizontal line and vertical line from a grayscale image.

		Prameters
    	----------
		inputImageFile :  String
			grayscale image of raster type (.jpg, .png, .tiff)
		horizontalPosition : Int
			Positional information of the perpendicular line to be acquired (pixel)
		verticalPosition : Int
			Positional information of the horizontal line to be acquired (pixel)

		Returns
	    -------
    	imageVerticalArray : Int List
        	Intensity distribution on a specified horizontal line in the image.
        	Black(min: 0) <--> White(max: 255)
        imageHorizontalArray : Int List
        	Intensity distribution on a specified vertical line in the image.
        	Black(min: 0) <--> White(max: 255)
		"""

		image = Image.open(inputImageFile)
		width, height = image.size

		if horizontalPosition > width:
			print("error!! HorizontalPosition is over the image width!!")
			print("must be within " + str(width) + " pixel!")
			sys.exit()
		if horizontalPosition <= 0:
			print("error!! HorizontalPosition is negative value!!")
			print("must be be a positive value!")
			sys.exit()
		if verticalPosition > height:
			print("error!! VerticalPosition is over the image height!!")
			print("must be within " + str(height) + " pixel!")
			sys.exit()
		if verticalPosition <= 0:
			print("error!! VerticalPosition is negative value!!")
			print("must be be a positive value!")
			sys.exit()

		imageHorizontalArray = np.zeros((width), dtype = int)
		imageVerticalArray = np.zeros((height), dtype = int)

		for y in range(height):
		    for x in range(width):
		        if x == horizontalPosition:
		            imageVerticalArray[y] = image.getpixel((x, y))
		        if y == verticalPosition:
		            imageHorizontalArray[x] = image.getpixel((x, y))

		return imageVerticalArray, imageHorizontalArray
	

	def plotGridSpecFigure(self, imageFile, horizontalPosition, verticalPosition):
		"""
		Return a pdf file of the input image with the intensity distribution.
		
		Prameters
    	----------
		imageFile :  String
			grayscale image of raster type (.jpg, .png, .tiff)
		horizontalPosition : Int
			Positional information of the perpendicular line to be acquired (pixel)
		verticalPosition : Int
			Positional information of the horizontal line to be acquired (pixel)
		"""
		
		image = Image.open(imageFile)
		width, height = image.size
		aspectRatio = width/height
		
		verticalArray, horizontalArray = self.getArraysOnImage(imageFile, horizontalPosition, verticalPosition)
		
		""" plot """
		fig = plt.figure(figsize=(5*aspectRatio, 5))
		gs = gridspec.GridSpec(2, 2, height_ratios=(4, 1), width_ratios=(1, 4))
		plt.title('vertical position : {:.0f} px, horizontal position : {:.0f} px'\
		            .format(verticalPosition, horizontalPosition), fontsize=13)
		plt.axis('off')
		plt.gray()

		""" 2nd of 2x2 matrix """
		ax2 = fig.add_subplot(gs[0, 1])
		ax2.plot([horizontalPosition, horizontalPosition],[0, height], "red", linestyle='dashed')
		ax2.plot([0, width],[verticalPosition, verticalPosition], "blue", linestyle='dashed')
		ax2.imshow(image, alpha=1.0)

		""" 1st of 2x2 matrix """
		ax1 = fig.add_subplot(gs[0, 0], sharey=ax2)
		maxValue = np.max(verticalArray)
		ax1.set_xlim([0, maxValue+10])
		ax1.set_ylim([height, 0])
		ax1 = plt.plot(verticalArray, range(height), "red")

		""" 4th of 2x2 matrix """
		ax4 = fig.add_subplot(gs[1, 1], sharex=ax2)
		maxValue = np.max(horizontalArray)
		ax4.set_xlim([0, width])
		ax4.set_ylim([0, maxValue+10])
		ax4 = plt.plot(horizontalArray, "blue")

		""" show """
		#plt.show()

		""" save as pdf """
		plt.savefig('FireFly_intensity_prof.pdf', dpi=600)


if __name__ == "__main__":

	horizontalPosition = 88 # (pixel)
	verticalPosition = 135  # (pixel)

	im = imageAnalysis()
	im.plotGridSpecFigure('FireFly_gray.jpg', horizontalPosition, verticalPosition)
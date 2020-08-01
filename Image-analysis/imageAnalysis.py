
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from PIL import Image

# ------------------------------------------------------------------
# variables
VerticalPosition = 145  # (pixel)
HorizontalPosition = 80 # (pixel)

# ------------------------------------------------------------------
# image data
image_name = 'FireFly_gray.jpg'
image = Image.open(image_name)
width, height = image.size

# ------------------------------------------------------------------
# input image data
imageHorizontalArray = np.zeros((width), dtype = int)
imageVerticalArray = np.zeros((height), dtype = int)

for y in range(height):
    for x in range(width):
        if x == HorizontalPosition:
            imageVerticalArray[y] = image.getpixel((x, y))
        if y == VerticalPosition:
            imageHorizontalArray[x] = image.getpixel((x, y))
# for check
# print(imageVerticalArray)
# print(imageHorizontalArray)

# ------------------------------------------------------------------
# plot images
fig = plt.figure(figsize=(8.84, 5))
gs = gridspec.GridSpec(2, 2, height_ratios=(4, 1), width_ratios=(1, 4))
plt.title('vertical position : {:.0f} px, horizontal position : {:.0f} px'\
            .format(VerticalPosition, HorizontalPosition), fontsize=13)
plt.axis('off')
plt.gray()

# 2x2の2番目
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot([HorizontalPosition, HorizontalPosition],[0, height], "red", linestyle='dashed')
ax2.plot([0, width],[VerticalPosition, VerticalPosition], "blue", linestyle='dashed')
ax2.imshow(image, alpha=1.0)

# 2x2の1番目
ax1 = fig.add_subplot(gs[0, 0], sharey=ax2)
maxValue = np.max(imageVerticalArray)
ax1.set_xlim([0, maxValue+10])
ax1.set_ylim([height, 0])
ax1 = plt.plot(imageVerticalArray, range(height), "red")

# 2x2の4番目
ax4 = fig.add_subplot(gs[1, 1], sharex=ax2)
maxValue = np.max(imageHorizontalArray)
ax4.set_xlim([0, width])
ax4.set_ylim([0, maxValue+10])
ax4 = plt.plot(imageHorizontalArray, "blue")

# show
plt.show()

# ------------------------------------------------------------------

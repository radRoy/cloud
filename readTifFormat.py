import skimage
"""import numpy as np
import os.path"""

if __name__ == "__main__":

    file = "M:/data/d.walther/Microscopy/babb03/tiff-ct3/-crop-bicubic-scaled0.25-autofluo-hyperstackSequence/" \
           "id01-Ch405,488,561nm-crop-scaled0.25-hyperstackSequence.tif"
    image = skimage.io.imread(file)
    print("shape:", image.shape)

    file = "M:/data/d.walther/Microscopy/babb03/tiff-ct3/-crop-bicubic-scaled0.25-autofluo-hyperstackRGB24/" \
           "id01-Ch405,488,561nm-crop-scaled0.25-hyperstackRGB.tif"
    image = skimage.io.imread(file)
    print("shape:", image.shape)

    file = "M:/data/d.walther/Microscopy/babb03/tiff-ct3/-crop-bicubic-scaled0.25-autofluo-hyperstackRGB24-czyx/" \
           "id01-Ch405,488,561nm-crop-scaled0.25-hyperstackRGB-czyx.tif"
    image = skimage.io.imread(file)
    print("shape:", image.shape)

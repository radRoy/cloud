import skimage
import os


def main(file_list=["M:/data/d.walther/Microscopy/babb03/tiff-ct3/-crop-bicubic-scaled0.25-autofluo-hyperstackSequence/id01-Ch405,488,561nm-crop-scaled0.25-hyperstackSequence.tif", "M:/data/d.walther/Microscopy/babb03/tiff-ct3/-crop-bicubic-scaled0.25-autofluo-hyperstackRGB24/id01-Ch405,488,561nm-crop-scaled0.25-hyperstackRGB.tif", "M:/data/d.walther/Microscopy/babb03/tiff-ct3/-crop-bicubic-scaled0.25-autofluo-hyperstackRGB24-czyx/id01-Ch405,488,561nm-crop-scaled0.25-hyperstackRGB-czyx.tif"]):

    for file in file_list:

        if os.path.isfile(file):
            image = skimage.io.imread(file)
            print("shape:", image.shape)

        else:
            print("File", file, "does not exist.")

    return 0


if __name__ == "__main__":

    files = ["M:/data/d.walther/Microscopy/babb03/tiff-ct3/-crop-bicubic-scaled0.25-autofluo-hyperstackSequence/id01-Ch405,488,561nm-crop-scaled0.25-hyperstackSequence.tif",
             "M:/data/d.walther/Microscopy/babb03/tiff-ct3/-crop-bicubic-scaled0.25-autofluo-hyperstackRGB24/id01-Ch405,488,561nm-crop-scaled0.25-hyperstackRGB.tif",
             "M:/data/d.walther/Microscopy/babb03/tiff-ct3/-crop-bicubic-scaled0.25-autofluo-hyperstackRGB24-czyx/id01-Ch405,488,561nm-crop-scaled0.25-hyperstackRGB-czyx.tif"]

    main(files)

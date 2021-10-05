import os
from PIL import Image


def get_size(fp):
    """
    Retrieve the size of the file in KB.
    :param fp: file path
    :return: the size in KB of the file
    """

    return os.path.getsize(fp) // 1024


def compress_image(fp, ts, step=1, quality=95):
    """
    Transform the given image to jpg format and compress it without changing its resolution.
    :param fp: the file path which is to be compressed
    :param ts: target size after compression, in KB
    :param step: everytime the amount quality decreases
    :param quality: the quality of an image in jpg
    :return: the file path of the compressed file
    """

    file_size = get_size(fp)
    root = os.path.splitext(fp)[0]
    ofp = "{}-out{}".format(root, '.jpg')

    if file_size <= ts:
        print("No need to compress!")
    else:
        while file_size > ts:
            with Image.open(fp) as img:
                img.save(ofp, quality=quality)
            if quality - step < 0:
                print("Target size is too small!")
                break
            else:
                quality -= step
            file_size = get_size(ofp)

    return ofp


infp = input("Enter the image path: \n")
target_size = int(input("Enter the target size in KB: \n"))
outfp = compress_image(infp, target_size)
print("Finished! Go to {} and check!".format(outfp))

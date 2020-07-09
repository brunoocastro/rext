#!/usr/bin/python

###########################################
# REXT - V 1.0
# Text Remover
# First version of this software
# thats object is remove text from
# specific images of an competition dataset

# Use rext.py -h to see how to use
###########################################

import numpy as np
from matplotlib import pyplot as plt
import cv2
import sys
import getopt


# Clean Function
# The core funcition of this script
def clean(img, show = False):
    # Option defines which InPainting method will be used
    # If option = 1, will use TELEA method
    # If option = 2, will use NS method
    option = 1

    # Some Params
    # for LaPlace operator
    ddepth = cv2.CV_16S 
    kernel_size = 15
    
    # Kernel for morfoligy operations
    # 3 by 3 and 8-conected
    kernel = np.ones((3,3),np.uint8)
    
    ## IMAGE PROCESSING

    # Converting image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Canny Edge Implementation
    canny = cv2.Canny(gray,900,1000)
    
    # Implementation of LaPlace Operator
    lp = cv2.Laplacian(canny, ddepth, ksize=kernel_size)

    # Image binary convertion 
    _, bc = cv2.threshold(lp, 127, 255, cv2.THRESH_BINARY)

    #Modifying the morphology of the image
    #Dilating
    di = cv2.dilate(bc, kernel, iterations = 4)

    # 8-bit transform
    final_mask = np.uint8(di)

    # InPaint implementation
    ip1 = cv2.inpaint(img, final_mask, 3, cv2.INPAINT_TELEA)
    ip2 = cv2.inpaint(img, final_mask, 3, cv2.INPAINT_NS)

    if option == 2:
        final = cv2.cvtColor(ip2, cv2.COLOR_RGB2BGR)
    else:
        final = cv2.cvtColor(ip1, cv2.COLOR_RGB2BGR)

    # Show the result (optional)
    # To show with matplotlib
    # an visual result before
    # a final image
    if show == True: 
        plt.subplot(421),plt.imshow(img, cmap = 'gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(422),plt.imshow(gray, cmap = 'gray')
        plt.title('Grayscale Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(423),plt.imshow(canny, cmap = 'gray')
        plt.title('Canny Edge'), plt.xticks([]), plt.yticks([])
        plt.subplot(424),plt.imshow(lp, cmap = 'gray')
        plt.title('LaPlace Operator'), plt.xticks([]), plt.yticks([])
        plt.subplot(425),plt.imshow(bc, cmap = 'gray')
        plt.title('Binary Mask'), plt.xticks([]), plt.yticks([])
        plt.subplot(426),plt.imshow(di, cmap = 'gray')
        plt.title('Final Mask'), plt.xticks([]), plt.yticks([])
        plt.subplot(427),plt.imshow(ip1, cmap = 'gray')
        plt.title('InPainting "TELEA"'), plt.xticks([]), plt.yticks([])
        plt.subplot(428),plt.imshow(ip2, cmap = 'gray')
        plt.title('InPainting "NS"'), plt.xticks([]), plt.yticks([])
        plt.show()
        
    return final

def main(argv):
    # Path to the image to be processed
    image_path = ''
    # Name of final image
    filename = ''
    # If true, shows all steps of image processing
    show = True

    # Recieving 
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
    except getopt.GetoptError:
        print('python3 rext.py -i <input_img_path>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('python3 rext.py -i <input_image>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            image_path = arg
    
    filename = 'new_' + image_path

    # Using cv2.imread() method 
    # to read the image 
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    if image is None:
        print("Use rext.py -h to help")
        sys.exit("Could not read the image.")
    else:
        # Init program print's
        print("REXT - A image remove text script")
        print("")
        print("Image to process:", image_path)
        print("Image shape:     ", image.shape)
        print("Final file name: ", filename)

    # Converting from BGR to RGB 
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Calling the function
    final_img = clean(img, show)

    # Saving the final image 
    cv2.imwrite(filename, final_img) 

if __name__ == "__main__":
    main(sys.argv[1:])
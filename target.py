import cv2

def findTarget(image):
    '''Returns centre coordinates (x,y), dimensions (height, width),
    inclination angle, and the tweaked image (for manual/automatic 
    checking - not actually used by the robot itself).
    '''
    
    # Convert from BGR colourspace to HSV. Makes thresholding easier.
    ##hsv_image = ???
    
    # Threshold the image to only get the green of the target. This gives us a
    # mask to apply to the original image (if we want).
    # Hue values are in degrees, but OpenCV only takes single byte arguments,
    # which means a maximum of 255. To get around this OpenCV takes hue values
    # in the range [0, 180]. This means 120 degrees (for example) maps to 60 in
    # OpenCV.
    ##mask = ???
    
    # The thresholding will leave some ragged edges, and some rogue points in
    # the mask. Use a Gaussian Blur to smooth this out.
    ##blurred = ???
    
    # OpenCV can find contours in the image - essentially closed loops of edges.
    # We are expecting the largest contour is the target.
    # First get all the contours:
    ##contours = ???
    
    # Now find the largest and do some sanity checking to make sure we have
    # actually got a target in view.
    ##largest = ???
    ## <insert sanity checking here>
    
    # We know our target is a rectangle. This means we can fit a bounding box
    # to it. We should make it an oriented bounding box (OBB) because if the
    # target is to the side it appears on an angle in our image.
    ##obb = ???
    
    # Now that we have an OBB we can get its vital stats to return to the
    # caller. Remember that these numbers need to be independent of the size
    # of the image (we can't return them in pixels). Scale everything relative
    # to the image - between [-1, 1]. So (1,1) would be the top right of the
    # image, (-1,-1) bottom left, and (0,0) dead centre.
    ## x = ???
    ## y = ???
    ## w = ???
    ## h = ???
    ## angle = ???
    
    # We can return an altered image so that we can check that things are
    # working properly.
    ## result_image = <something with image and one of the intermediate steps -
    ##                 mask, blurred, contours, obb, etc>
    
    ####################
    # Dummy values to get it working
    (x, y, w, h, angle) = (0, 0, 0, 0, 0)
    result_image = image
    ####################
    
    return x, y, w, h, angle, result_image
    
if __name__ == "__main__":
    # Load an image. This could be a test image from a file,
    # or a frame from the video stream
    # Store it in a variable called 'image'
    
    ##image = ???
    
    ################
    # Dummy image to get it going
    import numpy as np
    image = np.zeros((480, 640, 3), np.uint8)
    image[:] = (0, 180, 0) # BGR
    ################
    
    x, y, w, h, angle, processed_image = findTarget(image)
    cv2.namedWindow("preview")
    cv2.imshow("preview", processed_image)
    
    # Wait for a key, or the preview image just disappears...
    key = cv2.waitKey(0)
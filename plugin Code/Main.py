import cv2

import os

# prompt= " login screen landscape light theme"

# def is_landscape(image_path):
#     image = cv2.imread(image_path)
#     height, width, _ = image.shape
#     return width > height

# def is_portrait(image_path):
#     image = cv2.imread(image_path)
#     height, width, _ = image.shape
#     return width < height

# def check_image_orientation(image_path):
#     image1_is_landscape = is_landscape(image_path)
#     image1_is_portrait = is_portrait(image_path)

#     orientation = ""

#     if image1_is_landscape:
#         print(f"{image_path} image have landscape orientation.")
#         orientation = "landscape"
#     elif not image1_is_portrait:
#         print(f"{image_path} image have portrait orientation.")
#         orientation = "portrait"
#     else :
#         print(f"unable to find orientation of image {image_path}.")
#     return orientation, image_path


#     # Provide the paths of the two images you want to compare
# image_paths = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
# if "landscape" in prompt:
#     landscape_img = []
#     for image_path in image_paths :
#      orientation, image = check_image_orientation(image_path)
#      if orientation == "landscape" :
#          landscape_img.append(image)
    
# elif "portrait" in prompt:
#     portrait_img = []
#     for image_path in image_paths :
#      orientation, image = check_image_orientation(image_path)
#      if orientation == "portrait" :
#          portrait_img.append(image)
# else :
#     print("invalid prompt")

def extract_input_boxes(image_path, output_directory):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding
    _, thresholded = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours based on area and aspect ratio
    min_area = 500  # Minimum contour area to consider
    aspect_ratio_range = (0.5, 2.0)  # Range of aspect ratios to consider

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Extract and save each input box as a separate image
    for i, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        x, y, width, height = cv2.boundingRect(contour)
        aspect_ratio = width / float(height)

        if area > min_area and aspect_ratio >= aspect_ratio_range[0] and aspect_ratio <= aspect_ratio_range[1]:
            input_box = image[y:y+height, x:x+width]
            output_path = os.path.join(output_directory, f"input_box_{i+1}.jpg")
            cv2.imwrite(output_path, input_box)

# Usage example
image_path = "demo.png"
output_directory = "h"

extract_input_boxes(image_path, output_directory)

# import cv2
# import numpy as np

# strength = 0 
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
#     return orientation

# def compare_images(image1, image2):
#     # Load the images
#     img1 = cv2.imread(image1)
#     img2 = cv2.imread(image2)

#     # Convert images to HSV color space
#     hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
#     hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

#     # Calculate histograms for each image
#     hist1 = cv2.calcHist([hsv1], [0, 1], None, [180, 256], [0, 180, 0, 256])
#     hist2 = cv2.calcHist([hsv2], [0, 1], None, [180, 256], [0, 180, 0, 256])

#     # Normalize the histograms
#     cv2.normalize(hist1, hist1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
#     cv2.normalize(hist2, hist2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

#     # Calculate histogram comparison using Chi-Square method
#     similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CHISQR)

#     return similarity

# def get_image_size_opencv(image_path):
#     image = cv2.imread(image_path)
#     height, width, _ = image.shape
#     return width, height

#     # Provide the paths of the two images you want to compare
# image1_path = '1.jpg'
# image2_path = "2.jpg"
# orientation = check_image_orientation(image1_path)
# # -------------------------------------------------------------------------------------------------------------------

# if orientation == "landscape" :
#     strength += 100
# # -------------------------------------------------------------------------------------------------------------------


#     # Compare the images
#     similarity_score = compare_images(image1_path, image2_path)

#     # Calculate the percentage similarity
#     percentage_similarity = similarity_score / 100

#     # Define a threshold value to determine similarity
#     threshold = 20.0
#     data = 0
#     # Check if the percentage similarity is below the threshold
#     if percentage_similarity < threshold:
#         print(f"The images are {percentage_similarity}% similar.")
#         strength += percentage_similarity
#     else:
#         print(f"The images are {percentage_similarity}% similar.")
#         strength += percentage_similarity

# # -------------------------------------------------------------------------------------------------------------------
# if orientation == "portrait" :
#     strength += 100
# # -------------------------------------------------------------------------------------------------------------------

#     # Provide the paths of the two images you want to compare
#     image1_path = '1.jpg'
#     image2_path = '2.jpg'

#     # Compare the images
#     similarity_score = compare_images(image1_path, image2_path)

#     # Calculate the percentage similarity
#     percentage_similarity = similarity_score / 100

#     # Define a threshold value to determine similarity
#     threshold = 20.0

#     # Check if the percentage similarity is below the threshold
#     if percentage_similarity < threshold:
#         print(f"The images are {percentage_similarity}% similar.")
#         strength += percentage_similarity
#     else:
#         print(f"The images are {percentage_similarity}% similar.")
#         strength += percentage_similarity

# # -------------------------------------------------------------------------------------------------------------------

# print(strength*100/400)
    
    


#     # quality = ""
    
#     # width, height = get_image_size_opencv(image1_path)
#     # width2, height2 = get_image_size_opencv(image2_path)
#     # print("Image size:", width, "x", height)
#     # if height > 4000 and width > 3000 :
#     #     strength += 50
#     #     quality = "good"
#     # elif height > 2000 and width > 1500 :
#     #     quality = "average"
#     #     strength += 25
#     # elif height > 1000 and width > 750 :
#     #     quality = "poor"
#     #     strength += 13

import cv2

GAUSSIAN_BLUR_FILTER_SIZE = (5, 5)
GAUSSIAN_BLUR_SIGMA_X = 0
CANNY_THRESHOLD_1 = 200
CANNY_THRESHOLD_2 = 450


def get_gaussian_blur_image(image):
    return cv2.GaussianBlur(image, GAUSSIAN_BLUR_FILTER_SIZE, GAUSSIAN_BLUR_SIGMA_X)


def get_canny_image(image):
    return cv2.Canny(image, CANNY_THRESHOLD_1, CANNY_THRESHOLD_2)


def get_contours(image):
    contours, _ = cv2.findContours(image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def get_contour_area_threshold(image_width, image_height):
    contour_area_min = (image_width * 0.15) * (image_height * 0.25) * 0.8
    contour_area_max = (image_width * 0.15) * (image_height * 0.25) * 1.2
    return contour_area_min, contour_area_max


def get_arc_length_threshold(image_width, image_height):
    arc_length_min = 2 * ((image_width * 0.15) + (image_height * 0.25)) * 0.8
    arc_length_max = 2 * ((image_width * 0.15) + (image_height * 0.25)) * 1.2
    return arc_length_min, arc_length_max


def get_offset_threshold(image_width):
    offset_min = 0.2 * image_width
    offset_max = 0.85 * image_width
    return offset_min, offset_max


image_raw = cv2.imread("image.png")
image_height, image_width, _ = image_raw.shape
image_gaussian_blur = get_gaussian_blur_image(image_raw)
image_canny = get_canny_image(image_gaussian_blur)
contours = get_contours(image_canny)


contour_area_min, contour_area_max = get_contour_area_threshold(image_width, image_height)
arc_length_min, arc_length_max = get_arc_length_threshold(image_width, image_height)
offset_min, offset_max = get_offset_threshold(image_width)
offset = None
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if contour_area_min < cv2.contourArea(contour) < contour_area_max and arc_length_min < cv2.arcLength(contour, True) \
            < arc_length_max and offset_min < x < offset_max:
        cv2.rectangle(image_raw, (x, y), (x + w, y + h), (0, 255, 0), 2)
        offset = x
cv2.imwrite("image_result.png", image_raw)
print('offset:', offset)
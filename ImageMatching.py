from typing import Sequence
import cv2 as cv
import numpy as np


def image_matching(sample_img: np.ndarray, item_id: int) -> tuple[Sequence[int], tuple[int, int]] | None:

    # Getting a copy of the image for modification
    h, w = 0, 0
    pattern_img = np.ndarray

    # Bruh, they fr got swtich statements in python(3.10) now lol.
    match item_id:
        case 0:  # Pal sphere
            pattern_img = cv.imread('items/pal_sphere.png')
            assert pattern_img is not None, "File could not be read"
        case 1:
            pattern_img = cv.imread('items/Max_img.png')
            assert pattern_img is not None, "File could not be read"
        case 2:
            pattern_img = cv.imread('items/Start_img.png')
            assert pattern_img is not None, "File could not be read"
        case 4:
            pattern_img = cv.imread('items/Acquire_img.png')
            assert pattern_img is not None, "File could not be read"
        case 10:  # Mega sphere
            pattern_img = cv.imread('items/mega_sphere.png')
            assert pattern_img is not None, "File could not be read"
        case 11:  # Giga sphere
            pattern_img = cv.imread('items/giga_sphere.png')
            assert pattern_img is not None, "File could not be read"
        case 12:  # Arrows
            pattern_img = cv.imread('items/arrows.png')
            assert pattern_img is not None, "File could not be read"
        case 13:  # Fire Arrows
            pattern_img = cv.imread('items/fire_arrows.png')
            assert pattern_img is not None, "File could not be read"
        case 14:  # Nails
            pattern_img = cv.imread('items/nails.png')
            assert pattern_img is not None, "File could not be read"
        case 15:  # Cement
            pattern_img = cv.imread('items/cement.png')
            assert pattern_img is not None, "File could not be read"
        case 16:  # Low Grade Medical
            pattern_img = cv.imread('items/low_grade_medical_supplies.png')
            assert pattern_img is not None, "File could not be read"
        case 17:  # Medical
            pattern_img = cv.imread('items/medical_supplies.png')
            assert pattern_img is not None, "File could not be read"
        case 18:  # High Grade Medical
            pattern_img = cv.imread('items/high_grade_medical_supplies.png')
            assert pattern_img is not None, "File could not be read"
        case _:
            print('Invalid case...')
            exit(-1)

    # Getting the dimensions of each pattern images respectfully
    h, w, _ = pattern_img.shape

    # Start template matching using the TM_CCOEFF_NORMED algo
    # More on the different types of algos that can be used
    # Here: https://docs.opencv.org/3.4/d4/dc6/tutorial_py_template_matching.html
    res = cv.matchTemplate(sample_img, pattern_img, cv.TM_CCOEFF_NORMED)

    # We use the .where() function to get the max_locations of objects that closly
    # resemble the pattern image based off a threshold.

    threshold = 0.80
    _, max_val, _, max_loc = cv.minMaxLoc(res)

    if max_val >= threshold:
        print(max_val)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        return top_left, bottom_right

    return None

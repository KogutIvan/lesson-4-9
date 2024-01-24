from PKG_Images.Im_PIL import (
    ImgVision
)
# import package_functions
# from package_functions import module_1, module_2, module_3

# from package_classes import (
#     MyClass_my_cv_dict,
#     MyClass_my_cv_file_w,
#     MyClass_my_cv_file_r,
#     MyClass_f_digit_detector
# )

def package_image_main_def():
    file_name_start = 'Kharkiv_map2.jpg'
    file_name_stop = "stop.jpg"
    file_name_filter = "stop_filter.jpg"

    print('оберіть тип перетворення!')
    print('0 - відтінки сірого')
    print('1 - серпія')
    print('2 - негатив')
    print('3 - зашумлення')
    print('4 - зміна яскравості')
    print('5 - монохромне зображення')
    #print('6 - фільтр-векторизатор')  # always it does
    mode = int(input('mode:'))
    Img = ImgVision(file_name_start, file_name_stop, file_name_filter)
    if (mode == 0): Img.shades_of_gray()
    elif (mode == 1): Img.serpia()
    elif (mode == 2): Img.negative()
    elif (mode == 3): Img.noise()
    elif (mode == 4): Img.brightness_change()
    elif (mode == 5): Img.monochrome()
    Img.contour_im()

    return


if __name__ == '__main__':
    # package_functions_main_def()
    # package_class_main_def()
    package_image_main_def()
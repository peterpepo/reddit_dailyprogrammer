from PIL import Image


def is_grey(pixel):
    """
    Returns true if passed pixel is grey, otherwise returns false.
    """
    return pixel[0] == pixel[1] == pixel[2]


def find_colored(image):
    """
    Finds first non-grey pixel.
    """
    image_pixels = image.getdata()

    i=0
    while is_grey(image_pixels[i]):
        i += 1

    return i


def roll_image(image, amount):
    image_width, image_height = image.size

    amount = amount % image_width
    new_left_part = image.crop((0, 0, amount, image_height))
    new_right_part = image.crop((amount, 0, image_width, image_height))

    new_image = Image.new(image.mode, image.size)
    new_image.paste(new_right_part, (0,0))
    new_image.paste(new_left_part, (image_width-amount, 0))

    return new_image

image_name = "test_rMYBq14.PNG"

output_image_name = image_name.split(".")[0] + "_UNSCRAMBLED." + image_name.split(".")[1]

source_image = Image.open(image_name)

image_width, image_height = source_image.size

new_image = Image.new(source_image.mode, source_image.size)

# Cycle through image rows
for image_line_index in range(image_height):

    # Chop off single line of image
    image_line = source_image.crop((0, image_line_index, image_width, image_line_index+1))

    roll_amount = find_colored(image_line)
    image_line = roll_image(image_line, roll_amount)

    new_image.paste(image_line, (0, image_line_index))

new_image.save(output_image_name, "PNG")
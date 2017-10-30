from PIL import Image

image_name = "test_rMYBq14.PNG"
output_image_name = image_name.split(".")[0] + "_UNSCRAMBLED_." + image_name.split(".")[1]

source_image = Image.open(image_name)

image_width, image_height = source_image.size

new_image = Image.new(source_image.mode, source_image.size)

# Cycle through image rows
for image_line_index in range(image_height-1):

    # Chop off single line of image
    image_line = source_image.crop((0, image_line_index, image_width, image_line_index+1))

    roll_amount = 10
    # Find colored pixel in the line
    image_line_pixels = image_line.getdata()
    for current_pixel_index in range(len(image_line_pixels)):
        current_pixel = image_line_pixels[current_pixel_index]
        is_grey = current_pixel[0] == current_pixel[1] == current_pixel[2]

        if not(is_grey):
            roll_amount = current_pixel_index


    # print(image_line)
    # Roll line

    roll_amount = roll_amount % image_width

    new_image_line_part1 = source_image.crop((0, image_line_index, roll_amount, image_line_index+1))
    new_image_line_part2 = source_image.crop((roll_amount, image_line_index, image_width, image_line_index+1))
    new_image_line_part1.load()
    new_image_line_part2.load()

    new_image.paste(new_image_line_part2, (0, image_line_index, image_width-roll_amount, image_line_index+1))
    new_image.paste(new_image_line_part1, (image_width-roll_amount, image_line_index, image_width, image_line_index+1))

    # new_image.paste(image_line, (0, image_line_index, image_width, image_line_index+1))

new_image.save(output_image_name, "PNG")
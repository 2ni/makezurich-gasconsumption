from PIL import Image
import pytesseract

def find_numbers(image_path):
    # Load and convert the image to Pillow format
    image = Image.open(image_path)

    # Use Tesseract for Optical Character Recognition (OCR)
    text_detected = pytesseract.image_to_string(image)

    # Filter out only the numbers
    numbers = ''.join(filter(str.isdigit, text_detected))

    return numbers

# Main code block
if __name__ == '__main__':
    image_path = './gasmeter2.jpg'  # Specify the path of the image to be analyzed
    numbers = find_numbers(image_path)
    print("Numbers in the image: " + numbers)

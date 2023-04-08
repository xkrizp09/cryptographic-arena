from PIL import Image

def decode_text():

    input_image = Image.open("Enter image name: ")

    binary_data = ""

    # získat pixelová data obrázku
    pixel_data = list(input_image.getdata())

    # projít všechny pixely obrázku a načíst zakódovanou zprávu
    for pixel in pixel_data:
        red, green, blue = pixel

        # načíst nejnižší bity z každého kanálu barvy pixelu
        binary_data += str(red & 1)
        binary_data += str(green & 1)
        binary_data += str(blue & 1)

    # převést binární řetězec na původní zprávu
    message = ''
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        message += chr(int(byte, 2)) 

    return message

def encode():
    print("ahoj")
    return

def main():
    a = int(input(":: Vitejte ve steganographii ::\n" "1. Kodovani \n2. Dekodovani\n"))
    if (a == 1):
        encode()
    elif (a == 2):
        print("Decoded Word :  " + decode_text())
    else:
        raise Exception("Enter correct input")
 
# Driver Code
if __name__ == '__main__' :
 
    # Volal hlavni funkci
    main()

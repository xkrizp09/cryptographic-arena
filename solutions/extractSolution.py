import cv2
import sys
     
def showData(image):
    # Load the image
    image = cv2.imread(image) 
    
    binary_data = ""
    decoded_data = ""
    
    # Convert pixel values to binary format
    for row in image:
        for pixel in row:
            #convert the red, green and blue values into binary format
            r, g, b = helperFunctions.messageToBinary(pixel) 
            
            #extracting data from the least significant bit of red pixel
            binary_data += r[-1]
            
            #extracting data from the least significant bit of green pixel
            binary_data += g[-1]
            
            #extracting data from the least significant bit of red pixel
            binary_data += b[-1]
          
    # split by 8-bits
    all_bytes = helperFunctions.splitBinaryData(binary_data)
  
    # convert from bits to characters from all_bytes
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        
        #check if we have reached the delimeter which is ";;;"
        if decoded_data[-3:] == ";;;":
            break
        
    #remove the delimeter to show the original hidden message  
    return decoded_data[:-3]
     
def main():
    if len(sys.argv) == 2:
        image = sys.argv[1]
        print("Decoded message is " + showData(image)) 
    else:
        print("Chyba: Musíte zadat jeden parametr.")

if __name__ == "__main__":
    main()
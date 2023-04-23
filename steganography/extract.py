import cv2
import sys
from helperFunctions import messageToBinary, splitBinaryData  
     
def extractData(image):
    # Load the image
    image = cv2.imread(image) 
    
    binary_data = ""
    decoded_data = ""
    
    # Convert pixel values to binary format
    for row in image:
        for pixel in row:
            #convert the red, green and blue values into binary format, check helperFunctions
            
            #extracting data from the least significant bit of red pixel
            
            #extracting data from the least significant bit of green pixel
            
            #extracting data from the least significant bit of red pixel
          
    # split by 8-bits
    all_bytes = splitBinaryData(binary_data)
  
    for byte in all_bytes:
        # convert from bits to characters from all_bytes
        decoded_data += chr(int(byte, 2))
        
      #check if we have reached the delimeter which is ";;;"  
      
       
    #remove the delimeter to show the original hidden message  
    return decoded_data[:-3]
              
def main():
    if len(sys.argv) == 2:
        image = sys.argv[1]
        print(extractData(image)) 
    else:
        print("Error: you have to run it with the parameter.")

if __name__ == "__main__":
    main()
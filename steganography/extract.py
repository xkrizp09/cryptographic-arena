import cv2
import numpy as np
import sys
     
def showData(image):
    # Load the image
    image = cv2.imread(image) 
    
    binary_data = ""
    decoded_data = ""
    all_bytes = []
    
    # Convert pixel values to binary format
    for row in image:
        for pixel in row:
            #convert the red, green and blue values into binary format
            
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

# define a function called "messageToBinary" that takes a single argument "message"
def messageToBinary(message):  # define a function called "messageToBinary" that takes a single argument "message"
    if type(message) == str:  # check if "message" is a string 
        return ''.join([ format(ord(i), "08b") for i in message ])# convert each character of the string to its binary representation using the "ord" function and format it as an 8-bit string with leading zeros ("08b"); join the resulting binary strings together and return as a single string
    elif type(message) == bytes or type(message) == np.ndarray:  # check if "message" is a bytes or numpy array object
        return [ format(i, "08b") for i in message ] # apply binary formatting to each element of the array using a list comprehension and return a list of binary strings
    elif type(message) == int or type(message) == np.uint8:  # check if "message" is an integer or numpy uint8 object
        return format(message, "08b") # format the integer directly as an 8-bit binary string and return it
    else:  # if "message" is not one of the supported types, raise a TypeError with a custom error message
      raise TypeError("Vstup neni podporovan")

# Split a binary string into 8-bit chunks
def splitBinaryData(binary_data):
    chunks = [] # Define a list to store the 8-bit chunks
    
    for i in range(0, len(binary_data), 8): # Iterate over the binary string with a step size of 8
        chunk = binary_data[i: i+8] # Extract an 8-bit chunk starting from the current index and append it to the list
        chunks.append(chunk)
        
    return chunks # Return the list of 8-bit chunks
                
def main():
    if len(sys.argv) == 2:
        image = sys.argv[1]
        print("Tajná zprava je: " + showData(image)) 
    else:
        print("Chyba: Musíte zadat jeden parametr.")

if __name__ == "__main__":
    main()
import cv2
import sys
import helperFunctions

     
def extractData(image):
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
    all_bytes = helperFunctions.splitBinaryData(binary_data)
  
    for byte in all_bytes:
        # convert from bits to characters from all_bytes
        decoded_data += chr(int(byte, 2))
        
      #check if we have reached the delimeter which is ";;;"  
      
       
    #remove the delimeter to show the original hidden message  
    return decoded_data[:-3]
              
def main():
    if len(sys.argv) == 2:
        image = sys.argv[1]
        print("Tajná zprava je: " + extractData(image)) 
    else:
        print("Chyba: Musíte zadat jeden parametr.")

if __name__ == "__main__":
    main()
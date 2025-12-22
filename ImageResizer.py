"""
This is a mini project which rescales a give image into the given scale percentage
---20-12-2025
"""
import cv2

source="<image to be resized>"
destination=f"{source}_resized.jpg"
scale_percentage=int(input("Enter scaler percentage:"))

src=cv2.imread(source,cv2.IMREAD_UNCHANGED)
 
new_width=int(src.shape[1]*scale_percentage/100)
new_height=int(src.shape[0]*scale_percentage/100)

output=cv2.resize(src,(new_width,new_height))

cv2.imwrite(destination,output)
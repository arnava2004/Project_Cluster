# Python program to open the 
# camera in Tkinter 
# Import the libraries, 
# tkinter, cv2, Image and ImageTk 
  
from tkinter import *
import cv2 
from PIL import Image, ImageTk 


  
# Define a video capture object 
camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
  
# Declare the width and height in variables 
width, height = 800, 600
  
# Set the width and height 
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width) 
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height) 
  
# Create a GUI app 
app = Tk() 
  
# Bind the app with Escape keyboard to 
# quit app whenever pressed 
app.bind('<Escape>', lambda e: app.quit()) 
  
# Create a label and display it on app 
label_widget = Label(app) 
label_widget.pack() 
  
# Create a function to open camera and 
# display it in the label_widget on app 
  
  
def open_camera(): 
  
    # Capture the video frame by frame 
    _, frame = camera.read() 
  
    # Convert image from one color space to other 
  
    # Capture the latest frame and transform to image 
    captured_image = Image.fromarray(frame) 
  
    # Convert captured image to photoimage 
    photo_image = ImageTk.PhotoImage(image=captured_image) 
  
    # Displaying photoimage in the label 
    label_widget.photo_image = photo_image 
  
    # Configure image in the label 
    label_widget.configure(image=photo_image) 
  
    # Repeat the same process after every 10 seconds 
    label_widget.after(10, open_camera) 
    app.bind("<q>", lambda e: cv2.imwrite("test.jpg", frame))
    def readImage():
        image_path = "C://Users//Arnav//Desktop//Projects//Project_Cluster//test.jpg"
        

    
    app.bind("<e>", lambda e: readImage())


  
# Create a button to open the camera in GUI app 
button1 = Button(app, text="Open Camera", command=open_camera) 
button1.pack() 
  
# Create an infinite loop for displaying app on screen 
app.mainloop()

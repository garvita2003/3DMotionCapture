# 3DMotionCapture
This project focuses on creating a virtual video motion capture system using Python and Unity, leveraging powerful libraries like CVZone and MediaPipe. The system detects and tracks 33 different key landmarks of an object (or body) in a video, storing their 3D coordinates (x, y, z) in an `animation.txt` file. The captured data can then be used for real-time animations or game development. 

# Technologies Used: 
1. Python: For video processing, landmark detection, and data storage.
   - MediaPipe: Used for detecting and tracking 33 different key landmarks of the body/object in a video.
   - CVZone: Simplifies working with computer vision pipelines and visualizes detected landmarks.
2. Unity: To create a 3D virtual environment for animation rendering and playback.
3. AnimationCode: For generating animations based on captured data.
4. LineCode: For smooth rendering and interpolation of movement between frames.

# Workflow  
1. Landmark Detection:  
   - Use MediaPipe to detect landmarks in each frame of the video.
   - Extract the (x, y, z) coordinates of the 33 detected landmarks.
2. Data Storage:  
   - Save the coordinates frame-by-frame into an `animation.txt` file.
3. Unity Integration:  
   - Load the `animation.txt` file into Unity.
   - Use AnimationCode and LineCode to visualize the motion capture in a 3D environment.
4. Real-Time Applications:  
   - Generate animations for games, simulations, or virtual avatars using the processed motion data.
     
![Screenshot 2025-01-04 173840](https://github.com/user-attachments/assets/ea3b6795-123b-458b-9e52-a44f960c75e3)

# Overview:

https://github.com/user-attachments/assets/897a7e4f-87f7-4c82-9de1-8371aae2ea48


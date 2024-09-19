#program for predicting if aday is weekend day or
"""""
weekend = ['sunday', 'saturday']
day = input("Enter a day of the week to verify if it is a weekend: ")
if day in weekend:
    print("It's the weekend! Let's enjoy the show!")
else:
    print("Please go to work, we are not in the weekend.")
    """
"""""
# Calculating Area of rectangle
Length = float(input("Enter Length: "))
Width = float(input("Enter Width: "))

# Calculate the area of the rectangle
Area = Length * Width
print("Area of my Rectangle is:", Area)
"""

# face recorgination python script


import cv2
import face_recognition

# Load a sample image and learn how to recognize it.
image_of_person = face_recognition.load_image_file("person.jpg")
person_encoding = face_recognition.face_encodings(image_of_person)[0]

# Create an array of known face encodings and their corresponding names
known_face_encodings = [person_encoding]
known_face_names = ["Person Name"]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# Start video capture
video_capture = cv2.VideoCapture(0)

while True:
    # Capture each frame of the video
    ret, frame = video_capture.read()

    # Resize frame to 1/4 size for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video for performance
    if process_this_frame:
        # Find all face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Check if the face matches known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # Use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
video_capture.release()
cv2.destroyAllWindows()




# import cv2 as cv
#
# img=cv.imread('D:\wot.png')
#
# cv.namedWindow('Image')
# cv.imshow('Image',img)
# cv.waitKey(0)
# cv2.destroyAllWindows()
import face_recognition
import cv2
import time


# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
Mine_image = face_recognition.load_image_file("zike.png")
Mine_face_encoding = face_recognition.face_encodings(Mine_image)[0]
t0 = time.time()
video_writer=cv2.VideoWriter('face.flv',cv2.VideoWriter_fourcc('F','L','V','1'),30,(640,480))
print('frame_count=',video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
print('frame_width=',video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print('frame_heith=',video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('FPS=',video_capture.get(cv2.CAP_PROP_FPS))
print(video_capture.get(cv2.CAP_PROP_FOURCC))

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    #frame=cv2.threshold(frame)
    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)


    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces([Mine_face_encoding], face_encoding,tolerance=0.5)

        name = "Unknown"
        if match[0]:
            name = "Zike"
            print('find Me')
            # import os
            # os.system('music.mp3')
            # time.sleep(5)
            # Draw a box around the face
            video_writer.write(frame)

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)



    cv2.imshow('Video', frame)

    # write to file

    print time.time() - t0
    t0 = time.time()

    # Display the resulting image
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
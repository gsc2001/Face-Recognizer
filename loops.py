import procesess as prc
import cv2
from save_face import save


def search_loop(camera) -> None:
    """
    Main search loop function
    :param camera: A cv2.VideoCapture object to read the webcam
    :return:
    """
    assert isinstance(camera, cv2.VideoCapture), 'Invalid camera object passed'
    process_this = True
    faces = []
    while True:
        ret, frame = camera.read()
        if process_this:
            faces = prc.process_faces(frame)
        process_this = not process_this
        prc.assign_faces(faces)
        prc.mark_faces(frame, faces)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def save_loop(camera, name: str) -> None:
    """
    Loop to save face
    :param camera: A cv2.VideoCapture object to read the webcam
    :param name:   Name of the person
    :return: None
    """
    faces = []
    process_this = True
    face_to_be_saved = None
    while True:
        ret, frame = camera.read()
        if process_this:
            faces = prc.process_faces(frame)
        process_this = not process_this
        # changing name of each face to empty string
        message = ''
        if len(faces) == 1:
            face_to_be_saved = faces[0]
            face_to_be_saved.assign_name('')
        elif len(faces) > 1:
            message = 'More than 1 face detected'
        else:
            message = 'No face detected'
        prc.mark_faces(frame, faces)
        cv2.putText(frame, message, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    if face_to_be_saved is not None:
        save(face_to_be_saved, name)
    else:
        print("Couldn't save the face")

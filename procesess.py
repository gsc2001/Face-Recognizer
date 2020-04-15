import face_recognition as fr
import cv2
from face_class import Face
import numpy as np
from search import find_face


def process_faces(frame=None) -> list:
    """
    A function which process the given frame for faces
    :param frame:
    :return: Returs a list of faces ( object of class faces )
    """
    faces = []
    # reducing the size of frame to fasten the process
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # converting bgr frame of cv2 to rgb
    rgb_small = small_frame[:, :, ::-1]

    face_locations = fr.face_locations(rgb_small)
    face_encodings = fr.face_encodings(rgb_small, model='large')
    for location, encoding in zip(face_locations, face_encodings):
        # multiply face locations by 4 because we initially compressed them
        location = tuple(map(lambda x: x * 4, location))
        current_face = Face(location, encoding)
        faces.append(current_face)

    return faces


def assign_faces(faces):
    for face in faces:
        find_face(face)


def mark_faces(frame=None, faces=None):
    """
    Function to mark faces in current frame
    :param frame: frame in which to draw rectangles
    :param faces: list of faces
    :return: None
    """
    for face in faces:
        cv2.rectangle(frame, face.location[0], face.location[1], face.color, 3)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, face.name, face.text_location, font, 1.0, face.color, 1)

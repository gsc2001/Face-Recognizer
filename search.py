from face_class import Face
import pandas as pd
import face_recognition as fr
from random import random


# try to open faces.csv if available 

c = ['{}'.format(i) for i in range(128)] + ['names']
faces_df = pd.DataFrame({},columns=c)
try:
    faces_df = pd.read_csv('faces.csv')
except FileNotFoundError:
    pass


known_names = list(faces_df['names'])
known_faces = faces_df[faces_df.columns[:-1]].to_numpy()
colors = {}


def find_face(face: Face = None) -> None:
    """
    Function to search for name of the face and color and set its name
    :param face: Face to search for
    :return: None
    """
    if not face:
        raise AssertionError('Face not supplied')
    distances = fr.face_distance(known_faces, face.encoding)

    # initializing current minimum distance to tolerance value (0.6)
    min_dis = 0.6
    for i in range(len(distances)):
        if distances[i] < min_dis:
            face.assign_name(known_names[i])
            min_dis = min(distances[i], min_dis)
    if face.name in colors.keys():
        color_of_border = colors[face.name]
    else:
        color_of_border = (255, 255, 255)
        color_of_border = list(map(lambda x: int(x * random()), color_of_border))
        colors[face.name] = color_of_border
    face.assign_color(color_of_border)


def update_data() -> None:
    """
    Funciton to update the data after saving from save_face.py
    :return: None
    """
    global known_faces, known_names, faces_df
    faces_df = pd.read_csv('faces.csv')

    known_names = list(faces_df['names'])
    known_faces = faces_df[faces_df.columns[:-1]].to_numpy()

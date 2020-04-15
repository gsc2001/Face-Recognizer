# File to get face and save its encodings to faces.csv
from face_class import Face
import pandas as pd
from search import update_data

faces_df = pd.read_csv('faces.csv')


def save(face: Face = None, name: str = None) -> None:
    global faces_df
    """
    Function which saves the encodings of given face to faces.csv
    :param face: A Face object whose encodings need to be stored
    :param name: Name of the person
    :return:
    """
    # if person name already in csv just update it
    name = name.capitalize()
    # print('Gurkirat' in faces_df.names)
    if name in list(faces_df.names):
        # print(name)
        faces_df = faces_df[faces_df.names != name]
    to_add = pd.Series(face.encoding)
    col = [f'{i}' for i in range(128)] + ['names']
    face_df = pd.DataFrame([list(to_add) + [name]], columns=col)
    faces_df = pd.concat([faces_df, face_df])
    faces_df.to_csv('faces.csv', index=False)
    update_data()

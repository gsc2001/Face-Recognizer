class Face:
    """
    Class to store a face
    """

    def __init__(self, location, encoding):
        self.location = (location[3], location[0]), (location[1], location[2])
        self.encoding = encoding
        self.name = 'Unknown'
        self.color = (255, 255, 255)
        self.text_location = location[3] + 6, location[2] - 6

    def assign_name(self, name):
        self.name = name

    def assign_color(self, color):
        self.color = color

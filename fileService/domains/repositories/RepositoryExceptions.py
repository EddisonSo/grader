class MissingFilenameException(Exception):
    def __init__(self, message=None):
        print("Missing filename!")
        if message:
            print(message)

class UnkownDBError(Exception):
    def __init__(self, message=None):
        print("An unkown error has occured!")
        if message:
            print(message)

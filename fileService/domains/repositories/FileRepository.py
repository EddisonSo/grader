from domains.models.file import File
from domains.repositories.RepositoryExceptions import *
from sqlalchemy.orm import Session

class FileRepository:
    db_session: Session

    """
    Initialize FileRepository object and pass in db_session using dependency injection pattern
    """
    def __init__(self, db_session:Session):
        self.session = db_session

    """
    Description: Add new file object to be persisted using a file object
    Arguments: A file object represented the file to be persisted in the db
    Returns: File object that was created
    Throws: UnknownDBError if there was a problem persisting the file data
    """
    def _add_file(self, file: File):
        try:
            self.session.add(file)
            self.session.commit()
            return file
        except:
            raise UnkownDBError(None)

    """
    Description: Add new file object to be persisted
    Arguments: file_name for the file to be stored. Keep in mind file_name does not have to be unique as files are stored internally by its uuid.
    Returns: File object that was created
    Throws: MissingFilenameException if file_name was not specified
    """
    def add_file(self, file_name):
        new_file = File()

        if not file_name:
            raise MissingFilenameException(None)

        new_file.set_mapped_name(file_name)
        return self._add_file(new_file)


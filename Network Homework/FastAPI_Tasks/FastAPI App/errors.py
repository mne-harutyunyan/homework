'''This is a module for the errors'''

from fastapi import HTTPException

class ValidationError(HTTPException):
    '''Raised when input data fails validation.'''

    def __init__(self, message: str,status_code=400):
        super().__init__(status_code=status_code, detail=message)

class FileError(HTTPException):
    '''Raised when JSON files are missing, corrupted, or unreadable.'''

    def __init__(self, message: str,status_code=400):
        super().__init__(status_code=status_code, detail=message)

class NotFoundError(HTTPException):
    ''' Raised when a user or task with the given ID is not found.'''

    def __init__(self, message: str,status_code=404):
        super().__init__(status_code=status_code, detail=message)

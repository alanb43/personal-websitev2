"""Swetter development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'\xc2\xf8\xf5\xaa\x12\x88\xc3\xf9\xca'
SECRET_KEY += b'\xc4\xf0\x15\xf2\x13KyX%-\t\xb7\x0ca'
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
BERGFLIX_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = BERGFLIX_ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/insta485.sqlite3
DATABASE_FILENAME = BERGFLIX_ROOT/'var'/'insta485.sqlite3'
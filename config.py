# lokale database settings
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_HOST = 'localhost'  # without port number
DB_PASSWORD = 'password'
DB_ALCHEMY_URI_LOC = 'postgresql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_NAME

# database settings BAA
DB_NAME_BAA = '???'
DB_USER_BAA = '???'
DB_HOST_BAA = '???'
DB_PASSWORD_BAA = '???'
DB_ALCHEMY_URI_BAA = 'postgresql://' + DB_USER_BAA + ':' + DB_PASSWORD_BAA + '@' + DB_HOST_BAA + '/' + DB_NAME_BAA

# Database Tables
DB_LOC_TABLENAME = 'dm_informatieportal'
DB_BAA_TABLENAME = 'dm_informatieportal'

# SQL Alchemy setting
SQLALCHEMY_DATABASE_URI = 'postgresql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_NAME

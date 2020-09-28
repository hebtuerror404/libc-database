import os

ES_INDEX_NAME = 'libcsearch'

# ES_HOST = 'localhost'
ES_HOST = 'es01'

# DB_DIR = os.path.dirname(os.path.abspath(__file__)) + '/../db'
DB_DIR = '/db'

DEFAULT_SYMBOLS = [
    '__libc_start_main_ret',
    'system',
    'dup2',
    'str_bin_sh',
    'read',
    'write',
    'puts',
    'printf',
]
DOWNLOAD_URL = 'http://127.0.0.1/download/{}.so'

#config variables in this file should not reach git, fill it with your own values
SECRET_KEY = 'THESECRETKEY'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/test'
SECRET_CONFIG_READING_TEST = 'Its a magical place.'
MAILGUN_PVT_API_KEY = 'key-xxxxxxxxxxxxxxxxxxxx'
EMAIL_DOMAIN = 'xxxxx.mailgun.org'
HMAC_KEY = 'I have the high ground Anakin'
TEMP_UPLOAD_FOLDER = 'files/temp/'
VIDEO_REPOSITORY = 'files/repository/'
LOGS_DIR = 'files/logs/'
OUTPUT_DIR = 'files/output/'
ENABLE_KVM = True
KVM_LINUX_NAME = 'ubuntu'
LINUX_JOBS_DIR = 'files/mount/jobs/'
KVM_WINDOWS_NAME = ''
WINDOWS_JOBS_DIR = ''
KVM_MAC_NAME = ''
MAC_JOBS_DIR = ''

ENABLE_LOCAL_MODE = False
"""
Only to be filled in case of local mode:
"""
ADMIN_NAME = 'Administrator'
ADMIN_EMAIL = 'admin@ccextractor.web'
ADMIN_PWD = 'admin@ccextractor.web'

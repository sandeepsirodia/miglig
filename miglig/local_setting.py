SECRET_KEY = 'vf-u%bj@f(ytd))6bi*3@*pxdo*fcp^=_$bddapf034njp_w$7'

DATABASES = {
   'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'miglig',
      'USER': 'miglig',
      'PASSWORD': 'testing',
      'HOST': 'localhost',
      'PORT': '',
   }
}


ALLOWED_HOSTS = [
	'159.89.162.102',
    'http://127.0.0.1:8000',
    'localhost:4200',
    'localhost:8000',
    'localhost',
    '127.0.0.1',
    'http://127.0.0.1',
    'http://www.miglig.com',
    'https://miglig.com',
    'http://api.miglig.com',
    '.miglig.com'
]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:8000',
    'localhost:4200',
    'localhost:8000',
    'localhost',
    'http://127.0.0.1',
    'http://www.miglig.com',
    'https://miglig.com',
    'http://api.miglig.com',
    '.miglig.com'
]























# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home/'
# SOCIAL_AUTH_LOGIN_URL = '/'

# AWS_S3_ACCESS_KEY_ID = 'AKIAIVQMPTT3VTSPUDJQ'
# AWS_S3_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'devtraansport'

# EMAIL_BACKEND = 'django_ses.SESBackend'

# AWS_ACCESS_KEY_ID = 'AKIAIVQMPTT3VTSPUDJQ'
# AWS_SECRET_ACCESS_KEY = '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'

# # Additionally, if you are not using the default AWS region of us-east-1,
# # you need to specify a region, like so:
# AWS_SES_REGION_NAME = 'us-west-2'
# AWS_SES_REGION_ENDPOINT = 'email.us-west-2.amazonaws.com'


# GOOGLE_MAPS_KEY = "AIzaSyDsu939PIsm4MzpUkZ7zZrTe6mAG6Xt20M"

# AWS_S3_SECURE_URLS = True  # use http instead of https
# S3_URL = 'http://s3-eu-west-1.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME
# # MEDIA_ROOT = 'media/'
# # STATIC_ROOT = '/static/'
# # STATIC_URL = S3_URL + STATIC_ROOT
# # MEDIA_URL = S3_URL + '/' + MEDIA_ROOT


# CORS_ALLOW_METHODS = (
#     'GET',
#     'POST',
#     'PUT',
#     'PATCH',
#     'DELETE',
#     'OPTIONS'
# )
# CORS_ORIGIN_REGEX_WHITELIST = ('^(http?://)?([\w-]+\.)?traansport\.com\/?(\/[.\w]*)*', '^(https?://)?([\w-]+\.)?traansport\.com\/?(\/[.\w]*)*')

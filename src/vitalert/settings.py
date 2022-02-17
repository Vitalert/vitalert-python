
import os
# COGNITO
USER_POOL_ID = os.environ['USER_POOL_ID']
ADMIN_GROUP_NAME = "admin"
PRO_GROUP_NAME = 'pro'
PREMIUM_GROUP_NAME = 'premium'
BASIC_GROUP_NAME = 'basic'
NOPLAN_GROUP_NAME = 'noPlan'

# APPSYNC
API_URL = os.environ['API_URL']
API_KEY = os.environ['API_KEY']
API_HEADERS = {"x-api-key": API_KEY}


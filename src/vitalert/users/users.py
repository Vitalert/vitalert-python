from typing import List


import vitalert.settings as st
from vitalert.users.user import User

# AWS
import boto3



class Users:
    def __init__(self) -> None:
        self.client = boto3.client('cognito-idp')

    def getProUsers(self) -> List[User]:
        """Retrieves Pro users"""
        users = self.client.list_users_in_group(UserPoolId=st.USER_POOL_ID, GroupName=st.PRO_GROUP_NAME)["Users"]
        return [User(data, st.PRO_GROUP_NAME) for data in users]

    def getPremiumUsers(self) -> List[User]:
        """Retrieves Premium users"""
        users = self.client.list_users_in_group(UserPoolId=st.USER_POOL_ID, GroupName=st.PREMIUM_GROUP_NAME)["Users"]
        return [User(data, st.PREMIUM_GROUP_NAME) for data in users]

    def getBasicUsers(self) -> List[User]:
        """Retrieves basic users"""
        users = self.client.list_users_in_group(UserPoolId=st.USER_POOL_ID, GroupName=st.BASIC_GROUP_NAME)["Users"]
        return [User(data, st.BASIC_GROUP_NAME) for data in users]

    def getNoPlanUsers(self) -> List[User]:
        """Retrieves noPlan users"""
        users = self.client.list_users_in_group(UserPoolId=st.USER_POOL_ID, GroupName=st.NOPLAN_GROUP_NAME)["Users"]
        return [User(data, st.NOPLAN_GROUP_NAME) for data in users]


users = Users()

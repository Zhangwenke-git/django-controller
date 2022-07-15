from datetime import datetime


'''
在url中使用    #path('login/',obtain_jwt_token),时，才会调用该方法
'''
def jwt_response_handler(token,user=None,request=None):
    print(user,dir(user))
    jwt_res = {
        "result":True,
        "msg":"登录成功",
        "code":10002,
        "login_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),
        "info":{
            "token": token,
            "user": user.user_id,
            "name": user.name,
            "email":user.email
        }


    }

    return jwt_res
#
# from rest_framework.settings import
# from rest_framework_jwt.settings import
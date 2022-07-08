

dict_ = {"field": "user_id", "type": 1, "val": 2}

mapping = {"字符串":0,"整型":1,"Null":2,"空字符串":3,"True":4,"False":5,"浮点型":6,"JSON类型":7,"List类型":8}


import copy
import json
from string import Template


def parser(param:dict):
    param_copy = copy.deepcopy(param)
    type_ = param_copy["type"]
    val = param_copy["val"]
    try:
        if int(type_)==0:
            param_copy.update(val=str(val))
        elif int(type_) == 1:
            param_copy.update(val=int(val))
        elif int(type_) == 2:
            param_copy.update(val=None)
        elif int(type_) == 3:
            param_copy.update(val="")
        elif int(type_) == 4:
            param_copy.update(val=True)
        elif int(type_) == 5:
            param_copy.update(val=False)
        elif int(type_) == 6:
            param_copy.update(val=float(val))
        elif int(type_) in(7,8):
            param_copy.update(val=json.loads(val))
        else:
            raise AttributeError("Wrong data type.")
    except Exception as e:
        raise NotImplementedError(f"Fail to convert data due to error: {str(e)}")
    else:
        return param_copy


def parser_request_info(data:dict):
    header = data.get("header")
    if header:
        header = {item["field"]:item["val"] for item in header}
    param = data.get("default")
    if param:
        param_ = list(map(parser,param))
        param = {item["field"]:item["val"] for item in param_}
    template = data.get("data")
    if template and param:
        template = template.replace("{{","$").replace("}}","")
        template = json.loads(Template(template).safe_substitute(param))

    method = data.get("method")
    if int(method) == 0:
        method = "GET"
    elif int(method) == 1:
        method = "POST"
    elif int(method) == 2:
        method = "PUT"
    elif int(method) == 3:
        method = "DELETE"
    else:
        raise ValueError("Method value error.")
    data.update(
        header=header,
        data=template,
        method=method
    )
    return data


"""

{'url': 'http://192.168.246.128:9000/api/auth', 'header': [{'field': 'Content-Type', 'val': 'application/json'}], 'method': '1', 'data': '{"username": "{{u
sername}}", "password": "{{password}}"}', 'default': [{'field': 'username', 'type': 0, 'val': 'eee'}, {'field': 'password', 'type': 0, 'val': 'eeee'}]} 
"""

if __name__ =="__main__":
    print(parser(dict_))

    info = {'url': 'http://192.168.246.128:9000/api/auth', 'header': [{'field': 'Content-Type', 'val': 'application/json'},{'field': 'token', 'val': 'EWQEWDASDDEFEWREW'}], 'method': '1', 'data': '{"username": "{{username}}", "password": "{{password}}","check":1}', 'default': [{'field': 'username', 'type': 0, 'val': 'eee'}, {'field': 'password', 'type': 0, 'val': 'eeee'}]}
    print(parser_request_info(info))
dict_ = {"field": "user_id", "type": 7, "val": 2}

mapping = {"字符串":0,"整型":1,"Null":2,"空字符串":3,"True":4,"False":5,"浮点型":6,"JSON类型":7,"List类型":8}


import copy
import json
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




if __name__ =="__main__":
    print(parser(dict_))

import json
import copy
from functools import reduce

"""输出的格式，也是执行引擎输入的格式
{
    "uid": "6a4841c0f9d843cdb84a8171ea869039",
    "casetemplate": {
        "uid": "fd33fccdd5c541b28d1b6b3cd9488faf",
        "statue_display": "有效",
        "method_display": "POST",
        "statue": 1,
        "create_time": "2022-05-18T09:52:11.600052",
        "update_time": "2022-06-04T20:19:36.666887",
        "name": "AGGR登录",
        "url": "http://127.0.0.1:9091/user/login/",
        "method": 1,
        "header": {
            "Content-Type": "application/json"
        },
        "data": {
            "user_id": "{{user_id}}",
            "password": "{{password}}"
        },
        "process_name": "",
        "linux_order_str": "",
        "table_name": "",
        "owner": "root"
    },
    "statue_display": "有效",
    "priority_display": "高",
    "module": "AGGR",
    "class_title": "中台聚合",
    "create_time": "2022-05-18T09:04:43.422381",
    "update_time": "2022-05-18T09:52:29.506619",
    "case": "login_api",
    "case_title": "登录接口",
    "case_description": "登录接口测试",
    "priority": 0,
    "owner": "root",
    "template": "fd33fccdd5c541b28d1b6b3cd9488faf",
    "testsuit": "ec26f6793e7b4508912a4ec8e74f2efe",
    "scenarios": [
        [
            {
                "user_id": "root",
                "password": "Ccwtn@123"
            },
            "用户名和密码均正确",
            {
                "$.code": 1002,
                "$.result": true,
                "$.data.user_id": "root"
            }
        ],
        [
            {
                "password": "22312321"
            },
            "用户名和密码均错误",
            {
                "$.code2": 1002,
                "$.result": false
            }
        ]
    ]
}

"""

def case_parser(params, *args, **kwargs):
    """
    将case进行解析，解析为执行引擎可识别的数据
    @param params:
    @param args:
    @param kwargs:
    @return:dict，需将dict包装为list
    """
    expect = {}
    active_scenarios = filter(lambda x:x["statue"]==1,params["details"])
    # scenarios = [[item["parameter"],item["scenario"],item["validator"]] for item in active_scenarios]

    scenarios=[]
    for item in active_scenarios:
        p_dict_,v_dict_ = {},{}
        for k,v in item["parameter"].items():
            k_=k.split("@")[0]
            p_dict_.update({k_:v})
        for k,v in item["validator"].items():
            k_=k.split("@")[0]
            v_dict_.update({k_:v})
        scenarios.append([p_dict_,item["scenario"],v_dict_])

    expect.update(params["summary"])
    expect.update(scenarios=scenarios)
    return expect


def module_parser(params, *args, **kwargs):
    """
    将module或多个case进行解析，解析为执行引擎可识别的数据
    @param params:
    @param args:
    @param kwargs:
    @return: list
    """
    active_cases = filter(lambda x:x["statue"]==1,params["details"])
    expects = []
    for case in active_cases:
        case_copy = copy.deepcopy(case)
        # scenarios = [[item["parameter"], item["scenario"], item["validator"]] for item in case["case_scenario"]]
        scenarios = []
        for item in case["case_scenario"]:
            p_dict_, v_dict_ = {}, {}
            for k, v in item["parameter"].items():
                k_ = k.split("@")[0]
                p_dict_.update({k_: v})
            for k, v in item["validator"].items():
                k_ = k.split("@")[0]
                v_dict_.update({k_: v})
            scenarios.append([p_dict_, item["scenario"], v_dict_])
        del case_copy["case_scenario"]
        case_copy.update(scenarios=scenarios)
        expects.append(case_copy)
    return expects


def project_parser(params, *args, **kwargs):
    """
    将project或者多个module进行解析，解析为执行引擎可识别的数据
    @param params:
    @param args:
    @param kwargs:
    @return: list
    """
    active_modules = filter(lambda x: x["statue"] == 1, params["details"])
    expects = []
    for module in active_modules:
        active_cases=filter(lambda x: x["statue"] == 1, module["suit_case"])
        expect = []
        for case in active_cases:
            case_copy = copy.deepcopy(case)
            # scenarios = [[item["parameter"], item["scenario"], item["validator"]] for item in case["case_scenario"]]
            scenarios = []
            for item in case["case_scenario"]:
                p_dict_, v_dict_ = {}, {}
                for k, v in item["parameter"].items():
                    k_ = k.split("@")[0]
                    p_dict_.update({k_: v})
                for k, v in item["validator"].items():
                    k_ = k.split("@")[0]
                    v_dict_.update({k_: v})
                scenarios.append([p_dict_, item["scenario"], v_dict_])
            del case_copy["case_scenario"]
            case_copy.update(scenarios=scenarios)
            expect.append(case_copy)
        expects.append(expect)
    res = list(reduce(lambda x,y:x+y,expects))
    return res


if __name__ == "__main__":
    sample ={
    "type": "case",
    "summary": {
        "uid": "d8cd49276da64e40b1ba7a083d651099",
        "casetemplate": {
            "uid": "82a8b78e78a34f4ca793663d457dc18a",
            "statue_display": "有效",
            "method_display": "POST",
            "statue": 1,
            "create_time": "2022-04-09T20:37:02.284546",
            "update_time": "2022-05-17T14:28:32.960718",
            "name": "kms_login",
            "url": "https://element-plus.gitee.io/zh-CN/component/loading.html",
            "method": 1,
            "header": {
                "Content-Type": "application/json"
            },
            "data": {
                "password": "{{password}}",
                "username": "{{username}}"
            },
            "process_name": "tbs-dq-ts",
            "linux_order_str": "",
            "table_name": "user_info",
            "owner": "root"
        },
        "statue_display": "有效",
        "module": "KMS",
        "class_title": "kms",
        "create_time": "2022-04-09T21:12:04.323575",
        "update_time": "2022-05-08T09:39:24.618754",
        "case": "kms_login",
        "case_title": "KMS登录接口",
        "case_description": "kms_login",
        "owner": "root",
        "template": "82a8b78e78a34f4ca793663d457dc18a",
        "testsuit": "6da637c62c64471db32b101d117b7f9e"
    },
    "details": [
        {
            "uid": "1b8eadb51c0c40e497a028d04a90ffbd",
            "statue_display": "作废",
            "priority_display": "Medium",
            "testcase": "kms_login",
            "statue": 0,
            "create_time": "2022-05-08T19:27:28.061799",
            "update_time": "2022-05-17T13:56:44.305213",
            "scenario": "ffff",
            "parameter": {
                "name": "223243",
                "agress": "232344jhgjg",
                "password": "aaa1111!",
                "username": "44444",
                "username2": "44444",
                "username3": "44444",
                "username4": "44444",
                "username5": "44444",
                "username6": "44444",
                "username7": "44444",
                "username8": "44444",
                "username9": "44444",
                "username10": "44444",
                "username11": "44444"
            },
            "validator": {
                "code": 200,
                "result": " sussess"
            },
            "priority": 1,
            "owner": "root",
            "cases": "d8cd49276da64e40b1ba7a083d651099"
        },
        {
            "uid": "7b8232e83fad451aa68aad66c5f48b8b",
            "statue_display": "有效",
            "priority_display": "Medium",
            "testcase": "kms_login",
            "statue": 1,
            "create_time": "2022-05-08T13:34:21.672804",
            "update_time": "2022-05-17T13:56:41.811248",
            "scenario": "YYYYYYY",
            "parameter": {
                "password": "aaa1111!",
                "username": "44444"
            },
            "validator": {
                "code": 200,
                "result": " sussess"
            },
            "priority": 1,
            "owner": "root",
            "cases": "d8cd49276da64e40b1ba7a083d651099"
        }
    ]
}
    case_parser(sample)
    X="222"


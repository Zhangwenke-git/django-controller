import re
import json

def remove_character(string: str):
    character = ['$', '{', '}']
    for char_ in character:
        string = string.replace(char_, '')
    return string

def parameterized_fields(case_template):
    filed_pattern = r'\{{(.+?)\}}'
    comment = re.compile(filed_pattern, re.DOTALL)
    field_list = comment.findall(json.dumps(case_template))
    fields = list(map(remove_character, field_list))
    fields = list(set(fields))

    func_pattern = r'\$\{.+?>'
    comment = re.compile(func_pattern, re.DOTALL)
    func_list = comment.findall(json.dumps(case_template))
    func = list(map(remove_character, func_list))
    fields = list(set(fields))
    func_dict_list = []
    for fun in func:
        func_dict = {}
        fun_list = fun.split("|")
        try:
            func_dict[fun_list[0]] = fun_list[1]
        except IndexError:
            raise NameError(f"The separative sign '|' in function string: [{fun_list[0]}] not found!")
        func_dict = {k: list(v.replace('<', '').replace('>', '').split(',')) for k, v in
                     func_dict.items()}  # 处理参数的中特殊字符，并转换成tuple格式
        func_dict_list.append(func_dict)

    for temp in func_dict_list:
        for k, v in temp.items():
            if v[0] == "":
                temp.update({k: None})
            else:
                pass

    return fields,func_dict_list
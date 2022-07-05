def parser_counts_by_task(task:str,dict_list:list):
    if len(dict_list) > 0:
        for index,dict_ in enumerate(dict_list):
            if task == dict_["task"]:
                return dict_["counts"]
    return

def delete_dict_by_task(task:str,dict_list:list):
    if len(dict_list)>0:
        for index,dict_ in enumerate(dict_list):
            if task == dict_["task"]:
                del dict_list[index]
    return dict_list



if __name__ == "__main__":
    dict_list = [
        {
            "task": "PERIOD39c2edb0f680403285b4d77cbf61841e",
            "counts": 1
        },
        {
            "task": "PERIODec9aa257dc034058a27e2356ff1ea6b6",
            "counts": 0
        }

    ]

    print(parser_counts_by_task('PERIOD39c2edb0f680403285b4d77cbf61841',dict_list))
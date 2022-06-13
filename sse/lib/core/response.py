from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from sse.lib.utils.logger import logger

logger = logger()

class APIResponse(Response):
    def __init__(self,data=None, msg='success',result=True,status=HTTP_200_OK, headers=None, **kwargs):
        _data = {"msg": msg,"result":result}
        if data:
            _data.update(data=data)
        _data.update(**kwargs)
        if _data["result"]:
            pass
        else:
            try:
                _data["error"] = _data["error"].title()
            except AttributeError:
                status=HTTP_400_BAD_REQUEST
            logger.error(f"An error occurred:{_data}")
        super().__init__(data=_data, status=status, headers=headers)
